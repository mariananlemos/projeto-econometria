# =============================================================================
# ANÁLISE ECONOMÉTRICA — AGRONEGÓCIO BRASILEIRO (1995-2025)
# =============================================================================
# Relação entre PIB do Agronegócio, Consumo de Diesel e Área Plantada
#
# Fontes:
#   - PIB do Agronegócio: CEPEA/Esalq-USP (R$ bilhões, valores deflacionados)
#   - Consumo de Diesel: ANP — Agência Nacional do Petróleo (milhares de m³/ano)
#   - Área Plantada: IBGE/PAM — Produção Agrícola Municipal (milhões de hectares)
#
# Bibliotecas utilizadas: pandas, numpy, matplotlib, scipy.stats
# =============================================================================

import matplotlib
matplotlib.use('Agg')  # Backend não-interativo (salva gráficos sem abrir janelas)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Configuração geral dos gráficos
plt.rcParams.update({
    'figure.figsize': (12, 7),
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight'
})

# Diretório para salvar os gráficos
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
GRAFICOS_DIR = os.path.join(OUTPUT_DIR, 'graficos')
os.makedirs(GRAFICOS_DIR, exist_ok=True)

# =============================================================================
# ETAPA 1: Carregamento e inspeção dos dados
# =============================================================================
print("=" * 70)
print("ETAPA 1: CARREGAMENTO DOS DADOS")
print("=" * 70)

# Lê o arquivo CSV com os dados anuais
csv_path = os.path.join(OUTPUT_DIR, 'dados_econometria.csv')
df = pd.read_csv(csv_path)

# Exibe as primeiras linhas para verificação
print("\n📋 Primeiras linhas do DataFrame:")
print(df.head(10).to_string(index=False))

# Estatísticas descritivas das variáveis
print("\n📊 Estatísticas descritivas:")
print(df.describe().round(2).to_string())

# Verifica se há valores ausentes
print(f"\n🔍 Valores ausentes por coluna:\n{df.isnull().sum()}")
print(f"\n📏 Total de observações: {len(df)}")
print(f"📅 Período: {df['ano'].min()} a {df['ano'].max()}")


# =============================================================================
# ETAPA 2: Gráfico de dispersão — Consumo de Diesel × PIB Agro
# =============================================================================
print("\n" + "=" * 70)
print("ETAPA 2: GRÁFICO DE DISPERSÃO")
print("=" * 70)

fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot com cores representando o ano
scatter = ax.scatter(
    df['pib_agro'], df['consumo_diesel'],
    c=df['ano'], cmap='viridis', s=100, edgecolors='white',
    linewidth=1.5, zorder=5, alpha=0.9
)

# Barra de cores indicando o ano
cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label('Ano', fontsize=11)

