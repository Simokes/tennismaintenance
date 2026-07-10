#!/usr/bin/env python3
"""Vérifie que chaque lien « document source » cité dans docs/ existe.

Contrôle CI de l'architecture Option 3 (cf. issue #34) : une page publiée
(`docs/`) peut renvoyer vers son document de référence à la racine via un lien
GitHub `…/blob/<branche>/<chemin>`. Ce script échoue (exit 1) si l'un de ces
`<chemin>` n'existe pas dans le dépôt, empêchant la publication d'un renvoi cassé.

Usage : python scripts/check_source_links.py [--docs docs] [--repo .]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Capture le chemin après blob/<branche>/ jusqu'au premier séparateur d'URL.
BLOB_RE = re.compile(
    r"https://github\.com/Simokes/tennismaintenance/blob/[^/]+/([^\s)\"'>#]+)"
)


def find_broken(docs_dir: Path, repo_root: Path):
    broken = []
    checked = 0
    for md in sorted(docs_dir.rglob("*.md")):
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for match in BLOB_RE.finditer(line):
                rel = match.group(1)
                checked += 1
                if not (repo_root / rel).is_file():
                    broken.append((md.relative_to(repo_root), lineno, rel))
    return broken, checked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", default="docs", help="dossier des pages publiées")
    parser.add_argument("--repo", default=".", help="racine du dépôt")
    args = parser.parse_args()

    repo_root = Path(args.repo).resolve()
    docs_dir = (repo_root / args.docs).resolve()
    if not docs_dir.is_dir():
        print(f"ERREUR : dossier introuvable : {docs_dir}", file=sys.stderr)
        return 2

    broken, checked = find_broken(docs_dir, repo_root)

    if broken:
        print(f"[ERREUR] {len(broken)} lien(s) source casse(s) sur {checked} verifie(s) :")
        for md, lineno, rel in broken:
            print(f"  - {md}:{lineno} -> document source manquant : {rel}")
        print("\nCorrige le lien ou ajoute le document source manquant a la racine.")
        return 1

    print(f"[OK] {checked} lien(s) source verifie(s), tous les documents existent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
