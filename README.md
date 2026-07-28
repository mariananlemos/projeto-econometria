# 📊 Análise Econométrica — Consumo de Diesel × PIB do Agronegócio Brasileiro

Trabalho de econometria que investiga a relação entre o **consumo de diesel** e o **PIB do agronegócio** (valor adicionado, metodologia CEPEA/Esalq-USP) no Brasil, para o período de **1995 a 2025**.

## 🎯 Objetivo

Quantificar, por meio de regressão linear (MQO), como o crescimento do agronegócio brasileiro se relaciona com a demanda por diesel — principal combustível da cadeia produtiva agrícola.

## 📂 Estrutura do Projeto

```
projeto-econometria/
├── analise_econometrica.py    # Script principal com toda a análise
├── dados_econometria.csv      # Base de dados (31 observações, 1995-2025)
├── trabalho_econometria.md    # Relatório completo do trabalho acadêmico
├── graficos/                  # Gráficos gerados pela análise
│   ├── 01_dispersao_diesel_pib.png
│   ├── 02_regressao_simples.png
│   ├── 03_residuos_regressao_simples.png
│   └── 04_serie_temporal_diesel_pib.png
├── .gitignore
└── README.md
```

## 📈 Modelos Estimados

### Regressão Simples
```
consumo_diesel = 33.033,43 + 13,55 × pib_agro
R² = 0,7834  |  p-valor = 3,83 × 10⁻¹¹
```

### Regressão Múltipla
```
consumo_diesel = 2.086,22 − 2,34 × pib_agro + 736,38 × area_plantada
R² = 0,9488  |  R² ajustado = 0,9452
```

## 📊 Gráficos

| Dispersão | Regressão Simples |
|:-:|:-:|
| ![Dispersão](graficos/01_dispersao_diesel_pib.png) | ![Regressão](graficos/02_regressao_simples.png) |

| Diagnóstico de Resíduos | Série Temporal |
|:-:|:-:|
| ![Resíduos](graficos/03_residuos_regressao_simples.png) | ![Série](graficos/04_serie_temporal_diesel_pib.png) |

## 🗂️ Fontes dos Dados

| Variável | Fonte |
|---|---|
| PIB do Agronegócio (R$ bi, deflacionado) | [CEPEA/Esalq-USP](https://www.cepea.esalq.usp.br/br/pib-do-agronegocio-brasileiro.aspx) |
| Consumo de Diesel (mil m³/ano) | [ANP](https://www.gov.br/anp/) |
| Área Plantada (mi ha) | [IBGE/PAM](https://sidra.ibge.gov.br/) |

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.8+
- Bibliotecas: `pandas`, `numpy`, `matplotlib`, `scipy`

### Instalação das dependências
```bash
pip install pandas numpy matplotlib scipy
```

### Executar a análise
```bash
python analise_econometrica.py
```

Os gráficos serão salvos automaticamente na pasta `graficos/`.

## 📝 Principais Resultados

- O PIB agro **sozinho** explica **78%** da variação no consumo de diesel
- Com a **área plantada** como controle, o modelo explica **94,9%**
- A **área plantada** é o principal preditor direto (cada 1 mi ha → +736 mil m³ de diesel)
- Alta **multicolinearidade** entre PIB agro e área plantada (r = 0,93)
- Resíduos **não passam** no teste de normalidade de Shapiro-Wilk (p = 0,012)

## 📚 Referências Principais

- BARROS, G. S. de C. et al. *PIB do Agronegócio Brasileiro: metodologia e estimação.* CEPEA/Esalq-USP, 2020.
- GASQUES, J. G. et al. *Produtividade total dos fatores e transformações da agricultura brasileira.* IPEA, 2010.
- WOOLDRIDGE, J. M. *Introductory Econometrics: A Modern Approach.* 5ª ed., 2012.

---

> Trabalho desenvolvido para fins acadêmicos.
