import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import load_dataset

plt.rcParams["font.size"] = 11

def characterize(csv_path: str, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = load_dataset(csv_path)

    def save_fig(name: str):
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, bottom=0.15, left=0.12, right=0.95)
        plt.grid(alpha=0.3, linestyle="--")
        plt.savefig(out / name, dpi=180)
        plt.close()

    # 1) Linguagens
    fig, ax = plt.subplots(figsize=(9,6))
    df["language"].value_counts().sort_values(ascending=False).plot(kind="bar", ax=ax, color="#5B8FF9")
    ax.set_title("Distribuição de Repositórios por Linguagem")
    ax.set_xlabel("Linguagem")
    ax.set_ylabel("Quantidade")
    save_fig("caracterizacao_linguagens.png")

    # 2) Stars
    fig, ax = plt.subplots(figsize=(9,6))
    df["stars"].plot(kind="hist", bins=10, color="#FF9F6E", ax=ax)
    ax.set_title("Distribuição de Stars")
    ax.set_xlabel("Stars")
    ax.set_ylabel("Frequência")
    save_fig("caracterizacao_stars_hist.png")

    # 3) Forks vs Stars
    fig, ax = plt.subplots(figsize=(9,6))
    df.plot(kind="scatter", x="stars", y="forks", ax=ax, color="#5AD8A6", alpha=0.7)
    ax.set_title("Relação Stars × Forks")
    ax.set_xlabel("Stars")
    ax.set_ylabel("Forks")
    save_fig("caracterizacao_stars_vs_forks.png")

    # 4) Idade dos Repositórios
    fig, ax = plt.subplots(figsize=(9,6))
    df["age_years"].plot(kind="hist", bins=10, color="#9270CA", ax=ax)
    ax.set_title("Distribuição da Idade dos Repositórios (anos)")
    ax.set_xlabel("Idade (anos)")
    ax.set_ylabel("Frequência")
    save_fig("caracterizacao_idade_hist.png")

    # 5) Dias desde último commit
    fig, ax = plt.subplots(figsize=(9,6))
    df["days_since_last_commit"].plot(kind="hist", bins=10, color="#F6BD16", ax=ax)
    ax.set_title("Dias Desde o Último Commit")
    ax.set_xlabel("Dias")
    ax.set_ylabel("Frequência")
    save_fig("caracterizacao_dias_ultimo_commit.png")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Caracterização do dataset")
    p.add_argument("csv", help="Caminho para o CSV de repositórios")
    p.add_argument("--out", default="graphics", help="Diretório de saída")
    args = p.parse_args()
    characterize(args.csv, args.out)
