# LAB04 – Visualização de Dados (versão em Python)

Este repositório entrega uma alternativa **em Python** ao laboratório de BI – gerando as mesmas ideias de **caracterização do dataset** e **visualizações por RQ** (Perguntas de Pesquisa), mas com scripts reprodutíveis (pandas + matplotlib).

> Baseado nas diretrizes do enunciado *LABORATÓRIO 04 – Visualização de dados utilizando uma ferramenta de BI* da disciplina **Laboratório de Experimentação de Software**. A proposta original usa Power BI / Tableau / Looker Studio; aqui fornecemos uma opção programática para facilitar a automação e o versionamento.

## Estrutura

```
bi-dashboard-python/
├── data/
│   └── sample_repos.csv           # Amostra de dados (GitHub) para teste
├── graphics/                      # Saída dos gráficos gerados (é ignorado no Git)
├── src/
│   ├── utils.py                   # Funções de carregamento e derivação
│   ├── data_characterization.py   # Caracterização do dataset
│   └── rq_visualizations.py       # Gráficos para RQs (exemplos)
├── run_all.py                     # Pipeline simples para gerar tudo
├── requirements.txt               # Dependências
└── .gitignore
```

## Como executar

1. **Criar o ambiente** (recomendado):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```
2. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Rodar com sua base** (CSV deve conter as colunas abaixo):
   ```bash
   python run_all.py data/sample_repos.csv
   # ou
   python src/data_characterization.py data/seu_dataset.csv --out graphics
   python src/rq_visualizations.py data/seu_dataset.csv --out graphics
   ```

### Colunas esperadas no CSV

- `repo` (str) – nome do repositório  
- `language` (str) – linguagem principal  
- `stars` (int) – número de stars  
- `forks` (int) – número de forks  
- `issues` (int) – issues abertas  
- `created_at` (date) – data de criação (YYYY-MM-DD)  
- `last_commit_at` (date) – data do último commit (YYYY-MM-DD)  
- `commits_last_90d` (int) – total de commits nos últimos 90 dias

> O script converte datas/numéricos e deriva `days_since_last_commit` e `age_years` automaticamente.

## O que é gerado

Em `graphics/`:
- `caracterizacao_linguagens.png`
- `caracterizacao_stars_hist.png`
- `caracterizacao_stars_vs_forks.png`
- `caracterizacao_idade_hist.png`
- `caracterizacao_dias_ultimo_commit.png`
- `rq1_stars_por_linguagem_boxplot.png`
- `rq2_commits90d_vs_stars_scatter.png`
- `rq2_correlacao.txt` (valor da correlação de Pearson)

## Adaptação para o seu GQM

- **RQ1 (exemplo):** “Existe relação entre *linguagem* e *popularidade (stars)*?” – *boxplot por linguagem*  
- **RQ2 (exemplo):** “Atividade recente impacta popularidade?” – *scatter commits(90d) × stars + correlação*

Você pode **duplicar/alterar** `rq_visualizations.py` para espelhar as suas RQs reais, ajustando métricas, filtros e rótulos.

## Licença

Livre uso acadêmico. Ajuste conforme sua necessidade.
