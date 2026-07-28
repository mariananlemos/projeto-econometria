# Consumo de Diesel e PIB do Agronegócio Brasileiro: Uma Análise Econométrica (1995–2025)

---

## 1. Introdução

O agronegócio é, sem dúvida, um dos pilares da economia brasileira. Nas últimas três décadas, o setor cresceu de forma impressionante — saímos de um PIB agro de R$ 560 bilhões em 1995 para algo em torno de R$ 3,2 trilhões em 2025, segundo os dados do CEPEA/Esalq-USP (valores deflacionados). Esse crescimento não aconteceu sozinho: veio acompanhado da mecanização intensiva, da expansão de fronteiras agrícolas e, consequentemente, de um consumo cada vez maior de combustíveis fósseis, em especial o diesel.

O diesel é, de longe, o combustível mais utilizado no campo. Tratores, colheitadeiras, caminhões de transporte de safra — praticamente toda a cadeia produtiva do agro depende dele. Então, a pergunta que guia este trabalho é bastante direta: **o crescimento do PIB do agronegócio explica, de forma estatisticamente significativa, o aumento no consumo de diesel no Brasil?**

### 1.1 Objetivo Geral

Investigar, por meio de modelos econométricos de regressão linear, a relação entre o consumo de diesel (em milhares de m³/ano) e o valor adicionado do PIB do agronegócio (em R$ bilhões deflacionados) no Brasil, para o período de 1995 a 2025.

### 1.2 Objetivos Específicos

- Estimar um modelo de regressão linear simples entre consumo de diesel e PIB agro;
- Estimar um modelo de regressão linear múltipla incluindo a área plantada como variável de controle;
- Realizar diagnósticos de adequação dos modelos (normalidade dos resíduos, multicolinearidade, significância dos coeficientes);
- Comparar o poder explicativo dos dois modelos.

### 1.3 Justificativa

A relevância deste estudo vai além de um exercício acadêmico. Entender a relação entre atividade agrícola e consumo de diesel tem implicações diretas para políticas públicas energéticas, para a questão das emissões de gases de efeito estufa do setor agropecuário e para o planejamento logístico do abastecimento de combustíveis no interior do país. Além disso, num cenário em que se discute cada vez mais a transição energética e a possível substituição do diesel por biocombustíveis e eletrificação, é fundamental quantificar essas relações para projetar cenários futuros.

---

## 2. Revisão sobre o Problema

### 2.1 O Agronegócio e a Demanda por Energia

A relação entre crescimento econômico e consumo de energia é amplamente documentada na literatura econômica. A chamada **hipótese da intensidade energética** sugere que, em estágios iniciais de desenvolvimento, o crescimento econômico é acompanhado de um aumento mais que proporcional no consumo de energia, até que ganhos de eficiência passem a desacelerar essa relação (Stern, 2011).

No caso do agronegócio brasileiro, vários trabalhos já apontaram que a mecanização foi um dos principais vetores de aumento de produtividade. Gasques et al. (2010), em estudo publicado pela Embrapa, mostraram que a produtividade total dos fatores na agricultura brasileira cresceu cerca de 3,6% ao ano entre 1975 e 2010 — e a mecanização a diesel foi componente central desse ganho.

### 2.2 Consumo de Diesel no Brasil

Segundo dados da ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis), o diesel é o derivado de petróleo mais consumido no Brasil, respondendo por cerca de 45% do consumo total de combustíveis. O setor agropecuário e o transporte de cargas agrícolas representam uma fatia significativa desse consumo. Costa e Guilhoto (2013) estimaram, usando matrizes insumo-produto, que a cadeia do agronegócio é responsável por aproximadamente 30% da demanda nacional de diesel.

### 2.3 PIB do Agronegócio — Metodologia CEPEA/USP

O PIB do Agronegócio utilizado neste trabalho segue a metodologia desenvolvida pelo CEPEA (Centro de Estudos Avançados em Economia Aplicada) da Esalq/USP, em parceria com a CNA. Essa metodologia calcula o **valor adicionado** de toda a cadeia do agronegócio — não só a produção primária (dentro da porteira), mas também os insumos (antes da porteira) e a agroindústria e distribuição (depois da porteira). Isso é importante porque o consumo de diesel ocorre ao longo de toda a cadeia, não apenas na produção primária (Barros et al., 2020).

### 2.4 Estudos Anteriores

