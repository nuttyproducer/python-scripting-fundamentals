"""crypto-plotter — lees prijzen.csv en teken een lijngrafiek."""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("prijzen.csv")

    print(f"Hoogste prijs: €{df['prijs'].max():,.0f}")
    print(f"Laagste prijs: €{df['prijs'].min():,.0f}")

    plt.plot(df["dag"], df["prijs"], marker="o")
    plt.title("BTC-prijs over de tijd")
    plt.xlabel("Dag")
    plt.ylabel("Prijs (€)")
    plt.show()


if __name__ == "__main__":
    main()
