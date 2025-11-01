import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import load_dataset

def rq_visuals(csv_path: str, out_dir: str):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = load_dataset(csv_path)

    # RQ1: Linguagem se relaciona com número de stars? (boxplot)
    ax = df.boxplot(column="stars", by="language", rot=30)
    plt.title("RQ1: Stars por Linguagem (Boxplot)")
    plt.suptitle("")
    plt.xlabel("Linguagem")
    plt.ylabel("Stars")
    plt.tight_layout()
    plt.savefig(out / "rq1_stars_por_linguagem_boxplot.png", dpi=160)
    plt.clf()

    # RQ2: Atividade recente (commits_last_90d) se correlaciona com stars? (scatter)
    ax = df.plot(kind="scatter", x="commits_last_90d", y="stars")
    plt.title("RQ2: Commits (90d) vs Stars")
    plt.xlabel("Commits nos últimos 90 dias")
    plt.ylabel("Stars")
    plt.tight_layout()
    plt.savefig(out / "rq2_commits90d_vs_stars_scatter.png", dpi=160)
    plt.clf()

    # RQ2b: Correlação numérica simples (Pearson)
    corr = df[["commits_last_90d","stars"]].corr(method="pearson").iloc[0,1]
    (out / "rq2_correlacao.txt").write_text(f"Correlação de Pearson (commits_last_90d vs stars): {corr:.3f}", encoding="utf-8")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Visualizações para RQs")
    p.add_argument("csv", help="Caminho para o CSV de repositórios")
    p.add_argument("--out", default="graphics", help="Diretório de saída (imagens)")
    args = p.parse_args()
    rq_visuals(args.csv, args.out)