# Rótulos dos eixos e título
ax.set_xlabel('PIB do Agronegócio (R$ bilhões, deflacionado)', fontsize=13)
ax.set_ylabel('Consumo de Diesel (milhares de m³/ano)', fontsize=13)
ax.set_title('Dispersão: Consumo de Diesel × PIB do Agronegócio\nBrasil (1995–2025)',
             fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# Anotações nos pontos extremos
for _, row in df.iterrows():
    if row['ano'] in [1995, 2000, 2005, 2010, 2015, 2020, 2025]:
        ax.annotate(
            str(int(row['ano'])),
            (row['pib_agro'], row['consumo_diesel']),
            textcoords="offset points", xytext=(8, 8),
            fontsize=8, color='gray', fontweight='bold'
        )

plt.tight_layout()
plt.savefig(os.path.join(GRAFICOS_DIR, '01_dispersao_diesel_pib.png'))
plt.close()
print("✅ Gráfico de dispersão salvo em graficos/01_dispersao_diesel_pib.png")


# =============================================================================
# ETAPA 3: Regressão Linear Simples
#   Modelo: consumo_diesel = β₁ + β₂ × pib_agro
# =============================================================================
print("\n" + "=" * 70)
print("ETAPA 3: REGRESSÃO LINEAR SIMPLES")
print("=" * 70)

# Variáveis da regressão simples
x = df['pib_agro'].values
y = df['consumo_diesel'].values

# Executa a regressão usando scipy.stats.linregress
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r_squared = r_value ** 2

# Exibe os resultados da regressão
print(f"\n📐 Modelo: consumo_diesel = β₁ + β₂ × pib_agro")
print(f"   ─────────────────────────────────────────────")
print(f"   β₁ (intercepto)  = {intercept:>12.4f}")
print(f"   β₂ (coeficiente) = {slope:>12.6f}")
print(f"   R²               = {r_squared:>12.4f}  ({r_squared*100:.2f}%)")
print(f"   R (correlação)   = {r_value:>12.4f}")
print(f"   p-valor (β₂)     = {p_value:>12.2e}")
print(f"   Erro padrão (β₂) = {std_err:>12.6f}")
print(f"\n   ▸ Interpretação: para cada aumento de R$ 1 bilhão no PIB Agro,")
print(f"     o consumo de diesel aumenta em {slope:.2f} milhares de m³.")

if p_value < 0.01:
    print(f"   ▸ O coeficiente β₂ é estatisticamente significativo ao nível de 1%.")
elif p_value < 0.05:
    print(f"   ▸ O coeficiente β₂ é estatisticamente significativo ao nível de 5%.")

# Valores preditos pela reta de regressão
y_pred_simples = intercept + slope * x

# Gráfico de dispersão com a reta de regressão ajustada
fig, ax = plt.subplots(figsize=(12, 7))

# Pontos observados
scatter = ax.scatter(
    x, y, c=df['ano'], cmap='viridis', s=100,
    edgecolors='white', linewidth=1.5, zorder=5, alpha=0.9,
    label='Dados observados'
)

# Reta de regressão
x_line = np.linspace(x.min() - 50, x.max() + 50, 300)
y_line = intercept + slope * x_line
ax.plot(x_line, y_line, color='crimson', linewidth=2.5, linestyle='-',
        label=f'Reta: ŷ = {intercept:.1f} + {slope:.4f}x', zorder=4)

# Intervalo de confiança (95%)
n = len(x)
x_mean = np.mean(x)
se_line = std_err * np.sqrt(1/n + (x_line - x_mean)**2 / np.sum((x - x_mean)**2))
# Usando t de Student para IC 95%
t_crit = stats.t.ppf(0.975, df=n-2)
ax.fill_between(
    x_line,
    intercept + slope * x_line - t_crit * se_line * np.sqrt(np.sum((y - y_pred_simples)**2)/(n-2)),
    intercept + slope * x_line + t_crit * se_line * np.sqrt(np.sum((y - y_pred_simples)**2)/(n-2)),
    alpha=0.15, color='crimson', label='IC 95%'
)

cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label('Ano', fontsize=11)

ax.set_xlabel('PIB do Agronegócio (R$ bilhões)', fontsize=13)
ax.set_ylabel('Consumo de Diesel (milhares de m³/ano)', fontsize=13)
ax.set_title(f'Regressão Linear Simples — R² = {r_squared:.4f}\n'
             f'consumo_diesel = {intercept:.1f} + {slope:.4f} × pib_agro',
             fontsize=14, fontweight='bold')
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')

# Caixa de texto com estatísticas
textstr = (f'R² = {r_squared:.4f}\n'
           f'β₁ = {intercept:.2f}\n'
           f'β₂ = {slope:.6f}\n'
           f'p = {p_value:.2e}\n'
           f'n = {n}')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.97, 0.35, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(GRAFICOS_DIR, '02_regressao_simples.png'))
plt.close()
print("✅ Gráfico de regressão simples salvo em graficos/02_regressao_simples.png")


# =============================================================================
# ETAPA 4: Regressão Linear Múltipla
#   Modelo: consumo_diesel = β₁ + β₂ × pib_agro + β₃ × area_plantada
# =============================================================================
print("\n" + "=" * 70)
print("ETAPA 4: REGRESSÃO LINEAR MÚLTIPLA")
print("=" * 70)

# Construção da matriz de variáveis explicativas (com constante)
# X = [1, pib_agro, area_plantada]
X_multi = np.column_stack([
    np.ones(n),                    # Coluna de 1s para o intercepto
    df['pib_agro'].values,         # Variável X₂
    df['area_plantada'].values     # Variável X₃
])

# Estimação por MQO (Mínimos Quadrados Ordinários): β = (X'X)⁻¹ X'y
# β = inv(X^T X) @ X^T y
XtX = X_multi.T @ X_multi
XtX_inv = np.linalg.inv(XtX)
beta_hat = XtX_inv @ (X_multi.T @ y)

