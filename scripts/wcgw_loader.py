"""
wcgw_loader.py — Loader único para base estruturada WCGW.
"""

from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WCGW_MASTER = ROOT / "context" / "wcgw-master.json"
DEFAULT_MASTER_LISTS_DIR = ROOT / "context" / "master-lists"

VALID_SCOT_PHASES = {"Initiation", "Recording", "Processing", "Reporting"}
VALID_SEVERITIES = {"Baixo", "Moderado", "Alto", "Crítico"}


def load_wcgw_master(path: Path | None = None) -> dict:
    target = path or DEFAULT_WCGW_MASTER
    if not target.exists():
        raise FileNotFoundError(f"Base WCGW não encontrada: {target}")
    return json.loads(target.read_text(encoding="utf-8"))


def get_wcgw_items(path: Path | None = None) -> list[dict]:
    master = load_wcgw_master(path)
    return master.get("items", [])


def index_wcgw_by_id(items: list[dict]) -> dict[str, dict]:
    return {item["id"]: item for item in items if "id" in item}


def group_wcgw_by_process(items: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    for item in items:
        grouped[item.get("process_slug", "unknown")].append(item)
    return dict(grouped)


def load_master_lists(master_lists_dir: Path | None = None) -> dict[str, dict]:
    """
    Carrega master lists em Markdown para consumo único pelos scripts.
    Retorna:
      {
        "<slug>": {
          "path": "...",
          "content": "...",
        }
      }
    """
    base = master_lists_dir or DEFAULT_MASTER_LISTS_DIR
    if not base.exists():
        raise FileNotFoundError(f"Pasta de master lists não encontrada: {base}")

    loaded = {}
    for md in sorted(base.glob("*.md")):
        loaded[md.stem] = {
            "path": str(md),
            "content": md.read_text(encoding="utf-8"),
        }
    return loaded
