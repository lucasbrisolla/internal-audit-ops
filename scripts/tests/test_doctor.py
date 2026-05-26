from pathlib import Path
import importlib.util
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_doctor_module():
    doctor_path = PROJECT_ROOT / "scripts" / "doctor.py"
    spec = importlib.util.spec_from_file_location("doctor", doctor_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_parse_states_catalog_extracts_states_and_aliases():
    doctor = load_doctor_module()
    content = """
engagement:
  states:
    - planejamento
    - execução
área:
  states:
    - não_iniciado
achado:
  states:
    - rascunho
plano_de_ação:
  states:
    - aberto
aliases:
  não_iniciado:
    - nao_iniciado
"""

    states, aliases = doctor.parse_states_catalog(content)

    assert states["engagement"] == {"planejamento", "execucao"}
    assert states["area"] == {"nao_iniciado"}
    assert states["achado"] == {"rascunho"}
    assert states["plano_de_acao"] == {"aberto"}
    assert "nao_iniciado" in aliases


def test_check_states_flags_invalid_status_in_engagement_file(tmp_path, monkeypatch):
    doctor = load_doctor_module()
    monkeypatch.setattr(doctor, "ROOT", tmp_path)

    write(
        tmp_path / "states.yml",
        """
engagement:
  states:
    - planejamento
área:
  states:
    - não_iniciado
achado:
  states:
    - rascunho
plano_de_ação:
  states:
    - aberto
aliases:
  planejamento:
    - plan
""".strip()
        + "\n",
    )
    write(
        tmp_path / "context/clients/acme/engagements/2026-q2.md",
        """
**Status:** desconhecido
""".strip()
        + "\n",
    )

    results = doctor.check_states()
    failures = [r for r in results if not r["pass"]]

    assert any("status 'desconhecido' invalido para engagement" in r["label"] for r in failures)


def test_check_broken_links_detects_missing_links_and_ignores_docs_by_default(tmp_path, monkeypatch):
    doctor = load_doctor_module()
    monkeypatch.setattr(doctor, "ROOT", tmp_path)

    write(tmp_path / "README.md", "[ok](CLAUDE.md)\n")
    write(tmp_path / "CLAUDE.md", "sem links\n")
    write(tmp_path / "_method-wiki/index.md", "[quebrado](missing.md)\n")
    write(tmp_path / "context/clients/_example/index.md", "[ok](../_example/index.md)\n")
    write(tmp_path / "docs/specs/x.md", "[quebrado](nao-existe.md)\n")

    results = doctor.check_broken_links(include_docs=False)
    failures = [r for r in results if not r["pass"]]
    oks = [r for r in results if r["pass"]]

    assert any("docs/ e archive/docs/ ignorados por padrao" in r["label"] for r in oks)
    assert any("_method-wiki/index.md — link quebrado: missing.md" in r["label"] for r in failures)
    assert not any("docs/specs/x.md" in r["label"] for r in failures)


def test_check_broken_links_include_docs_validates_docs_folder(tmp_path, monkeypatch):
    doctor = load_doctor_module()
    monkeypatch.setattr(doctor, "ROOT", tmp_path)

    write(tmp_path / "README.md", "ok\n")
    write(tmp_path / "CLAUDE.md", "ok\n")
    write(tmp_path / "_method-wiki/index.md", "ok\n")
    write(tmp_path / "context/clients/_example/index.md", "ok\n")
    write(tmp_path / "docs/specs/x.md", "[quebrado](nao-existe.md)\n")

    results = doctor.check_broken_links(include_docs=True)
    failures = [r for r in results if not r["pass"]]

    assert any("docs/specs/x.md — link quebrado: nao-existe.md" in r["label"] for r in failures)


def test_check_broken_links_include_docs_validates_archive_docs_folder(tmp_path, monkeypatch):
    doctor = load_doctor_module()
    monkeypatch.setattr(doctor, "ROOT", tmp_path)

    write(tmp_path / "README.md", "ok\n")
    write(tmp_path / "CLAUDE.md", "ok\n")
    write(tmp_path / "_method-wiki/index.md", "ok\n")
    write(tmp_path / "context/clients/_example/index.md", "ok\n")
    write(tmp_path / "archive/docs/specs/x.md", "[quebrado](nao-existe.md)\n")

    results = doctor.check_broken_links(include_docs=True)
    failures = [r for r in results if not r["pass"]]

    assert any("archive/docs/specs/x.md — link quebrado: nao-existe.md" in r["label"] for r in failures)


def test_check_claude_consistency_detects_missing_refs_and_orphans(tmp_path, monkeypatch):
    doctor = load_doctor_module()
    monkeypatch.setattr(doctor, "ROOT", tmp_path)

    write(
        tmp_path / "CLAUDE.md",
        """
| Teste | `workflows/existente.md` |
| Skill | `skills/inexistente.md` |
| WCGW | `context/wcgw/otc.md` |
""".strip()
        + "\n",
    )
    write(tmp_path / "workflows/existente.md", "# ok\n")
    write(tmp_path / "workflows/orfao.md", "# orfao\n")
    write(tmp_path / "skills/outra.md", "# orfa\n")
    write(tmp_path / "context/wcgw/otc.md", "# ok\n")
    write(tmp_path / "context/wcgw/orfao.md", "# orfao\n")

    results = doctor.check_claude_consistency()
    failures = [r for r in results if not r["pass"]]
    warnings = [r for r in results if r.get("level") == "warning"]

    assert any("skills/inexistente.md referenciado no CLAUDE.md, mas ausente" in r["label"] for r in failures)
    assert any("workflows/orfao.md existe, mas nao esta no CLAUDE.md" in r["label"] for r in warnings)
    assert any("skills/outra.md existe, mas nao esta no CLAUDE.md" in r["label"] for r in warnings)
    assert any("context/wcgw/orfao.md existe, mas nao esta no CLAUDE.md" in r["label"] for r in warnings)