# Valores preditos e resíduos
y_pred_multi = X_multi @ beta_hat
residuos_multi = y - y_pred_multi

# Cálculo do R² da regressão múltipla
SS_res = np.sum(residuos_multi ** 2)         # Soma dos quadrados dos resíduos
SS_tot = np.sum((y - np.mean(y)) ** 2)       # Soma dos quadrados total
R2_multi = 1 - (SS_res / SS_tot)

# R² ajustado (penaliza pelo número de variáveis)
k = 2  # número de variáveis explicativas (sem o intercepto)
R2_adj = 1 - ((1 - R2_multi) * (n - 1)) / (n - k - 1)

# Estimativa da variância dos resíduos
s2 = SS_res / (n - k - 1)

# Matriz de variância-covariância dos coeficientes
var_cov_beta = s2 * XtX_inv

# Erros padrão dos coeficientes
se_beta = np.sqrt(np.diag(var_cov_beta))

# Estatísticas t e p-valores para cada coeficiente
t_stats = beta_hat / se_beta
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=n - k - 1))

# Exibe os resultados
print(f"\n📐 Modelo: consumo_diesel = β₁ + β₂ × pib_agro + β₃ × area_plantada")
print(f"   ──────────────────────────────────────────────────────────────────")

# Tabela de coeficientes
print(f"\n   {'Variável':<20} {'Coeficiente':>12} {'Erro Padrão':>12} {'t-stat':>10} {'p-valor':>12}")
print(f"   {'─'*66}")
nomes = ['β₁ (intercepto)', 'β₂ (pib_agro)', 'β₃ (area_plantada)']
for i in range(3):
    sig = ''
    if p_values[i] < 0.01:
        sig = '***'
    elif p_values[i] < 0.05:
        sig = '**'
    elif p_values[i] < 0.10:
        sig = '*'
    print(f"   {nomes[i]:<20} {beta_hat[i]:>12.4f} {se_beta[i]:>12.4f} {t_stats[i]:>10.4f} {p_values[i]:>12.4e} {sig}")

print(f"\n   R²          = {R2_multi:.4f}  ({R2_multi*100:.2f}%)")
print(f"   R² ajustado = {R2_adj:.4f}  ({R2_adj*100:.2f}%)")
print(f"   σ² (resíd.) = {s2:.2f}")
print(f"   n           = {n}")

print(f"\n   ▸ Interpretação:")
print(f"     • Para cada R$ 1 bi a mais no PIB Agro (ceteris paribus),")
print(f"       o consumo de diesel varia em {beta_hat[1]:.2f} mil m³.")
print(f"     • Para cada 1 milhão de ha a mais de área plantada (ceteris paribus),")
print(f"       o consumo de diesel varia em {beta_hat[2]:.2f} mil m³.")

# Teste F (significância global do modelo)
SS_reg = SS_tot - SS_res
F_stat = (SS_reg / k) / (SS_res / (n - k - 1))
p_F = 1 - stats.f.cdf(F_stat, k, n - k - 1)
print(f"\n   📊 Teste F (significância global):")
print(f"      F-statistic = {F_stat:.4f}")
print(f"      p-valor     = {p_F:.2e}")

# Correlação entre variáveis explicativas (multicolinearidade)
corr_x = np.corrcoef(df['pib_agro'], df['area_plantada'])[0, 1]
print(f"\n   ⚠️  Correlação entre pib_agro e area_plantada: {corr_x:.4f}")
if abs(corr_x) > 0.8:
    print(f"      → Alta correlação! Possível multicolinearidade.")

# Comparação entre modelos
print(f"\n   📈 Comparação R² simples vs. múltiplo:")
print(f"      R² (simples)  = {r_squared:.4f}")
print(f"      R² (múltiplo) = {R2_multi:.4f}")
print(f"      R² ajustado   = {R2_adj:.4f}")
print(f"      Ganho absoluto de R² = {R2_multi - r_squared:.4f}")


# =============================================================================
# ETAPA 5: Gráfico de resíduos da regressão simples
# =============================================================================
print("\n" + "=" * 70)
print("ETAPA 5: ANÁLISE DE RESÍDUOS — REGRESSÃO SIMPLES")
print("=" * 70)

# Calcula os resíduos da regressão simples
residuos_simples = y - y_pred_simples

# Painel de diagnóstico com 4 subgráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Diagnóstico de Resíduos — Regressão Simples', fontsize=16, fontweight='bold')

