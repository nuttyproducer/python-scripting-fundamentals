"""dev-check — controleer of je Python-omgeving volledig is."""

import sys
import importlib.util

PAKKETTEN = ["jupyter", "pandas", "matplotlib", "seaborn"]


def is_geinstalleerd(pakket: str) -> bool:
    """Geeft True als het pakket geïnstalleerd is."""
    return importlib.util.find_spec(pakket) is not None


def main():
    print("=== Dev-check ===\n")
    print(f"Python-versie: {sys.version.split()[0]}")

    print("\nPakketten:")
    for pakket in PAKKETTEN:
        status = "✅" if is_geinstalleerd(pakket) else "❌"
        print(f"  {status}  {pakket:<12}")

    geinstalleerd = sum(1 for p in PAKKETTEN if is_geinstalleerd(p))
    print(f"\n{geinstalleerd}/{len(PAKKETTEN)} pakketten geïnstalleerd.")


if __name__ == "__main__":
    main()
