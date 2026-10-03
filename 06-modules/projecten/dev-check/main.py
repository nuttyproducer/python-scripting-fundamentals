"""dev-check — controleer of je Python-omgeving volledig is."""

import sys
import importlib.util

# Pakketten die je dit semester nodig hebt
PAKKETTEN = ["jupyter", "pandas", "matplotlib", "seaborn"]


def is_geinstalleerd(pakket: str) -> bool:
    """Geeft True als het pakket geïnstalleerd is."""
    # TODO: gebruik importlib.util.find_spec() en geef terug of het bestaat
    ...


def main():
    print("=== Dev-check ===")
    # TODO: print de Python-versie (sys.version)
    # TODO: loop over PAKKETTEN en print ✅ of ❌ per pakket, netjes uitgelijnd


if __name__ == "__main__":
    main()