# 5a) Resíduos vs. valores ajustados
ax1 = axes[0, 0]
ax1.scatter(y_pred_simples, residuos_simples, c='steelblue', s=80,
            edgecolors='white', linewidth=1, alpha=0.8)
ax1.axhline(y=0, color='crimson', linewidth=1.5, linestyle='--')
ax1.set_xlabel('Valores Ajustados (ŷ)')
ax1.set_ylabel('Resíduos (e)')
ax1.set_title('Resíduos vs. Valores Ajustados')
ax1.grid(True, alpha=0.3, linestyle='--')

# 5b) Resíduos ao longo do tempo
ax2 = axes[0, 1]
ax2.bar(df['ano'], residuos_simples, color='steelblue', alpha=0.7, edgecolor='navy', linewidth=0.5)
ax2.axhline(y=0, color='crimson', linewidth=1.5, linestyle='--')
ax2.set_xlabel('Ano')
ax2.set_ylabel('Resíduos (e)')
ax2.set_title('Resíduos ao Longo do Tempo')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.tick_params(axis='x', rotation=45)

# 5c) Histograma dos resíduos (normalidade)
ax3 = axes[1, 0]
ax3.hist(residuos_simples, bins=8, color='steelblue', alpha=0.7,
         edgecolor='navy', linewidth=1, density=True)
# Curva normal teórica sobreposta
mu_res, sigma_res = np.mean(residuos_simples), np.std(residuos_simples)
x_hist = np.linspace(residuos_simples.min() - 500, residuos_simples.max() + 500, 200)
ax3.plot(x_hist, stats.norm.pdf(x_hist, mu_res, sigma_res),
         color='crimson', linewidth=2, label='Normal teórica')
ax3.set_xlabel('Resíduos (e)')
ax3.set_ylabel('Densidade')
ax3.set_title('Histograma dos Resíduos')
ax3.legend()
ax3.grid(True, alpha=0.3, linestyle='--')

# 5d) QQ-Plot (teste visual de normalidade)
ax4 = axes[1, 1]
res_sorted = np.sort(residuos_simples)
n_res = len(res_sorted)
theoretical_q = stats.norm.ppf(np.arange(1, n_res + 1) / (n_res + 1))
ax4.scatter(theoretical_q, res_sorted, c='steelblue', s=80,
            edgecolors='white', linewidth=1, alpha=0.8)
# Linha de referência
q_min, q_max = theoretical_q.min(), theoretical_q.max()
ax4.plot([q_min, q_max],
         [mu_res + sigma_res * q_min, mu_res + sigma_res * q_max],
         color='crimson', linewidth=1.5, linestyle='--', label='Referência normal')
ax4.set_xlabel('Quantis Teóricos (Normal)')
ax4.set_ylabel('Quantis Observados')
ax4.set_title('QQ-Plot dos Resíduos')
ax4.legend()
ax4.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig(os.path.join(GRAFICOS_DIR, '03_residuos_regressao_simples.png'))
plt.show()

# Teste de normalidade dos resíduos (Shapiro-Wilk)
stat_sw, p_sw = stats.shapiro(residuos_simples)
print(f"\n   🧪 Teste de Normalidade (Shapiro-Wilk):")
print(f"      Estatística W = {stat_sw:.4f}")
print(f"      p-valor       = {p_sw:.4f}")
if p_sw > 0.05:
    print(f"      → Não se rejeita H₀: os resíduos seguem distribuição normal (5%).")
else:
    print(f"      → Rejeita H₀: os resíduos NÃO seguem distribuição normal (5%).")

# Estatísticas dos resíduos
print(f"\n   📊 Estatísticas dos resíduos:")
print(f"      Média       = {np.mean(residuos_simples):.4f}")
print(f"      Desvio-pad. = {np.std(residuos_simples):.2f}")
print(f"      Mínimo      = {np.min(residuos_simples):.2f}")
print(f"      Máximo      = {np.max(residuos_simples):.2f}")

print("\n✅ Gráficos de resíduos salvos em graficos/03_residuos_regressao_simples.png")


# =============================================================================
# ETAPA 6: Série temporal — Consumo de Diesel e PIB Agro (dois eixos Y)
# =============================================================================
print("\n" + "=" * 70)
print("ETAPA 6: SÉRIE TEMPORAL COM DOIS EIXOS Y")
print("=" * 70)

