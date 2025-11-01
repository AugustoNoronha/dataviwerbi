import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import load_dataset

plt.rcParams["font.size"] = 11

def rq_visuals(csv_path: str, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = load_dataset(csv_path)

    def save_fig(name: str):
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, bottom=0.15, left=0.12, right=0.95)
        plt.grid(alpha=0.3, linestyle="--")
        plt.savefig(out / name, dpi=180)
        plt.close()

    # RQ1 – Stars por Linguagem
    fig, ax = plt.subplots(figsize=(9,6))
    df.boxplot(column="stars", by="language", rot=30, ax=ax, patch_artist=True)
    ax.set_title("RQ1: Stars por Linguagem (Boxplot)")
    plt.suptitle("")
    ax.set_xlabel("Linguagem")
    ax.set_ylabel("Stars")
    save_fig("rq1_stars_por_linguagem_boxplot.png")

    # RQ2 – Commits (90d) vs Stars
    fig, ax = plt.subplots(figsize=(9,6))
    df.plot(kind="scatter", x="commits_last_90d", y="stars", ax=ax, color="#5AD8A6", alpha=0.7)
    ax.set_title("RQ2: Commits (últimos 90 dias) × Stars")
    ax.set_xlabel("Commits nos últimos 90 dias")
    ax.set_ylabel("Stars")
    save_fig("rq2_commits90d_vs_stars_scatter.png")

    # Correlação Pearson
    corr = df[["commits_last_90d","stars"]].corr(method="pearson").iloc[0,1]
    (out / "rq2_correlacao.txt").write_text(
        f"Correlação de Pearson (commits_last_90d vs stars): {corr:.3f}",
        encoding="utf-8"
    )


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Visualizações para RQs")
    p.add_argument("csv", help="Caminho para o CSV de repositórios")
    p.add_argument("--out", default="graphics", help="Diretório de saída")
    args = p.parse_args()
    rq_visuals(args.csv, args.out)
