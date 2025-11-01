import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import load_dataset

def characterize(csv_path: str, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = load_dataset(csv_path)

    # 1) Languages distribution
    ax = df["language"].value_counts().sort_values(ascending=False).plot(kind="bar")
    ax.set_title("Distribuição de Repositórios por Linguagem")
    ax.set_xlabel("Linguagem")
    ax.set_ylabel("Quantidade de Repositórios")
    plt.tight_layout()
    plt.savefig(out / "caracterizacao_linguagens.png", dpi=160)
    plt.clf()

    # 2) Stars distribution (hist)
    ax = df["stars"].plot(kind="hist", bins=10)
    ax.set_title("Distribuição de Stars")
    ax.set_xlabel("Stars")
    ax.set_ylabel("Frequência")
    plt.tight_layout()
    plt.savefig(out / "caracterizacao_stars_hist.png", dpi=160)
    plt.clf()

    # 3) Forks vs Stars (scatter)
    ax = df.plot(kind="scatter", x="stars", y="forks")
    plt.title("Relação Stars x Forks")
    plt.xlabel("Stars")
    plt.ylabel("Forks")
    plt.tight_layout()
    plt.savefig(out / "caracterizacao_stars_vs_forks.png", dpi=160)
    plt.clf()

    # 4) Idade do repositório (anos)
    ax = df["age_years"].plot(kind="hist", bins=10)
    ax.set_title("Distribuição da Idade dos Repositórios (anos)")
    ax.set_xlabel("Idade (anos)")
    ax.set_ylabel("Frequência")
    plt.tight_layout()
    plt.savefig(out / "caracterizacao_idade_hist.png", dpi=160)
    plt.clf()

    # 5) Dias desde último commit
    ax = df["days_since_last_commit"].plot(kind="hist", bins=10)
    ax.set_title("Dias desde o Último Commit")
    ax.set_xlabel("Dias")
    ax.set_ylabel("Frequência")
    plt.tight_layout()
    plt.savefig(out / "caracterizacao_dias_ultimo_commit.png", dpi=160)
    plt.clf()

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Caracterização do dataset")
    p.add_argument("csv", help="Caminho para o CSV de repositórios")
    p.add_argument("--out", default="graphics", help="Diretório de saída (imagens)")
    args = p.parse_args()
    characterize(args.csv, args.out)
