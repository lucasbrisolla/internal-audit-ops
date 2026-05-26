"""
policy_register.py — Consulta, valida e reporta o registro de políticas corporativas.

Comandos:
    python3 scripts/policy_register.py status          # resumo por status
    python3 scripts/policy_register.py expiradas       # políticas expiradas
    python3 scripts/policy_register.py alerta [dias]   # expirando em N dias (default 90)
    python3 scripts/policy_register.py gap <framework> # domínios sem política para o framework
    python3 scripts/policy_register.py processo <cod>  # políticas por processo de auditoria
    python3 scripts/policy_register.py validar         # valida integridade do registro
    python3 scripts/policy_register.py checar <arq>    # checklist de conformidade de um JSON de política
"""

import json
import sys
from datetime import date, datetime
from pathlib import Path

REGISTER_PATH = Path(__file__).parent.parent / "context" / "policy-register.json"
CAMPOS_OBRIGATORIOS = ["id", "titulo", "dominio", "area_proprietaria", "versao",
                       "data_aprovacao", "data_expiracao", "status", "aprovador",
                       "frameworks", "processo_auditoria"]
STATUS_VALIDOS = {"vigente", "em_revisao", "expirada", "rascunho", "revogada"}


def load() -> dict:
    with open(REGISTER_PATH, encoding="utf-8") as f:
        return json.load(f)


