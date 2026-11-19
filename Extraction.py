
"""
Exploration initiale des 6 fichiers retenus du dataset MuMiN.
"""

from pathlib import Path
import pandas as pd

# Chemins
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "mumin_raw"

# Les 6 fichiers retenus pour notre projet
FILES = [
    "user",
    "tweet",
    "claim",
    "user_follows_user",
    "user_retweeted_tweet",
    "tweet_discusses_claim",
]


def load_table(name: str) -> pd.DataFrame:
    path = DATA_DIR / name

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    return pd.read_pickle(path, compression="xz")


def explore_files():
    print("EXPLORATION DU DATASET MuMiN")
    print("=" * 60)

    for name in FILES:
        print(f"\n\nFICHIER : {name}")
        print("-" * 60)

        df = load_table(name)

        print("Dimensions :", df.shape)
        print("Nombre de lignes :", f"{len(df):,}")
        print("Colonnes :", df.columns.tolist())

        print("\nTypes des colonnes :")
        print(df.dtypes)

        print("\nTrois premières lignes :")
        print(df.head(3).to_string(index=False))

        del df

    print("\nExploration terminée.")


if __name__ == "__main__":
    explore_files()
