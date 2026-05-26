#!/usr/bin/env python3
"""
doctor.py — Verificacao de integridade do internal-audit-ops.
Checa arquivos essenciais, workflows, skills, method-wiki e perfis de cliente.
"""

import sys
import re
import json
import unicodedata
from datetime import date, datetime
from urllib.parse import unquote
from pathlib import Path

from wcgw_loader import (
    DEFAULT_WCGW_MASTER,
    VALID_SCOT_PHASES,
    VALID_SEVERITIES,
    get_wcgw_items,
    group_wcgw_by_process,
)

ROOT = Path(__file__).parent.parent

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"

def ok(label):
    return {"pass": True, "level": "ok", "label": label}

def fail(label, fix):
    return {
        "pass": False,
        "level": "error",
        "label": label,
        "fix": fix if isinstance(fix, list) else [fix],
    }


def warn(label, fix):
    return {
        "pass": True,
        "level": "warning",
        "label": label,
        "fix": fix if isinstance(fix, list) else [fix],
    }


def normalize_token(value):
    cleaned = value.strip()
    cleaned = re.sub(r"[*`]", "", cleaned)
    cleaned = cleaned.split("#", 1)[0].strip()
    cleaned = unicodedata.normalize("NFKD", cleaned).encode("ascii", "ignore").decode("ascii")
    cleaned = cleaned.lower().replace("-", "_").replace("/", " ")
    cleaned = re.sub(r"[^a-z0-9_ ]", "", cleaned)
    cleaned = re.sub(r"\s+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned


def should_skip_state_candidate(raw_value):
    raw = raw_value.strip().lower()
    if not raw:
        return True
    if any(marker in raw for marker in ["[", "]", "{", "}", "<", ">", "...", " / "]):
        return True
    return False


def parse_states_catalog(content):
    object_alias = {
        "engagement": "engagement",
        "area": "area",
        "achado": "achado",
        "plano_de_acao": "plano_de_acao",
    }
    states_by_object = {k: set() for k in object_alias.values()}
    aliases = set()

    current_top = None
    in_states = False
    current_alias_key = None

    for line in content.splitlines():
        if re.match(r"^[^\s].*:\s*$", line):
            top_name = normalize_token(line.strip()[:-1])
            current_top = top_name
            in_states = False
            current_alias_key = None
            continue

        if current_top in object_alias:
            if re.match(r"^\s{2}states:\s*$", line):
                in_states = True
                continue
            if in_states:
                item_match = re.match(r"^\s{4}-\s+(.+)$", line)
                if item_match:
                    token = normalize_token(item_match.group(1))
                    if token:
                        states_by_object[object_alias[current_top]].add(token)
                    continue
                if re.match(r"^\s{2}\S", line):
                    in_states = False

        if current_top == "aliases":
            key_match = re.match(r"^\s{2}([^:#]+):\s*$", line)
            if key_match:
                current_alias_key = normalize_token(key_match.group(1))
                if current_alias_key:
                    aliases.add(current_alias_key)
                continue
            value_match = re.match(r"^\s{4}-\s+(.+)$", line)
            if value_match and current_alias_key:
                token = normalize_token(value_match.group(1))
                if token:
                    aliases.add(token)

    return states_by_object, aliases


def extract_markdown_links(content):
    return [m.group(1).strip() for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", content)]


def resolve_local_link(path_str, source_file):
    target = path_str.strip()
    if not target or target.startswith("#"):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    target = unquote(target)

    # URLs externas nao entram no escopo deste doctor.
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return None

    target_path = Path(target)
    if target_path.is_absolute():
        return target_path
    return (source_file.parent / target_path).resolve()


POLICY_REGISTER_PATH = ROOT / "context" / "policy-register.json"
POLICY_CAMPOS_OBRIGATORIOS = [
    "id", "titulo", "dominio", "area_proprietaria", "versao",
    "data_aprovacao", "data_expiracao", "status", "aprovador",
    "frameworks", "processo_auditoria",
]
POLICY_STATUS_VALIDOS = {"vigente", "em_revisao", "expirada", "rascunho", "revogada"}
POLICY_ALERTA_DIAS = 90


def _parse_date(s: str):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return None


# --- Checks ---

def check_essential_files():
    results = []
    files = {
        "CLAUDE.md": "routing e instrucoes do agente",
        "domain.md": "vocabulario tecnico e frameworks",
        "DATA_CONTRACT.md": "fronteira user/system layer",
        "states.yml": "estados canonicos de engagement, area, achado e plano de acao",
        "README.md": "descricao do produto",
    }
    for f, desc in files.items():
        path = ROOT / f
        if path.exists():
            results.append(ok(f"{f} encontrado ({desc})"))
        else:
            results.append(fail(f"{f} ausente", f"Criar {f} — {desc}"))
    return results


def check_skills():
    results = []
    expected = [
        ("skills/client-context.md", "skill interna obrigatoria"),
        ("skills/process-flow-mermaid.md", "skill interna obrigatoria"),
        ("skills/audit-dashboard-visualization.md", "skill interna obrigatoria"),
        ("skills/operating-model-analysis.md", "skill interna obrigatoria"),
    ]
    if not (ROOT / "skills").exists():
        return [fail("skills/ ausente", "Criar pasta skills/")]
    for relative_path, _desc in expected:
        path = ROOT / relative_path
        if path.exists():
            results.append(ok(relative_path))
        else:
            results.append(fail(f"{relative_path} ausente", f"Criar {relative_path}"))
    return results


def check_workflows():
    results = []
    # Extrair workflows prometidos no CLAUDE.md
    claude_path = ROOT / "CLAUDE.md"
    if not claude_path.exists():
        return [fail("CLAUDE.md ausente — nao foi possivel verificar workflows", "Criar CLAUDE.md")]

    content = claude_path.read_text(encoding="utf-8")
    # Encontrar referencias a workflows/*.md no CLAUDE.md
    referenced = set(re.findall(r"`(workflows/[^`]+\.md)`", content))

    workflows_dir = ROOT / "workflows"
    if not workflows_dir.exists():
        return [fail("workflows/ ausente", "Criar pasta workflows/")]

    for wf_path in sorted(referenced):
        full_path = ROOT / wf_path
        if full_path.exists():
            results.append(ok(wf_path))
        else:
            results.append(fail(f"{wf_path} ausente (referenciado em CLAUDE.md)", f"Criar {wf_path}"))

    # Verificar workflows existentes nao referenciados (warning em modo normal; bloqueia em --strict)
    existing = {f"workflows/{p.name}" for p in workflows_dir.glob("*.md")}
    orphans = existing - referenced
    for orphan in sorted(orphans):
        results.append(warn(
            f"{orphan} existe, mas nao esta no CLAUDE.md",
            "Referenciar no Routing ou mover para archive se obsoleto"
        ))

    return results


def check_method_wiki():
    results = []
    wiki = ROOT / "_method-wiki"
    if not wiki.exists():
        return [fail("_method-wiki/ ausente", "Restaurar base metodologica")]

    required = {
        "_method-wiki/index.md": "indice da wiki",
        "_method-wiki/README.md": "documentacao da wiki",
    }
    for f, desc in required.items():
        path = ROOT / f
        if path.exists():
            results.append(ok(f"{f} ({desc})"))
        else:
            results.append(fail(f"{f} ausente", f"Criar {f}"))

    required_dirs = ["processes", "checklists", "concepts", "patterns", "heuristics"]
    for d in required_dirs:
        dir_path = wiki / d
        if not dir_path.exists():
            results.append(fail(f"_method-wiki/{d}/ ausente", f"Criar _method-wiki/{d}/"))
        else:
            files = list(dir_path.glob("*.md"))
            if files:
                results.append(ok(f"_method-wiki/{d}/ ({len(files)} arquivos)"))
            else:
                results.append(fail(f"_method-wiki/{d}/ vazia", f"Adicionar conteudo em _method-wiki/{d}/"))

    return results


def check_wcgw_master():
    results = []
    master_path = DEFAULT_WCGW_MASTER
    if not master_path.exists():
        return [fail(
            "context/wcgw-master.json ausente",
            "Gerar base com: python3 scripts/build_wcgw_master.py"
        )]

    try:
        items = get_wcgw_items(master_path)
    except Exception as exc:  # noqa: BLE001
        return [fail(
            f"context/wcgw-master.json inválido ({exc})",
            "Regenerar com: python3 scripts/build_wcgw_master.py"
        )]

    if not items:
        return [fail(
            "context/wcgw-master.json sem itens",
            "Regenerar base WCGW e validar parser"
        )]

    results.append(ok(f"context/wcgw-master.json carregado ({len(items)} itens)"))

    required_fields = [
        "id",
        "process_slug",
        "process_code",
        "subprocess_slug",
        "subprocess_name",
        "wcgw",
        "scot_phase",
        "assertion",
        "severity",
        "source_file",
    ]

    seen_ids = set()
    duplicate_ids = set()

    for idx, item in enumerate(items, start=1):
        for field in required_fields:
            if not item.get(field):
                results.append(fail(
                    f"WCGW item #{idx} sem campo obrigatório '{field}'",
                    "Regenerar base e revisar origem markdown"
                ))

        wcgw_id = item.get("id")
        if wcgw_id in seen_ids:
            duplicate_ids.add(wcgw_id)
        else:
            seen_ids.add(wcgw_id)

        phase = item.get("scot_phase")
        if phase and phase not in VALID_SCOT_PHASES:
            results.append(fail(
                f"{wcgw_id} com fase SCOT inválida: {phase}",
                f"Usar uma fase válida: {sorted(VALID_SCOT_PHASES)}"
            ))

        severity = item.get("severity")
        if severity and severity not in VALID_SEVERITIES:
            results.append(fail(
                f"{wcgw_id} com severidade inválida: {severity}",
                f"Usar severidade válida: {sorted(VALID_SEVERITIES)}"
            ))

        source_file = item.get("source_file")
        if source_file:
            source_path = ROOT / source_file
            if not source_path.exists():
                results.append(fail(
                    f"{wcgw_id} referencia source_file inexistente: {source_file}",
                    "Regenerar base ou corrigir referência de origem"
                ))

    if duplicate_ids:
        results.append(fail(
            f"IDs WCGW duplicados: {', '.join(sorted(duplicate_ids)[:10])}",
            "Garantir ID único por WCGW nos markdowns de origem"
        ))
    else:
        results.append(ok(f"IDs WCGW únicos ({len(seen_ids)})"))

    grouped = group_wcgw_by_process(items)
    for process_slug, process_items in sorted(grouped.items()):
        results.append(ok(f"WCGW por processo — {process_slug}: {len(process_items)} itens"))

    return results


def check_client_profiles():
    results = []
    clients_dir = ROOT / "context" / "clients"

    if not clients_dir.exists():
        results.append(ok("context/clients/ ausente (nenhum cliente perfilado ainda)"))
        return results

    client_slugs = [
        d for d in clients_dir.iterdir()
        if d.is_dir() and d.name != "_example"
    ]

    if not client_slugs:
        results.append(ok("context/clients/ existe (sem clientes ativos — apenas _example)"))
        return results

    for client_dir in sorted(client_slugs):
        slug = client_dir.name
        index_path = client_dir / "index.md"

        if not index_path.exists():
            results.append(fail(
                f"context/clients/{slug}/index.md ausente",
                f"Criar index.md para o cliente '{slug}' via skills/client-context.md"
            ))
            continue

        results.append(ok(f"context/clients/{slug}/index.md encontrado"))

        # Verificar arquivos referenciados no index.md
        index_content = index_path.read_text(encoding="utf-8")
        referenced_files = re.findall(r"\[.*?\]\(([^)]+\.md)\)", index_content)

        for ref in referenced_files:
            ref_path = client_dir / ref
            if ref_path.exists():
                results.append(ok(f"  context/clients/{slug}/{ref}"))
            else:
                results.append(fail(
                    f"  context/clients/{slug}/{ref} ausente (referenciado no index)",
                    f"Criar ou atualizar via skills/client-context.md modo update"
                ))

    return results


def check_example_profile():
    results = []
    example_dir = ROOT / "context" / "clients" / "_example"
    if not example_dir.exists():
        results.append(fail(
            "context/clients/_example/ ausente",
            "Criar pasta de exemplo via plano de implementacao"
        ))
        return results

    required = [
        "index.md", "profile.md", "org-structure.md", "people.md",
        "processes.md", "control-environment.md", "compliance.md",
        "goals-pressures.md", "risk-signals.md", "open-tasks.md",
    ]
    for f in required:
        path = example_dir / f
        if path.exists():
            results.append(ok(f"context/clients/_example/{f}"))
        else:
            results.append(fail(
                f"context/clients/_example/{f} ausente",
                "Recriar arquivo de exemplo"
            ))

    return results


def check_states():
    results = []
    states_path = ROOT / "states.yml"
    if not states_path.exists():
        return [fail("states.yml ausente", "Criar states.yml com estados canonicos")]

    content = states_path.read_text(encoding="utf-8")
    states_by_object, alias_tokens = parse_states_catalog(content)
    required_objects = ["engagement", "area", "achado", "plano_de_acao"]
    for obj in required_objects:
        if states_by_object.get(obj):
            results.append(ok(f"states.yml — objeto '{obj}' presente"))
        else:
            results.append(fail(
                f"states.yml — objeto '{obj}' ausente",
                f"Adicionar estados para '{obj}' em states.yml"
            ))

    clients_dir = ROOT / "context" / "clients"
    if not clients_dir.exists():
        return results

    universal_valid_tokens = set(alias_tokens)
    for obj_states in states_by_object.values():
        universal_valid_tokens.update(obj_states)

    object_line_re = re.compile(
        r"(?im)^\s*(?:\*\*)?"
        r"(engagement|area|área|achado|plano_de_acao|plano_de_ação|plano de acao|plano de ação)"
        r"(?:\*\*)?\s*:\s*([^\n]+)$"
    )
    status_line_re = re.compile(r"(?im)^\s*(?:\*\*)?status(?:\*\*)?\s*:\s*([^\n]+)$")

    object_name_map = {
        "engagement": "engagement",
        "area": "area",
        "área": "area",
        "achado": "achado",
        "plano_de_acao": "plano_de_acao",
        "plano_de_ação": "plano_de_acao",
        "plano de acao": "plano_de_acao",
        "plano de ação": "plano_de_acao",
    }

    for md_file in sorted(clients_dir.rglob("*.md")):
        file_content = md_file.read_text(encoding="utf-8")

        for match in object_line_re.finditer(file_content):
            object_raw, value_raw = match.group(1), match.group(2)
            if should_skip_state_candidate(value_raw):
                continue
            object_key = object_name_map.get(object_raw.lower())
            token = normalize_token(value_raw)
            valid_tokens = set(states_by_object.get(object_key, set())) | universal_valid_tokens
            if token and token not in valid_tokens:
                rel = md_file.relative_to(ROOT)
                results.append(fail(
                    f"{rel} — estado '{value_raw.strip()}' invalido para '{object_raw}'",
                    f"Usar estado canônico de states.yml para '{object_key}'"
                ))

        # Em /engagements/, um campo Status costuma representar estado de engagement.
        if "/engagements/" in md_file.as_posix():
            for status_match in status_line_re.finditer(file_content):
                value_raw = status_match.group(1)
                if should_skip_state_candidate(value_raw):
                    continue
                token = normalize_token(value_raw)
                valid_tokens = set(states_by_object.get("engagement", set())) | universal_valid_tokens
                if token and token not in valid_tokens:
                    rel = md_file.relative_to(ROOT)
                    results.append(fail(
                        f"{rel} — status '{value_raw.strip()}' invalido para engagement",
                        "Usar estado canônico de engagement em states.yml"
                    ))
    return results


def check_data_contract():
    results = []
    contract_path = ROOT / "DATA_CONTRACT.md"
    if not contract_path.exists():
        return [fail("DATA_CONTRACT.md ausente", "Criar DATA_CONTRACT.md")]

    content = contract_path.read_text(encoding="utf-8")
    required_sections = ["User Layer", "System Layer", "A Regra"]
    for section in required_sections:
        if section in content:
            results.append(ok(f"DATA_CONTRACT.md — secao '{section}' presente"))
        else:
            results.append(fail(
                f"DATA_CONTRACT.md — secao '{section}' ausente",
                f"Adicionar secao '{section}' ao DATA_CONTRACT.md"
            ))

    return results


def _check_single_wiki_index(wiki_dir: Path):
    results = []
    label = wiki_dir.name
    index_path = wiki_dir / "index.md"

    if not index_path.exists():
        return [fail(f"{label}/index.md ausente", f"Criar index.md em {label}/")]

    content = index_path.read_text(encoding="utf-8")
    links = extract_markdown_links(content)

    broken = []
    linked_files = set()
    for link in links:
        resolved = resolve_local_link(link, index_path)
        if resolved is None:
            continue
        linked_files.add(resolved)
        if not resolved.exists():
            broken.append(link)

    if broken:
        for link in broken:
            results.append(fail(
                f"{label}/index.md — link quebrado: {link}",
                "Corrigir caminho ou remover entrada do index"
            ))
    else:
        results.append(ok(f"{label}/index.md — todos os {len(linked_files)} links existem no disco"))

    indexed_dirs = ["concepts", "processes", "patterns", "checklists", "heuristics"]
    orphans = []
    for d in indexed_dirs:
        dir_path = wiki_dir / d
        if not dir_path.exists():
            continue
        for md in sorted(dir_path.glob("*.md")):
            if md.resolve() not in linked_files:
                orphans.append(md.relative_to(wiki_dir))

    if orphans:
        for orphan in orphans:
            results.append(warn(
                f"{label}/{orphan} existe mas não está no index.md",
                "Adicionar entrada no index ou mover para archive se obsoleto"
            ))
    else:
        results.append(ok(f"{label} — todos os MDs das pastas indexadas estão no index.md"))

    return results


def check_method_wiki_index():
    results = []
    for wiki_name in ["_method-wiki"]:
        wiki_dir = ROOT / wiki_name
        if not wiki_dir.exists():
            results.append(warn(
                f"{wiki_name}/ não encontrado",
                f"Criar {wiki_name}/ se aplicável ao produto"
            ))
            continue
        results.extend(_check_single_wiki_index(wiki_dir))
    return results


def check_broken_links(include_docs=False):
    results = []
    files_to_check = [
        ROOT / "README.md",
        ROOT / "CLAUDE.md",
        ROOT / "_method-wiki" / "index.md",
    ]

    clients_root = ROOT / "context" / "clients"
    if clients_root.exists():
        files_to_check.extend(sorted(clients_root.glob("*/index.md")))

    if include_docs:
        docs_roots = []
        current_docs_root = ROOT / "docs"
        archived_docs_root = ROOT / "archive" / "docs"

        if current_docs_root.exists():
            docs_roots.append(current_docs_root)
        if archived_docs_root.exists():
            docs_roots.append(archived_docs_root)

        if docs_roots:
            for docs_root in docs_roots:
                files_to_check.extend(sorted(docs_root.rglob("*.md")))
            results.append(ok("docs/ ou archive/docs/ incluidos na validacao de links (--include-docs)"))
        else:
            results.append(ok("docs/ e archive/docs/ nao encontrados; nada para validar"))
    else:
        results.append(ok("docs/ e archive/docs/ ignorados por padrao (usar --include-docs para validar)"))

    for file_path in files_to_check:
        if not file_path.exists():
            results.append(fail(f"{file_path.relative_to(ROOT)} ausente", "Restaurar arquivo"))
            continue

        content = file_path.read_text(encoding="utf-8")
        links = extract_markdown_links(content)
        broken = []

        for link in links:
            local_target = resolve_local_link(link, file_path)
            if local_target is None:
                continue
            if not local_target.exists():
                broken.append(link)

        rel_file = file_path.relative_to(ROOT)
        if broken:
            for link in broken:
                results.append(fail(
                    f"{rel_file} — link quebrado: {link}",
                    "Corrigir caminho ou remover referencia"
                ))
        else:
            results.append(ok(f"{rel_file} — links locais validos ({len(links)})"))

    return results


def check_claude_consistency():
    results = []
    claude_path = ROOT / "CLAUDE.md"
    if not claude_path.exists():
        return [fail("CLAUDE.md ausente — sem como validar consistencia", "Criar CLAUDE.md")]

    content = claude_path.read_text(encoding="utf-8")

    referenced_workflows = set(re.findall(r"`(workflows/[^`]+\.md)`", content))
    referenced_skills = set(re.findall(r"`(skills/[^`]+\.md)`", content))
    referenced_wcgw = set(re.findall(r"`(context/wcgw/[^`]+\.md)`", content))

    for ref in sorted(referenced_workflows | referenced_skills | referenced_wcgw):
        if (ROOT / ref).exists():
            results.append(ok(f"{ref} referenciado e existente"))
        else:
            results.append(fail(
                f"{ref} referenciado no CLAUDE.md, mas ausente",
                f"Criar {ref} ou remover referencia do CLAUDE.md"
            ))

    existing_workflows = {f"workflows/{p.name}" for p in (ROOT / "workflows").glob("*.md")}
    existing_skills = {f"skills/{p.name}" for p in (ROOT / "skills").glob("*.md")}
    existing_wcgw = {f"context/wcgw/{p.name}" for p in (ROOT / "context" / "wcgw").glob("*.md")}

    for orphan in sorted(existing_workflows - referenced_workflows):
        results.append(warn(
            f"{orphan} existe, mas nao esta no CLAUDE.md",
            "Referenciar no Routing ou mover para archive se obsoleto"
        ))
    for orphan in sorted(existing_skills - referenced_skills):
        results.append(warn(
            f"{orphan} existe, mas nao esta no CLAUDE.md",
            "Referenciar em Skills Auxiliares ou mover para archive se obsoleto"
        ))
    for orphan in sorted(existing_wcgw - referenced_wcgw):
        results.append(warn(
            f"{orphan} existe, mas nao esta no CLAUDE.md",
            "Referenciar na Biblioteca de WCGW ou mover para archive se obsoleto"
        ))

    return results


def check_policy_register():
    results = []
    hoje = date.today()

    if not POLICY_REGISTER_PATH.exists():
        return [fail(
            "context/policy-register.json ausente",
            "Criar registro com: context/policy-register.json (ver templates/politica-exemplo.json)"
        )]

    try:
        data = json.loads(POLICY_REGISTER_PATH.read_text(encoding="utf-8"))
        policies = data.get("policies", [])
    except Exception as exc:
        return [fail(f"context/policy-register.json inválido ({exc})", "Verificar JSON de políticas")]

    results.append(ok(f"context/policy-register.json carregado ({len(policies)} políticas)"))

    # Integridade
    ids_vistos: set = set()
    erros_integridade = 0
    for p in policies:
        pid = p.get("id", "?")
        if pid in ids_vistos:
            results.append(fail(f"Política ID duplicado: {pid}", "Garantir IDs únicos no policy-register.json"))
            erros_integridade += 1
        ids_vistos.add(pid)
        for campo in POLICY_CAMPOS_OBRIGATORIOS:
            if not p.get(campo):
                results.append(fail(
                    f"[{pid}] campo obrigatório ausente: '{campo}'",
                    "Preencher campo no context/policy-register.json"
                ))
                erros_integridade += 1
        if p.get("status") not in POLICY_STATUS_VALIDOS:
            results.append(fail(
                f"[{pid}] status inválido: '{p.get('status')}'",
                f"Usar um de: {sorted(POLICY_STATUS_VALIDOS)}"
            ))
            erros_integridade += 1

    if erros_integridade == 0:
        results.append(ok(f"Integridade do registro: ok ({len(ids_vistos)} IDs únicos)"))

    # Expiradas (status explícito ou data passada com status vigente/em_revisao)
    expiradas = []
    for p in policies:
        status = p.get("status", "")
        exp = _parse_date(p.get("data_expiracao", ""))
        if status == "expirada":
            expiradas.append(p)
        elif status in ("vigente", "em_revisao") and exp and exp < hoje:
            expiradas.append(p)

    for p in expiradas:
        results.append(warn(
            f"Política expirada: [{p['id']}] {p['titulo']} (expiração: {p.get('data_expiracao','—')})",
            f"Revisar e atualizar — área responsável: {p.get('area_proprietaria','?')}"
        ))

    # Alerta de expiração próxima
    alertas = []
    for p in policies:
        if p.get("status") not in ("vigente", "em_revisao"):
            continue
        exp = _parse_date(p.get("data_expiracao", ""))
        if exp and 0 <= (exp - hoje).days <= POLICY_ALERTA_DIAS:
            alertas.append((exp, p))
    alertas.sort(key=lambda x: x[0])

    for exp, p in alertas:
        dias_rest = (exp - hoje).days
        results.append(warn(
            f"Política expira em {dias_rest} dias: [{p['id']}] {p['titulo']} ({exp})",
            f"Iniciar revisão — área responsável: {p.get('area_proprietaria','?')}"
        ))

    if not expiradas and not alertas:
        results.append(ok(f"Nenhuma política expirada ou expirando em {POLICY_ALERTA_DIAS} dias"))

    return results


# --- Runner ---

def run_section(title, checks_fn, strict=False):
    print(f"\n{title}")
    print("-" * len(title))
    results = checks_fn()
    summary = {"title": title, "ok": 0, "warnings": 0, "errors": 0, "blocking": 0}

    for r in results:
        level = r.get("level", "ok" if r.get("pass") else "error")
        if level == "ok":
            summary["ok"] += 1
            print(f"  {GREEN}✓{RESET} {r['label']}")
            continue

        if level == "warning":
            summary["warnings"] += 1
            if strict:
                summary["blocking"] += 1
            print(f"  {YELLOW}!{RESET} {r['label']}")
            for hint in r.get("fix", []):
                print(f"    {DIM}→ {hint}{RESET}")
            continue

        summary["errors"] += 1
        summary["blocking"] += 1
        if not r["pass"]:
            print(f"  {RED}✗{RESET} {r['label']}")
            for hint in r.get("fix", []):
                print(f"    {DIM}→ {hint}{RESET}")

    return summary


def main():
    print("\ninternal-audit-ops doctor")
    print("=========================")

    include_docs = "--include-docs" in sys.argv
    strict = "--strict" in sys.argv
    report = "--report" in sys.argv

    summaries = []
    summaries.append(run_section("Arquivos Essenciais", check_essential_files, strict=strict))
    summaries.append(run_section("Skills", check_skills, strict=strict))
    summaries.append(run_section("Workflows", check_workflows, strict=strict))
    summaries.append(run_section("Method Wiki", check_method_wiki, strict=strict))
    summaries.append(run_section("Method Wiki Index", check_method_wiki_index, strict=strict))
    summaries.append(run_section("WCGW Master", check_wcgw_master, strict=strict))
    summaries.append(run_section("States", check_states, strict=strict))
    summaries.append(run_section("Data Contract", check_data_contract, strict=strict))
    summaries.append(run_section("Links", lambda: check_broken_links(include_docs=include_docs), strict=strict))
    summaries.append(run_section("Consistencia do CLAUDE", check_claude_consistency, strict=strict))
    summaries.append(run_section("Perfil de Exemplo", check_example_profile, strict=strict))
    summaries.append(run_section("Perfis de Clientes", check_client_profiles, strict=strict))
    summaries.append(run_section("Registro de Políticas", check_policy_register, strict=strict))

    total_errors = sum(s["errors"] for s in summaries)
    total_warnings = sum(s["warnings"] for s in summaries)
    total_blocking = sum(s["blocking"] for s in summaries)

    if report:
        print("\nResumo")
        print("------")
        for s in summaries:
            print(f"  - {s['title']}: ok={s['ok']} warn={s['warnings']} err={s['errors']}")
        print(f"  Total: ok={sum(s['ok'] for s in summaries)} warn={total_warnings} err={total_errors}")
        if strict:
            print("  Modo: strict (warnings contam como bloqueio)")

    print()
    if total_blocking > 0:
        if strict and total_errors == 0 and total_warnings > 0:
            print(f"{YELLOW}! {total_warnings} warning(s) em modo strict.{RESET} Corrija e rode novamente:")
        else:
            print(f"{RED}✗ {total_blocking} problema(s) bloqueante(s) encontrado(s).{RESET} Corrija e rode novamente:")
        print(f"  python scripts/doctor.py")
        sys.exit(1)
    else:
        if total_warnings > 0:
            print(f"{YELLOW}! {total_warnings} warning(s) encontrado(s).{RESET} Nao bloqueante no modo padrao.")
        print(f"{GREEN}✓ Tudo ok.{RESET} internal-audit-ops pronto para uso.")
        sys.exit(0)


if __name__ == "__main__":
    main()
