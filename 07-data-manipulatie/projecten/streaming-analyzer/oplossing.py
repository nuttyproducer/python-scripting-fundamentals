"""streaming-analyzer — lees de dataset en haal er inzichten uit."""

import pandas as pd

CSV_PAD = "../../data/streams.csv"


def main():
    df = pd.read_csv(CSV_PAD)

    print("Top 3 streamers op totale views:")
    top = df.groupby("naam")["views"].sum().sort_values(ascending=False).head(3)
    print(top)

    print(f"\nGemiddelde views: {df['views'].mean():,.0f}")
    print(f"Maximale views: {df['views'].max():,.0f}")

    print("\nSamenvatting:")
    print(df.describe())


if __name__ == "__main__":
    main()
