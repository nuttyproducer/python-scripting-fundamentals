"""Shared helper to emit clean .ipynb notebooks from a list of (kind, source) cells."""
import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def make_nb(path, cells, title="Python"):
    """Write a notebook to `path` (repo-root relative).

    cells: list of ("md", source) or ("code", source) tuples.
    """
    nb = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    for kind, src in cells:
        src = src.rstrip("\n") + "\n"
        if kind == "md":
            nb["cells"].append(
                {
                    "cell_type": "markdown",
                    "id": uuid.uuid4().hex[:8],
                    "metadata": {},
                    "source": src.splitlines(True),
                }
            )
        else:
            nb["cells"].append(
                {
                    "cell_type": "code",
                    "id": uuid.uuid4().hex[:8],
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": src.splitlines(True),
                }
            )
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote", path)