def parse_date(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return None


def cor_status(status: str) -> str:
    return {
        "vigente":    "✅",
        "em_revisao": "🔄",
        "expirada":   "❌",
        "rascunho":   "📝",
        "revogada":   "⛔",
    }.get(status, "❓")


# ── Comandos ──────────────────────────────────────────────────────────────────

def cmd_status(policies: list):
    from collections import Counter
    contagem = Counter(p["status"] for p in policies)
    print(f"\n{'='*50}")
    print(f"  REGISTRO DE POLÍTICAS — {date.today()}")
    print(f"  Total: {len(policies)} políticas")
    print(f"{'='*50}")
    for status, n in sorted(contagem.items()):
        print(f"  {cor_status(status)}  {status:<15} {n:>3}")
    print()


def cmd_expiradas(policies: list):
    hoje = date.today()
    expiradas = [p for p in policies
                 if p["status"] == "expirada" or
                 (p["status"] == "vigente" and parse_date(p.get("data_expiracao", "")) and
                  parse_date(p["data_expiracao"]) < hoje)]
    if not expiradas:
        print("\nNenhuma política expirada.\n")
        return
    print(f"\n{'='*60}")
    print(f"  POLÍTICAS EXPIRADAS ({len(expiradas)})")
    print(f"{'='*60}")
    for p in expiradas:
        exp = p.get("data_expiracao", "—")
        print(f"  ❌  [{p['id']}] {p['titulo']}")
        print(f"       Expiração: {exp} | Área: {p['area_proprietaria']}")
        if p.get("notas"):
            print(f"       Nota: {p['notas']}")
    print()


def cmd_alerta(policies: list, dias: int = 90):
    hoje = date.today()
    alertas = []
    for p in policies:
        if p["status"] not in ("vigente", "em_revisao"):
            continue
        exp = parse_date(p.get("data_expiracao", ""))
        if exp and 0 <= (exp - hoje).days <= dias:
            alertas.append((exp, p))
    alertas.sort(key=lambda x: x[0])
    if not alertas:
        print(f"\nNenhuma política expira nos próximos {dias} dias.\n")
        return
    print(f"\n{'='*60}")
    print(f"  ALERTA — expirando em até {dias} dias ({len(alertas)})")
    print(f"{'='*60}")
    for exp, p in alertas:
        dias_rest = (exp - hoje).days
        print(f"  ⚠️   [{p['id']}] {p['titulo']}")
        print(f"       Expira em: {exp} ({dias_rest} dias) | {p['area_proprietaria']}")
    print()


def cmd_gap(policies: list, framework: str):
    framework_upper = framework.upper()
    com_framework = {p["dominio"] for p in policies
                     if framework_upper in [f.upper() for f in p.get("frameworks", [])]}
    todos_dominios = {p["dominio"] for p in policies}
    sem = todos_dominios - com_framework
    print(f"\n{'='*60}")
    print(f"  GAP ANALYSIS — framework: {framework_upper}")
    print(f"{'='*60}")
    print(f"  Domínios com cobertura ({len(com_framework)}):")
    for d in sorted(com_framework):
        print(f"    ✅  {d}")
    if sem:
        print(f"\n  Domínios SEM política para {framework_upper} ({len(sem)}):")
        for d in sorted(sem):
            print(f"    ❌  {d}")
    else:
        print(f"\n  Todos os domínios cobertos para {framework_upper}.")
    print()


def cmd_processo(policies: list, codigo: str):
    codigo_upper = codigo.upper()
    encontradas = [p for p in policies
                   if codigo_upper in [c.upper() for c in p.get("processo_auditoria", [])]]
    print(f"\n{'='*60}")
    print(f"  POLÍTICAS — processo de auditoria: {codigo_upper} ({len(encontradas)})")
    print(f"{'='*60}")
    if not encontradas:
        print("  Nenhuma política mapeada para este processo.")
    for p in encontradas:
        print(f"  {cor_status(p['status'])}  [{p['id']}] {p['titulo']}")
        print(f"       Versão: {p['versao']} | Expira: {p.get('data_expiracao','—')} | {p['area_proprietaria']}")
    print()


def cmd_validar(policies: list):
    erros = []
    ids_vistos = set()
    for i, p in enumerate(policies):
        pid = p.get("id", f"[índice {i}]")
        if pid in ids_vistos:
            erros.append(f"{pid}: ID duplicado")
        ids_vistos.add(pid)
        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in p or p[campo] is None or p[campo] == "":
                erros.append(f"{pid}: campo obrigatório ausente — '{campo}'")
        if p.get("status") not in STATUS_VALIDOS:
            erros.append(f"{pid}: status inválido — '{p.get('status')}'")
        for campo_data in ("data_aprovacao", "data_expiracao"):
            if p.get(campo_data) and not parse_date(p[campo_data]):
                erros.append(f"{pid}: data inválida em '{campo_data}' — '{p[campo_data]}'")

    print(f"\n{'='*50}")
    print(f"  VALIDAÇÃO DO REGISTRO")
    print(f"  {len(policies)} políticas verificadas")
    print(f"{'='*50}")
    if erros:
        print(f"  ❌  {len(erros)} erro(s) encontrado(s):")
        for e in erros:
            print(f"       • {e}")
    else:
        print("  ✅  Registro íntegro — nenhum erro encontrado.")
    print()


def cmd_checar(arquivo: str):
    """Checklist de conformidade de um JSON de política individual."""
    path = Path(arquivo)
    if not path.exists():
        print(f"\nArquivo não encontrado: {arquivo}\n")
        return

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"\nJSON inválido: {exc}\n")
        return

    ok_items = []
    warn_items = []
    fail_items = []

    def chk(cond: bool, label: str, critico: bool = True):
        if cond:
            ok_items.append(label)
        elif critico:
            fail_items.append(label)
        else:
            warn_items.append(label)

    empresa  = data.get("empresa", {})
    meta     = data.get("metadados", {})
    conteudo = data.get("conteudo", {})

    # ── Empresa ──
    chk(bool(empresa.get("nome", "").strip()),         "empresa.nome preenchido")
    chk(bool(empresa.get("elaborado_por", "").strip()), "empresa.elaborado_por preenchido", critico=False)

    # ── Metadados obrigatórios ──
    chk(bool(meta.get("titulo_politica", "").strip()),  "metadados.titulo_politica preenchido")
    chk(bool(meta.get("codigo", "").strip()),           "metadados.codigo preenchido")
    chk(bool(meta.get("versao", "").strip()),           "metadados.versao preenchido")
    chk(bool(meta.get("data_vigencia", "").strip()),    "metadados.data_vigencia preenchido")
    chk(bool(meta.get("area_proprietaria", "").strip()),"metadados.area_proprietaria preenchido")
    chk(bool(meta.get("aprovador", "").strip()),        "metadados.aprovador preenchido")
    chk(bool(meta.get("periodicidade_revisao", "").strip()), "metadados.periodicidade_revisao preenchido", critico=False)

    # ── Histórico de revisões ──
    historico = meta.get("historico_revisoes", [])
    chk(len(historico) >= 1, "histórico de revisões com pelo menos 1 entrada")
    if historico:
        h0 = historico[0]
        chk(bool(h0.get("versao") and h0.get("data") and h0.get("aprovador")),
            "primeira entrada do histórico com versão, data e aprovador")

    # ── Conteúdo obrigatório ──
    chk(bool(conteudo.get("objetivo", "").strip()),     "conteudo.objetivo preenchido")

    escopo = conteudo.get("escopo", {})
    chk(bool(escopo.get("aplicavel_a", "").strip()),    "conteudo.escopo.aplicavel_a preenchido")

    definicoes = conteudo.get("definicoes", [])
    chk(len(definicoes) >= 1, "conteudo.definicoes com pelo menos 1 termo")
    if definicoes:
        chk(all(d.get("termo") and d.get("definicao") for d in definicoes),
            "todas as definições com termo e definicao preenchidos", critico=False)

    diretrizes = conteudo.get("diretrizes", [])
    chk(len(diretrizes) >= 1, "conteudo.diretrizes com pelo menos 1 seção")

    responsabilidades = conteudo.get("responsabilidades", [])
    chk(len(responsabilidades) >= 1, "conteudo.responsabilidades com pelo menos 1 papel")
    if responsabilidades:
        chk(all(r.get("papel") and r.get("responsabilidade") for r in responsabilidades),
            "todos os papéis com papel e responsabilidade preenchidos", critico=False)

    chk(bool(conteudo.get("vigencia", "").strip()),     "conteudo.vigencia preenchido")

    # ── Qualidade mínima ──
    chk(bool(conteudo.get("referencias", [])),          "conteudo.referencias com pelo menos 1 item", critico=False)
    chk(bool(conteudo.get("penalidades", "").strip()),  "conteudo.penalidades preenchido", critico=False)

    # ── Data válida ──
    dv = meta.get("data_vigencia", "")
    if dv:
        chk(bool(parse_date(dv)), f"data_vigencia em formato válido (YYYY-MM-DD): '{dv}'")

    # ── Relatório ──
    total = len(ok_items) + len(warn_items) + len(fail_items)
    titulo = meta.get("titulo_politica") or path.name
    print(f"\n{'='*60}")
    print(f"  CHECKLIST DE CONFORMIDADE — {titulo}")
    print(f"  Arquivo: {path}")
    print(f"{'='*60}")
    for item in ok_items:
        print(f"  ✅  {item}")
    for item in warn_items:
        print(f"  ⚠️   {item}")
    for item in fail_items:
        print(f"  ❌  {item}")
    print(f"\n  Resultado: {len(ok_items)}/{total} ok  |  {len(warn_items)} avisos  |  {len(fail_items)} falhas críticas")
    if not fail_items:
        print("  ✅  Política em conformidade com estrutura mínima obrigatória.")
    else:
        print("  ❌  Preencher campos críticos antes de exportar o .docx.")
    print()


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    data = load()
    policies = data.get("policies", [])

    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"

    if cmd == "status":
        cmd_status(policies)
    elif cmd == "expiradas":
        cmd_expiradas(policies)
    elif cmd == "alerta":
        dias = int(sys.argv[2]) if len(sys.argv) > 2 else 90
        cmd_alerta(policies, dias)
    elif cmd == "gap":
        if len(sys.argv) < 3:
            print("Uso: policy_register.py gap <framework>  (ex: COSO, SOX, ISO27001, LGPD)")
            sys.exit(1)
        cmd_gap(policies, sys.argv[2])
    elif cmd == "processo":
        if len(sys.argv) < 3:
            print("Uso: policy_register.py processo <código>  (ex: P2P, ITGC, LCT)")
            sys.exit(1)
        cmd_processo(policies, sys.argv[2])
    elif cmd == "validar":
        cmd_validar(policies)
    elif cmd == "checar":
        if len(sys.argv) < 3:
            print("Uso: policy_register.py checar <arquivo.json>")
            sys.exit(1)
        cmd_checar(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
