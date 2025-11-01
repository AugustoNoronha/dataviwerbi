from pathlib import Path
import pandas as pd

REQUIRED_COLS = [
    "repo","language","stars","forks","issues","created_at","last_commit_at","commits_last_90d"
]

def load_dataset(csv_path: str) -> pd.DataFrame:
    """Load CSV and coerce dtypes expected by the project."""
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")
    df = pd.read_csv(p)
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Colunas faltando no dataset: {missing}. Esperado: {REQUIRED_COLS}")
    # Type coercions
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["last_commit_at"] = pd.to_datetime(df["last_commit_at"], errors="coerce")
    for c in ["stars","forks","issues","commits_last_90d"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    # Derived fields
    today = pd.Timestamp.today().normalize()
    df["days_since_last_commit"] = (today - df["last_commit_at"]).dt.days
    df["age_years"] = (today - df["created_at"]).dt.days / 365.25
    return df
