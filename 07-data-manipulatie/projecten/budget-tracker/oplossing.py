"""budget-tracker — lees budget.csv en visualiseer de netto per maand."""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("budget.csv")
    df["netto"] = df["inkomsten"] - df["uitgaven"]

    print(df[["maand", "netto"]])

    plt.bar(df["maand"], df["netto"])
    plt.title("Netto per maand")
    plt.xlabel("Maand")
    plt.ylabel("Netto (€)")
    plt.show()


if __name__ == "__main__":
    main()