fig, ax1 = plt.subplots(figsize=(14, 7))

# Eixo Y esquerdo — Consumo de Diesel
color_diesel = '#1f77b4'
ax1.set_xlabel('Ano', fontsize=13)
ax1.set_ylabel('Consumo de Diesel (milhares de m³/ano)', color=color_diesel, fontsize=12)
line1 = ax1.plot(df['ano'], df['consumo_diesel'], color=color_diesel, linewidth=2.5,
                 marker='o', markersize=6, markerfacecolor='white', markeredgewidth=2,
                 label='Consumo de Diesel', zorder=5)
ax1.fill_between(df['ano'], df['consumo_diesel'], alpha=0.1, color=color_diesel)
ax1.tick_params(axis='y', labelcolor=color_diesel)
ax1.set_xlim(df['ano'].min() - 0.5, df['ano'].max() + 0.5)

# Eixo Y direito — PIB do Agronegócio
ax2 = ax1.twinx()
color_pib = '#d62728'
ax2.set_ylabel('PIB do Agronegócio (R$ bilhões)', color=color_pib, fontsize=12)
line2 = ax2.plot(df['ano'], df['pib_agro'], color=color_pib, linewidth=2.5,
                 marker='s', markersize=6, markerfacecolor='white', markeredgewidth=2,
                 label='PIB Agronegócio', zorder=5)
ax2.fill_between(df['ano'], df['pib_agro'], alpha=0.1, color=color_pib)
ax2.tick_params(axis='y', labelcolor=color_pib)

# Título
plt.title('Evolução do Consumo de Diesel e PIB do Agronegócio\nBrasil (1995–2025)',
          fontsize=15, fontweight='bold', pad=20)

# Legenda combinada
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', framealpha=0.9, fontsize=11)

# Grade
ax1.grid(True, alpha=0.3, linestyle='--')

# Destaca anos de marcos importantes
marcos = {
    2003: 'Boom\ncommodities',
    2008: 'Crise\nfinanceira',
    2016: 'Recessão\nBR',
    2020: 'Pandemia\nCOVID-19'
}
for ano_marco, texto in marcos.items():
    ax1.axvline(x=ano_marco, color='gray', alpha=0.4, linestyle=':', linewidth=1)
    ax1.annotate(
        texto, xy=(ano_marco, ax1.get_ylim()[1]),
        xytext=(0, 10), textcoords='offset points',
        fontsize=7, color='gray', ha='center', va='bottom',
        fontweight='bold'
    )

fig.tight_layout()
plt.savefig(os.path.join(GRAFICOS_DIR, '04_serie_temporal_diesel_pib.png'))
plt.show()
print("✅ Gráfico de série temporal salvo em graficos/04_serie_temporal_diesel_pib.png")


# =============================================================================
# RESUMO FINAL
# =============================================================================
print("\n" + "=" * 70)
print("RESUMO FINAL DA ANÁLISE ECONOMÉTRICA")
print("=" * 70)
print(f"""
┌────────────────────────────────────────────────────────────────────┐
│  REGRESSÃO SIMPLES                                                 │
│  consumo_diesel = {intercept:.2f} + {slope:.4f} × pib_agro         │
│  R² = {r_squared:.4f}  |  p-valor = {p_value:.2e}                  │
├────────────────────────────────────────────────────────────────────┤
│  REGRESSÃO MÚLTIPLA                                                │
│  consumo_diesel = {beta_hat[0]:.2f} + {beta_hat[1]:.4f} × pib_agro │
│                  + {beta_hat[2]:.4f} × area_plantada               │
│  R² = {R2_multi:.4f}  |  R² adj = {R2_adj:.4f}                     │
├────────────────────────────────────────────────────────────────────┤
│  DIAGNÓSTICO                                                       │
│  Normalidade (Shapiro-Wilk): p = {p_sw:.4f}                        │
│  Correlação explicativas: r = {corr_x:.4f}                         │
│  Teste F (global): F = {F_stat:.2f}, p = {p_F:.2e}                 │
└────────────────────────────────────────────────────────────────────┘

📁 Gráficos salvos em: {GRAFICOS_DIR}
   • 01_dispersao_diesel_pib.png
   • 02_regressao_simples.png
   • 03_residuos_regressao_simples.png
   • 04_serie_temporal_diesel_pib.png
""")
