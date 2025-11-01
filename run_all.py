from pathlib import Path
import subprocess, sys

def run(csv_path: str, out_dir: str = "graphics"):
    base = Path(__file__).resolve().parent
    py = sys.executable

    print(">> Caracterização do dataset...")
    subprocess.check_call([py, str(base/"src"/"data_characterization.py"), csv_path, "--out", out_dir])

    print(">> Visualizações de RQs...")
    subprocess.check_call([py, str(base/"src"/"rq_visualizations.py"), csv_path, "--out", out_dir])

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Pipeline simples para gerar gráficos do dashboard")
    p.add_argument("csv", help="Caminho para o CSV (ex.: data/sample_repos.csv)")
    p.add_argument("--out", default="graphics", help="Diretório de saída")
    args = p.parse_args()
    run(args.csv, args.out)
