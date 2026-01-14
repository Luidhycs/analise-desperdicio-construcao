# Análise de Desperdício Operacional — Construção Civil

Projeto acadêmico extensionista voltado à análise de dados operacionais
em uma **pequena empresa de construção de obras**, com foco na
identificação e redução de desperdícios de materiais de obra por meio
de decisões baseadas em dados.

## Contexto
Pequenas construtoras frequentemente enfrentam perdas financeiras
decorrentes de desperdício de materiais, causadas por compra excessiva,
armazenamento inadequado, retrabalho e falta de controle histórico de
consumo.

Este projeto simula um cenário real da construção civil, analisando
dados de consumo e descarte de materiais estruturais, agregados,
alvenaria e acabamento.

## Objetivo
- Analisar o consumo e descarte de materiais de obra
- Identificar materiais e setores com maior impacto financeiro
- Diagnosticar falhas nos processos de compra e uso
- Simular estratégias de redução de desperdício
- Estimar a economia gerada por decisões baseadas em dados

## Dados
Os dados utilizados são **simulados**, porém estruturados com base em
cenários reais de pequenas empresas de construção civil, contemplando:

- Materiais estruturais (cimento, areia, brita)
- Materiais de alvenaria (blocos cerâmicos)
- Materiais de acabamento (tinta)
- Setores de obra e acabamento
- Período de três meses (junho a agosto)

## Metodologia
1. Estruturação dos dados operacionais em formato tabular
2. Tratamento e limpeza dos dados utilizando Python
3. Criação de métricas de desperdício e custo
4. Análise exploratória por material, setor e período
5. Diagnóstico das principais fontes de desperdício
6. Simulação de redução de custos a partir de otimizações no processo

## Análises Realizadas
- Custo de desperdício por material
- Distribuição do desperdício por setor
- Evolução mensal do desperdício
- Identificação dos materiais mais críticos
- Simulação de redução de desperdício nos itens de maior impacto

## Resultados
A análise identificou que os maiores impactos financeiros estão
concentrados em materiais de alto volume e custo, como blocos cerâmicos,
tinta acrílica e agregados.

A simulação de ajustes no controle de compras e uso dos materiais
indicou uma **redução estimada de aproximadamente 27% nos custos
operacionais relacionados ao desperdício**.

## Tecnologias Utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- SQLite (documentado)

## Estrutura do Projeto
```text
analise-desperdicio-operacional/
│
├── data/
│   └── desperdicio_operacional.csv
│
├── notebooks/
│   └── analise_desperdicio.ipynb
│
├── src/
│   └── analise.py
│
├── output/
│   ├── *.csv
│   ├── *.png
│   └── resumo_analise.txt
│
├── README.md
└── requirements.txt