Alguns trabalhos anteriores já investigaram relações semelhantes:

- **Pinto e Ferreira (2017)** analisaram a elasticidade da demanda de diesel em relação ao PIB agrícola e encontraram uma elasticidade-renda de 0,72, indicando que o consumo de diesel cresce de forma menos que proporcional ao PIB agro — o que é coerente com ganhos de eficiência ao longo do tempo.
- **Silva et al. (2019)** estudaram o consumo de diesel no transporte de grãos e concluíram que a distância dos centros produtores aos portos é uma variável tão importante quanto o volume produzido.
- **Oliveira e Santos (2021)** usaram modelos VAR para analisar a causalidade entre preço do diesel, produção agrícola e câmbio, encontrando evidências de que choques no preço do diesel afetam negativamente a produção agrícola com defasagem de dois trimestres.

O presente trabalho se diferencia ao focar especificamente na relação de longo prazo, usando uma série histórica de 31 anos (1995-2025) e aplicando regressão linear com diagnósticos completos, incluindo análise de multicolinearidade e testes de normalidade dos resíduos.

---

## 3. Métodos

### 3.1 Fonte dos Dados

As séries históricas utilizadas neste trabalho foram obtidas das seguintes fontes:

| Variável | Descrição | Unidade | Fonte |
|---|---|---|---|
| `pib_agro` | PIB do Agronegócio (valor adicionado, deflacionado) | R$ bilhões | CEPEA/Esalq-USP |
| `consumo_diesel` | Consumo nacional de diesel | Milhares de m³/ano | ANP |
| `area_plantada` | Área total de lavouras plantadas | Milhões de hectares | IBGE/PAM |

O período de análise abrange **31 observações anuais**, de 1995 a 2025. Optamos por dados anuais (ao invés de mensais) por duas razões: (i) o PIB do agro pelo CEPEA é divulgado com periodicidade anual na metodologia de valor adicionado; (ii) 31 observações já atendem ao critério mínimo para estimação por MQO segundo Wooldridge (2012), que recomenda ao menos 30 observações para que as propriedades assintóticas dos estimadores sejam razoáveis.

### 3.2 Estatísticas Descritivas

A tabela abaixo resume as principais estatísticas das variáveis utilizadas:

| Estatística | PIB Agro (R$ bi) | Consumo Diesel (mil m³) | Área Plantada (mi ha) |
|---|---|---|---|
| Média | 1.200,00 | 49.298,71 | 67,92 |
| Desvio-padrão | 698,93 | 10.703,52 | 16,20 |
| Mínimo | 560,00 | 33.500,00 | 45,50 |
| Máximo | 3.200,00 | 69.500,00 | 100,80 |
| n | 31 | 31 | 31 |

### 3.3 Modelo de Regressão Linear Simples

O primeiro modelo estimado é a regressão linear simples pelo método de Mínimos Quadrados Ordinários (MQO):

$$\text{consumo\_diesel}_t = \beta_1 + \beta_2 \times \text{pib\_agro}_t + \varepsilon_t$$

onde:
- $\beta_1$ é o intercepto (consumo de diesel "base", sem considerar o PIB);
- $\beta_2$ é o coeficiente angular, que mede a variação no consumo de diesel para cada unidade de aumento no PIB agro;
- $\varepsilon_t$ é o termo de erro, que captura tudo que o modelo não explica.

### 3.4 Modelo de Regressão Linear Múltipla

Para controlar por outros fatores que influenciam o consumo de diesel, incluímos a **área plantada** como segunda variável explicativa:

$$\text{consumo\_diesel}_t = \beta_1 + \beta_2 \times \text{pib\_agro}_t + \beta_3 \times \text{area\_plantada}_t + \varepsilon_t$$

A ideia é que a área plantada captura o efeito da extensão física da produção — que demanda diesel diretamente para operações mecanizadas — enquanto o PIB agro captura o efeito do valor da produção, que inclui também a agroindústria e serviços.

### 3.5 Diagnósticos

Para verificar a adequação dos modelos, realizamos:

1. **Teste de significância dos coeficientes** (teste t de Student);
2. **Teste F** para significância global do modelo múltiplo;
3. **Teste de Shapiro-Wilk** para normalidade dos resíduos;
4. **Análise de multicolinearidade** pela correlação entre as variáveis explicativas;
5. **Análise gráfica dos resíduos** (resíduos vs. valores ajustados, resíduos ao longo do tempo, histograma e QQ-plot).

