#!/usr/bin/env python3
"""
build_wcgw_master.py — Converte context/wcgw/*.md em base estruturada JSON.

Saída padrão:
    context/wcgw-master.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = ROOT / "context" / "wcgw"
DEFAULT_OUTPUT = ROOT / "context" / "wcgw-master.json"

TABLE_HEADER_RE = re.compile(
    r"^\|\s*ID\s*\|\s*WCGW\s*\|\s*Fase SCOT\s*\|\s*Asserção\s*\|\s*Severidade\s*\|",
    re.IGNORECASE,
)
SUBPROCESS_RE = re.compile(r"^##\s+Subprocesso\s+\d+\s*:\s*(.+?)\s*$", re.IGNORECASE)


def _slugify(value: str) -> str:
    lowered = value.strip().lower()
    lowered = (
        lowered.replace("ç", "c")
        .replace("ã", "a")
        .replace("á", "a")
        .replace("à", "a")
        .replace("â", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ü", "u")
    )
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-+", "-", lowered).strip("-")
    return lowered


def _parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    lines = text.splitlines()
    front_lines = []
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
        front_lines.append(line.rstrip("\n"))
    else:
        return {}

    frontmatter = {}
    current_key = None
    list_acc = None
    for raw in front_lines:
        if not raw.strip():
            continue
        if raw.startswith("  - ") and current_key and list_acc is not None:
            list_acc.append(raw[4:].strip())
            continue
        if ":" in raw:
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                current_key = key
                list_acc = []
                frontmatter[key] = list_acc
            else:
                current_key = key
                list_acc = None
                frontmatter[key] = value
    return frontmatter


def _split_row(row_line: str) -> list[str]:
    raw = row_line.strip()
    if not raw.startswith("|") or not raw.endswith("|"):
        return []
    cells = [c.strip() for c in raw.split("|")[1:-1]]
    return cells


def parse_wcgw_file(path: Path) -> list[dict]:
    content = path.read_text(encoding="utf-8")
    front = _parse_frontmatter(content)

    process_slug = front.get("processo", path.stem)
    process_code = front.get("abreviacao", process_slug.upper())
    frameworks = front.get("frameworks", [])
    references = front.get("referencias", [])

    entries: list[dict] = []
    current_subprocess = None
    current_subprocess_slug = None
    in_table = False

    for line in content.splitlines():
        subprocess_match = SUBPROCESS_RE.match(line.strip())
        if subprocess_match:
            current_subprocess = subprocess_match.group(1).strip()
            current_subprocess_slug = _slugify(current_subprocess)
            in_table = False
            continue

        if TABLE_HEADER_RE.match(line.strip()):
            in_table = True
            continue

        if in_table and re.match(r"^\|\s*[-: ]+\|\s*[-: ]+\|", line.strip()):
            continue

        if in_table and line.strip().startswith("|"):
            cells = _split_row(line)
            if len(cells) < 5:
                continue
            SEVERITY_MAP = {"Alta": "Alto", "Média": "Moderado", "Baixa": "Baixo"}

            wcgw_id, wcgw_text, scot_phase, assertion, severity = cells[:5]
            if not wcgw_id or wcgw_id.upper() == "ID":
                continue

            sev_raw = severity.strip()
            sev_norm = SEVERITY_MAP.get(sev_raw, sev_raw)

            entries.append(
                {
                    "id": wcgw_id.strip(),
                    "process_slug": process_slug,
                    "process_code": process_code,
                    "subprocess_slug": current_subprocess_slug,
                    "subprocess_name": current_subprocess,
                    "wcgw": wcgw_text.strip(),
                    "scot_phase": scot_phase.strip(),
                    "assertion": assertion.strip(),
                    "severity": sev_norm,
                    "frameworks": frameworks,
                    "source_file": str(path.relative_to(ROOT)),
                    "source_references": references,
                }
            )
            continue

        if in_table and line.strip() and not line.strip().startswith("|"):
            in_table = False

    return entries


def build_master(source_dir: Path) -> dict:
    files = sorted(source_dir.glob("*.md"))
    all_entries = []
    for wcgw_file in files:
        all_entries.extend(parse_wcgw_file(wcgw_file))

    return {
        "metadata": {
            "schema_version": "1.0.0",
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_dir": str(source_dir.relative_to(ROOT)),
            "total_process_files": len(files),
            "total_wcgw_items": len(all_entries),
        },
        "items": all_entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera context/wcgw-master.json a partir de context/wcgw/*.md")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.source_dir.exists():
        raise FileNotFoundError(f"Diretório de origem não encontrado: {args.source_dir}")

    master = build_master(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(master, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Arquivo gerado: {args.output}")
    print(f"Processos lidos: {master['metadata']['total_process_files']}")
    print(f"WCGWs extraídos: {master['metadata']['total_wcgw_items']}")


if __name__ == "__main__":
    main()

