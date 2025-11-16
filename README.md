# LAB04 – Visualização de Dados BI TIS-6

## Introdução

Este trabalho integra as atividades do Laboratório de Experimentação em Engenharia de Software (TIS 6) e tem como propósito aplicar princípios de Business Intelligence (BI) na análise de informações provenientes de repositórios de software. Para isso, utiliza-se o Microsoft Power BI como principal ferramenta de exploração e visualização dos dados coletados.

O Business Intelligence consiste no conjunto de práticas voltadas à obtenção, organização, interpretação e apresentação de dados, permitindo que decisões sejam tomadas com base em informações concretas. Por meio de dashboards dinâmicos e atualizados automaticamente, torna-se possível observar padrões, identificar problemas recorrentes e reconhecer oportunidades de otimização, contribuindo para o aprimoramento da qualidade do código e para o aumento da eficiência das equipes de desenvolvimento.


## Caracterização do Dataset

O conjunto de dados analisado neste projeto foi obtido a partir de diversos repositórios hospedados no GitHub. Ele reúne informações referentes a commits, além de métricas relacionadas à complexidade e à qualidade do código. A seguir, apresentam-se as principais tabelas utilizadas e seus respectivos atributos:

| Tabela                   | Descrição                          | Principais Campos                                                                 |
|--------------------------|-------------------------------------|------------------------------------------------------------------------------------|
| commits                  | Registros de commits realizados     | commit_hash, created_at, repository_id, changed_files, changed_sloc               |
| commits_metrics metrics  | Métricas de código por commit       | cbo, rfc, wmc, total_code_smells, blocker_quantity, critical_quantity, major_quantity, minor_quantity, info_quantity |
| commits_metrics repositories | Dados dos repositórios          | name, stars, created_at                                                            |

**Período considerado na análise:** janeiro a dezembro do ano avaliado  
**Quantidade de repositórios:** 22  
**Número total de commits:** 1000  

As métricas foram processadas e estruturadas de forma a possibilitar comparações entre qualidade do código, níveis de complexidade e padrões de alteração, tanto por repositório quanto em intervalos mensais.