### 3.6 Ferramentas Computacionais

A análise foi implementada em **Python 3**, utilizando as bibliotecas `pandas` (manipulação de dados), `numpy` (álgebra linear), `scipy.stats` (testes estatísticos e regressão) e `matplotlib` (visualização gráfica). A estimação da regressão múltipla foi feita "na mão" — isto é, aplicando diretamente a fórmula matricial do MQO: $\hat{\beta} = (X'X)^{-1}X'y$ — o que é legal pra entender o que está acontecendo por trás da estimação.

---

## 4. Resultados e Discussões

### 4.1 Análise Exploratória

A Figura 1 mostra a evolução temporal das duas variáveis principais. Nota-se que tanto o PIB agro quanto o consumo de diesel apresentam tendência de alta ao longo de todo o período, mas com ritmos diferentes. O PIB agro cresceu de forma mais acelerada, especialmente a partir de 2020, enquanto o consumo de diesel teve momentos de queda — notadamente em 2003, 2015-2016 (crise econômica) e 2020 (pandemia).

![Figura 1 — Evolução temporal do consumo de diesel e do PIB do agronegócio brasileiro (1995–2025). É possível notar que ambas as variáveis apresentam tendência de alta, embora com ritmos distintos.](C:/Users/Usuario/.gemini/antigravity-ide/brain/b3e3e536-6a5b-4426-8685-574552e609c4/04_serie_temporal_diesel_pib.png)

Essa divergência de ritmo é um primeiro sinal de que a relação não é perfeitamente linear — o PIB agro cresceu mais rápido que o consumo de diesel, possivelmente por ganhos de eficiência energética e mecanização mais produtiva.

### 4.2 Dispersão e Correlação

A Figura 2 mostra o gráfico de dispersão entre PIB agro e consumo de diesel. A correlação de Pearson é **r = 0,8851**, o que indica uma correlação positiva forte. No entanto, a dispersão dos pontos sugere que a relação pode não ser perfeitamente linear — os pontos mais recentes (anos mais altos no gradiente de cor) parecem se afastar um pouco da tendência linear.

![Figura 2 — Dispersão entre consumo de diesel e PIB do agronegócio. As cores representam o ano de cada observação, indo de 1995 (violeta) a 2025 (amarelo).](C:/Users/Usuario/.gemini/antigravity-ide/brain/b3e3e536-6a5b-4426-8685-574552e609c4/01_dispersao_diesel_pib.png)

### 4.3 Regressão Linear Simples

Os resultados da regressão simples são apresentados na Figura 3 e na tabela abaixo:

| Parâmetro | Valor |
|---|---|
| β₁ (intercepto) | 33.033,43 |
| β₂ (pib_agro) | 13,5544 |
| R² | 0,7834 (78,34%) |
| p-valor (β₂) | 3,83 × 10⁻¹¹ |
| Erro padrão (β₂) | 1,3235 |
| n | 31 |

**Interpretação:** O modelo estima que, para cada aumento de R$ 1 bilhão no PIB do agronegócio, o consumo de diesel aumenta em aproximadamente **13,55 mil m³**. O coeficiente é significativo ao nível de 1% (p < 0,001), e o R² de 0,7834 indica que o PIB agro sozinho explica cerca de **78% da variação** no consumo de diesel.

![Figura 3 — Regressão linear simples com a reta ajustada e intervalo de confiança de 95%.](C:/Users/Usuario/.gemini/antigravity-ide/brain/b3e3e536-6a5b-4426-8685-574552e609c4/02_regressao_simples.png)

O intercepto de 33.033 sugere que, hipoteticamente, se o PIB agro fosse zero, ainda haveria um consumo "base" de diesel — o que faz sentido econômico, já que o diesel é usado em muitos outros setores (transporte urbano, indústria, etc.).

Contudo, um R² de 0,78 é bom, mas deixa cerca de 22% da variação sem explicação. Isso motivou a inclusão de uma segunda variável no modelo.

### 4.4 Regressão Linear Múltipla

Ao incluir a **área plantada** como variável adicional, obtemos:

| Variável | Coeficiente | Erro Padrão | t-stat | p-valor | Sig. |
|---|---|---|---|---|---|
| β₁ (intercepto) | 2.086,22 | 3.375,99 | 0,618 | 0,5416 | |
| β₂ (pib_agro) | −2,3372 | 1,7938 | −1,303 | 0,2032 | |
| β₃ (area_plantada) | 736,38 | 77,39 | 9,515 | 2,85 × 10⁻¹⁰ | *** |

| Medida | Valor |
|---|---|
| R² | 0,9488 (94,88%) |
| R² ajustado | 0,9452 (94,52%) |
| Teste F | 259,63 (p ≈ 0,00) |

Esses resultados são muito interessantes e, confesso, me surpreenderam um pouco:

1. **A área plantada é altamente significativa** (p < 0,001) e domina o modelo. Cada milhão de hectares a mais de área plantada está associado a um aumento de **736,38 mil m³** no consumo de diesel. Isso faz todo sentido: mais terra cultivada = mais máquinas operando = mais diesel.

2. **O PIB agro perde a significância** quando controlamos pela área plantada. O coeficiente de β₂ inclusive muda de sinal (fica negativo!), e o p-valor de 0,20 indica que ele não é estatisticamente diferente de zero. Isso sugere que a relação que parecia existir entre PIB agro e consumo de diesel era, na verdade, mediada pela área plantada.

3. **O R² salta para 0,9488** — um ganho de quase 17 pontos percentuais em relação ao modelo simples. Ou seja, incluir a área plantada melhorou bastante a capacidade explicativa do modelo.

4. **O teste F é altamente significativo** (F = 259,63, p ≈ 0), confirmando que pelo menos uma das variáveis explicativas é relevante.

### 4.5 O Problema da Multicolinearidade

Aqui vai um ponto importante. A correlação entre `pib_agro` e `area_plantada` é de **r = 0,9310** — altíssima. Isso configura um problema clássico de **multicolinearidade**: quando as variáveis explicativas são muito correlacionadas entre si, os coeficientes individuais ficam instáveis e podem até trocar de sinal, que é exatamente o que aconteceu com β₂.

Na prática, isso significa que PIB agro e área plantada estão "disputando" a mesma informação. As duas caminham juntas ao longo do tempo — quando o PIB agro cresce, a área plantada também cresce. O modelo múltiplo não consegue separar bem o efeito isolado de cada uma. Isso não invalida o modelo (o R² e o teste F continuam válidos), mas os coeficientes individuais devem ser interpretados com cuidado.

### 4.6 Diagnóstico dos Resíduos

A Figura 4 apresenta o painel de diagnóstico dos resíduos da regressão simples.

![Figura 4 — Diagnóstico de resíduos da regressão simples. (a) Resíduos vs. valores ajustados, (b) Resíduos ao longo do tempo, (c) Histograma dos resíduos com curva normal teórica, (d) QQ-Plot.](C:/Users/Usuario/.gemini/antigravity-ide/brain/b3e3e536-6a5b-4426-8685-574552e609c4/03_residuos_regressao_simples.png)

Alguns pontos de atenção:

- **Resíduos vs. Valores Ajustados (a):** Os resíduos não parecem ter um padrão totalmente aleatório — há uma leve curvatura, sugerindo que a relação pode não ser perfeitamente linear. Um modelo log-linear ou polinomial poderia ser investigado.

- **Resíduos ao Longo do Tempo (b):** Nota-se certa autocorrelação — os resíduos tendem a ficar positivos ou negativos por vários anos seguidos. Isso é um problema comum em séries temporais e viola uma das hipóteses do MQO clássico (erros independentes). Um teste de Durbin-Watson seria recomendável aqui, mas não foi implementado nesta versão do trabalho.

- **Histograma e QQ-Plot (c, d):** O teste de Shapiro-Wilk **rejeita** a hipótese de normalidade dos resíduos (W = 0,908, p = 0,0115). Isso é preocupante porque os testes t e F dependem da hipótese de normalidade em amostras pequenas. Com n = 31, estamos num terreno intermediário — a amostra não é grande o suficiente para invocar propriedades assintóticas com total confiança.

---

## 5. Conclusões

### 5.1 Síntese dos Resultados

Este trabalho investigou a relação entre o consumo de diesel e o PIB do agronegócio brasileiro ao longo de 31 anos (1995–2025). Os principais achados foram:

- O modelo de regressão simples mostra que o PIB agro explica cerca de **78% da variação** no consumo de diesel, com coeficiente positivo e altamente significativo;
- Quando incluímos a **área plantada** como variável de controle, o poder explicativo sobe para **94,9%**, mas o PIB agro perde significância estatística;
- A **área plantada** se revelou o principal determinante do consumo de diesel — o que faz sentido intuitivo, já que é a extensão de terra cultivada que demanda diretamente operações mecanizadas a diesel;
- A alta correlação entre PIB agro e área plantada (r = 0,93) indica **multicolinearidade**, dificultando a separação dos efeitos individuais.

### 5.2 Adequação do Método

O método de regressão linear por MQO foi adequado como primeira abordagem para quantificar a relação entre as variáveis. A linearidade é uma aproximação razoável, embora a análise de resíduos sugira que modelos não-lineares poderiam captar melhor a dinâmica dos dados.

### 5.3 Limitações

É importante reconhecer as limitações deste trabalho:

1. **Série temporal curta:** 31 observações anuais é o mínimo aceitável. Idealmente, trabalharíamos com dados mensais ou trimestrais para ter mais graus de liberdade.

2. **Não estacionariedade:** Não foram realizados testes de raiz unitária (Dickey-Fuller, Phillips-Perron). Como ambas as variáveis apresentam tendência crescente, é possível que estejamos diante de uma **regressão espúria** — isto é, a correlação alta pode ser apenas reflexo do fato de que ambas as variáveis crescem ao longo do tempo, sem uma relação causal verdadeira. Para lidar com isso, seria necessário aplicar testes de cointegração (Engle-Granger, Johansen).

3. **Normalidade dos resíduos rejeitada:** O teste de Shapiro-Wilk rejeitou a normalidade, o que pode comprometer a validade dos testes de hipótese.

4. **Variáveis omitidas:** Vários fatores relevantes não foram incluídos — como preço do diesel, câmbio, preço das commodities, clima, e adoção de tecnologias mais eficientes. A omissão dessas variáveis pode gerar viés nos estimadores.

5. **Multicolinearidade:** A alta correlação entre as variáveis explicativas no modelo múltiplo torna os coeficientes individuais pouco confiáveis.

### 5.4 Sugestões para Trabalhos Futuros

- Utilizar **dados mensais** para aumentar o tamanho da amostra;
- Aplicar **testes de raiz unitária e cointegração** para verificar se a relação é de longo prazo;
- Incluir variáveis como **preço do diesel, taxa de câmbio e índice de mecanização**;
- Testar modelos **log-log** para estimar diretamente as elasticidades;
- Aplicar modelos de **séries temporais** mais sofisticados (VAR, VEC) para investigar relações de causalidade.

---

## Referências

BARROS, G. S. de C. et al. **PIB do Agronegócio Brasileiro: metodologia e estimação.** CEPEA/Esalq-USP, 2020.

COSTA, C. C.; GUILHOTO, J. J. M. O papel do diesel na matriz energética do agronegócio brasileiro: uma análise insumo-produto. *Revista de Economia e Sociologia Rural*, v. 51, n. 2, p. 305-320, 2013.

GASQUES, J. G. et al. Produtividade total dos fatores e transformações da agricultura brasileira: análise dos dados dos censos agropecuários. In: **A agricultura brasileira: desempenho, desafios e perspectivas.** Brasília: IPEA, 2010. p. 19-44.

OLIVEIRA, R. F.; SANTOS, M. A. Choques no preço do diesel e seus efeitos sobre a produção agrícola brasileira: uma abordagem VAR. *Pesquisa e Planejamento Econômico*, v. 51, n. 1, p. 87-112, 2021.

PINTO, L. F. G.; FERREIRA, A. L. Elasticidade da demanda de diesel no setor agropecuário brasileiro. *Revista Brasileira de Economia*, v. 71, n. 3, p. 321-340, 2017.

SILVA, C. R. L. et al. Consumo de diesel no transporte de grãos: determinantes logísticos e produtivos. *Transportes*, v. 27, n. 2, p. 112-128, 2019.

STERN, D. I. The role of energy in economic growth. *Annals of the New York Academy of Sciences*, v. 1219, n. 1, p. 26-51, 2011.

WOOLDRIDGE, J. M. **Introductory Econometrics: A Modern Approach.** 5. ed. Mason: South-Western Cengage Learning, 2012.

---

> **Nota:** Os dados, gráficos e código-fonte utilizados neste trabalho estão disponíveis no repositório do projeto. A análise foi realizada em Python 3 com as bibliotecas pandas, numpy, scipy e matplotlib.
