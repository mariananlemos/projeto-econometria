# Consumo de Diesel e PIB do Agronegócio Brasileiro: Uma Análise Econométrica (1996–2025)

---

## 1. Introdução

O agronegócio é, sem dúvida, um dos pilares mais importantes da economia brasileira. Nas últimas três décadas, o setor passou por uma transformação fantástica — saímos de um PIB do agronegócio de R$ 2,33 trilhões em 1996 para cerca de R$ 3,20 trilhões em 2025, segundo dados deflacionados do CEPEA/Esalq-USP (valores trazidos para a moeda de dezembro de 2025). Esse crescimento acelerado foi fortemente sustentado pelo avanço da mecanização agrícola, pela expansão de fronteiras e pelo ganho de produtividade no campo. Contudo, essa expansão tem uma contrapartida física direta: um consumo muito elevado de combustíveis fósseis, com destaque absoluto para o óleo diesel.

O óleo diesel é o combustível que move a agropecuária de ponta a ponta no Brasil. Ele está presente no funcionamento de tratores, colheitadeiras, pivôs de irrigação, geradores e, principalmente, na imensa frota de caminhões que realiza o escoamento das safras das fazendas até as indústrias e portos de exportação. Assim, entender a relação entre o desempenho econômico do setor e o volume de combustível consumido é fundamental. A pergunta central que guia esta pesquisa é: **o crescimento do PIB do agronegócio brasileiro explica, de forma estatisticamente significativa, o consumo nacional de óleo diesel no Brasil?**

### 1.1 Objetivo Geral

Investigar, por meio de um modelo econométrico de regressão linear simples, a relação entre as vendas (consumo) de óleo diesel pelas distribuidoras (em milhares de m³/ano) e o valor adicionado real do PIB do agronegócio (em R$ bilhões reais, base dezembro de 2025) no Brasil, no período de 1996 a 2025.

### 1.2 Objetivos Específicos

- Estimar, utilizando o método de Mínimos Quadrados Ordinários (MQO), a relação entre o consumo de óleo diesel (Y) e o PIB do agronegócio (X);
- Avaliar estatisticamente a significância do impacto do PIB sobre a demanda por diesel e o coeficiente de determinação ($R^2$);
- Conduzir testes diagnósticos de resíduos, especialmente o teste de Shapiro-Wilk para verificar a normalidade dos erros;
- Discutir a adequação econômica e as limitações do modelo de regressão para dados macroeconômicos de séries temporais.

### 1.3 Justificativa

A justificativa deste estudo é tanto teórica quanto prática. Sob o ponto de vista prático, o planejamento energético nacional depende diretamente da projeção de consumo de combustíveis. Como o agronegócio é um setor dinâmico e de forte crescimento, quantificar o impacto desse crescimento sobre a demanda por diesel ajuda o governo e as distribuidoras a estimarem gargalos de abastecimento e logística. Além disso, no contexto atual de discussões sobre transição energética (como o mandato de mistura de biodiesel e o desenvolvimento de maquinário elétrico ou híbrido), mensurar a dependência atual do setor em relação aos combustíveis tradicionais serve como um ponto de partida crítico para qualquer cenário de descarbonização da produção agropecuária.

---

## 2. Revisão sobre o Problema

### 2.1 O Agronegócio e a Demanda por Energia

A relação entre atividade econômica e demanda energética é um dos campos mais estudados na economia do desenvolvimento. Tradicionalmente, o crescimento da produção agrícola em larga escala é acompanhado por um aumento do consumo de energia. O agronegócio brasileiro seguiu esse caminho, substituindo o trabalho manual e tração animal por tratores de alta potência e sistemas automatizados, o que aumentou drasticamente a produtividade, mas também a queima de óleo diesel (STERN, 2011).

### 2.2 Estudos Anteriores e Referências Acadêmicas

A literatura econômica traz importantes contribuições que ajudam a entender como o agronegócio, sua mensuração e a demanda por diesel interagem no Brasil:

- **Barros et al. (2020)** detalham a metodologia de cálculo do PIB do agronegócio construída pelo CEPEA/Esalq-USP em parceria com a CNA. Os autores explicam que esse indicador mede o valor adicionado de toda a cadeia (antes, dentro e depois da porteira, incluindo insumos, agroindústria e agrosserviços). Essa abordagem ampla é muito útil para estudos de transporte e combustíveis, dado que a maior parte do diesel consumido no agronegócio ocorre na etapa de transporte rodoviário e agrosserviços de distribuição.
- **Gasques et al. (2010)** analisam a produtividade total dos fatores e mostram que a mecanização intensa do campo e o uso de fertilizantes químicos foram os principais motores do crescimento da agropecuária brasileira nas últimas dicas. Essa modernização do maquinário substituiu outras formas de energia pelo óleo diesel, gerando uma trajetória paralela de expansão econômica e de consumo de combustível fóssil.
- **Cardoso e Jesus (2017)** estimaram a elasticidade-preço e elasticidade-renda da demanda por diesel no Brasil. Eles constataram que a demanda por diesel é inelástica em relação ao preço no curto prazo, o que reflete a falta de substitutos próximos, e altamente dependente do nível de atividade econômica (renda), indicando que o crescimento do PIB é o principal impulsionador do consumo de combustível.
- Mais recentemente, a **Fundação Getulio Vargas (FGV Agro, 2025)** publicou um amplo mapeamento do perfil energético do campo. O estudo revela que a cadeia produtiva do agronegócio é responsável por consumir aproximadamente 30% de toda a energia gerada no país. O relatório destaca que a expansão da safra de grãos e das exportações agropecuárias cria uma demanda contínua por fontes de energia concentradas, como o óleo diesel e a eletricidade.

O presente trabalho busca somar-se a essa literatura, aplicando uma análise de regressão linear simples com dados históricos reais atualizados de 1996 a 2025 para verificar o ajuste empírico dessa relação.

---

## 3. Métodos

### 3.1 Fonte dos Dados

Para realizar este estudo, consolidamos séries históricas anuais de 1996 a 2025 (totalizando **30 observações**), utilizando bases de dados públicas e oficiais do país:

- **`consumo_diesel` (Variável Dependente - Y):** Vendas totais de óleo diesel pelas distribuidoras no mercado nacional (em milhares de $m^3$/ano). O dado original foi extraído da base de Dados Abertos da **ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis)**, que consolida a comercialização em metros cúbicos. Dividimos os valores por 1.000 para expressar a variável na escala de milhares de $m^3$.
- **`pib_agro` (Variável Independente - X):** Valor adicionado do PIB do Agronegócio Total calculado pelo **CEPEA/Esalq-USP** (em R$ bilhões deflacionados para dezembro de 2025). O dado original foi extraído em R$ milhões e dividido por 1.000 para a escala de bilhões, mantendo o valor real (ajustado pelo IGP-DI).

### 3.2 Estatísticas Descritivas

A Tabela 1 resume as principais medidas estatísticas das variáveis de estudo:

| Estatística | PIB Agro (R$ bilhões) | Consumo Diesel (milhares de m³) |
|---|---|---|
| Média | 2.378,57 | 49.627,78 |
| Desvio-padrão | 344,09 | 11.238,62 |
| Mínimo | 2.044,10 | 30.154,90 |
| Máximo | 3.200,58 | 69.476,71 |
| Observações (n) | 30 | 30 |

### 3.3 Modelo de Regressão Linear Simples (MQO)

Para quantificar a relação entre as séries, estimamos o seguinte modelo de regressão linear simples:

$$\text{consumo\_diesel}_t = \beta_1 + \beta_2 \cdot \text{pib\_agro}_t + \varepsilon_t$$

onde:
- $\beta_1$ é o intercepto (o consumo "base" de diesel quando o PIB agro tende a zero);
- $\beta_2$ é o coeficiente angular (a variação em milhares de $m^3$ no consumo de diesel para cada aumento de R$ 1 bilhão no PIB do agronegócio);
- $\varepsilon_t$ é o termo de erro estocástico.

O modelo foi estimado utilizando o método clássico de **Mínimos Quadrados Ordinários (MQO)**, que estima os coeficientes minimizando a soma dos erros quadrados observados: $\sum e_i^2 = \sum (y_i - \hat{y}_i)^2$.

### 3.4 Testes Diagnósticos

A fim de validar a consistência das conclusões estatísticas obtidas via MQO, realizamos:
1. **Teste t de Student:** Para avaliar se o coeficiente estimado $\beta_2$ é estatisticamente diferente de zero (relevância estatística);
2. **Coeficiente de Determinação ($R^2$):** Para medir a proporção da variação do diesel que é explicada pelo PIB agro;
3. **Teste de Shapiro-Wilk:** Aplicado sobre os resíduos ($e_i$) para testar se eles seguem uma distribuição normal ($H_0$: erros normais);
4. **Análise Gráfica:** Inspeção visual de resíduos contra valores ajustados e ao longo do tempo para detecção de anomalias (autocorrelação e heterocedasticidade).

---

## 4. Resultados e Discussões

### 4.1 Análise Exploratória e Evolução Temporal

A Figura 1 apresenta o comportamento das duas variáveis ao longo da série histórica. Nota-se que tanto o PIB do Agronegócio (linha vermelha) quanto o consumo de diesel (linha azul) apresentam uma clara tendência de alta ao longo do tempo. É importante destacar que as séries reais mostram flutuações e oscilações coerentes com a realidade do mercado. Por exemplo, a queda no PIB agro em 2005 reflete a severa estiagem e crise cambial vividas no período, enquanto a retração no diesel em 2015-2016 e em 2020 reflete a recessão nacional e a pandemia da COVID-19, respectivamente.

![Figura 1 — Evolução temporal das vendas de diesel e PIB do agronegócio no Brasil (1996–2025).](graficos/04_serie_temporal_diesel_pib.png)

A Figura 2 exibe o gráfico de dispersão com gradiente temporal (anos mais claros são os mais recentes). Há uma correlação linear positiva visível, mostrando que maiores valores do PIB do agronegócio estão fortemente associados a maiores consumos de óleo diesel.

![Figura 2 — Dispersão entre o Consumo de Diesel e o PIB do Agronegócio (1996–2025).](graficos/01_dispersao_diesel_pib.png)

### 4.2 Resultados da Regressão por MQO

A estimação do modelo gerou os coeficientes apresentados na Tabela 2:

| Parâmetro | Coeficiente | Erro Padrão | Estatística t | p-valor | Significância |
|---|---|---|---|---|---|
| Intercepto ($\beta_1$) | −8.155,09 | 12.784,07 | −0,6379 | 0,5288 | não sig. |
| PIB Agro ($\beta_2$) | 24,4125 | 5,2962 | 4,6094 | 0,000082 | *** (1%) |

A reta de regressão estimada é descrita pela seguinte equação linear:

$$\widehat{\text{consumo\_diesel}}_t = -8155,09 + 24,4125 \cdot \text{pib\_agro}_t$$

**Interpretação Econômica:** O coeficiente angular estimado de **24,4125** indica que, mantendo os demais fatores constantes (*ceteris paribus*), para cada aumento de R$ 1 bilhão no PIB real do agronegócio, as vendas anuais de diesel aumentam em aproximadamente **24,41 mil metros cúbicos** (cerca de 24,4 milhões de litros). O p-valor de $8,21 \times 10^{-5}$ é extremamente pequeno, rejeitando com muita segurança a hipótese nula de que o PIB agro não tem impacto sobre o diesel. O efeito é estatisticamente significativo ao nível de 1%.

O coeficiente de determinação **$R^2$ de 0,4307** indica que o PIB do agronegócio explica sozinho **43,07% da variação** do consumo nacional de diesel ao longo de 30 anos. Isso faz sentido econômico: o diesel no Brasil não é consumido exclusivamente pelo agronegócio. Outros setores (indústrias, transporte de passageiros urbanos, serviços logísticos gerais) dividem essa demanda. Portanto, o agronegócio explicar mais de 43% de todo o combustível consumido nacionalmente é um resultado bastante expressivo.

O intercepto negativo não possui interpretação econômica direta fora do intervalo de dados analisado. Na econometria, o intercepto é o valor extrapolado de Y caso X fosse igual a zero. Como o PIB do agronegócio brasileiro nunca esteve próximo de zero no período, o valor negativo serve apenas para o ajuste matemático da reta no quadrante de dados observados.

![Figura 3 — Reta de regressão ajustada sobre os dados observados (1996–2025).](graficos/02_regressao_simples.png)

### 4.3 Diagnóstico dos Resíduos

A validação das hipóteses clássicas do MQO foi feita por meio de testes e análise gráfica dos erros (Figura 4).

![Figura 4 — Painel de diagnóstico de resíduos.](graficos/03_residuos_regressao_simples.png)

O teste de **Shapiro-Wilk** apresentou um p-valor de **$p = 0,7987$** (estatística W = 0,9768). Como este valor é muito maior que o nível crítico de 5%, **não se rejeita a hipótese nula de normalidade**. Isso indica que os resíduos seguem uma distribuição normal, o que garante a validade da distribuição t de Student para testar as hipóteses dos coeficientes.

No entanto, o gráfico de resíduos ao longo do tempo (Figura 4b) acende um sinal de alerta: há uma tendência de resíduos consecutivos manterem o mesmo sinal (valores negativos de 1996 a 2007, positivos de 2010 a 2014 e oscilações no fim). Esse comportamento indica a presença de **autocorrelação serial** nos resíduos, muito comum em análises de séries temporais macroeconômicas. A autocorrelação não enviesa os coeficientes, mas subestima os erros padrão, o que significa que o p-valor real do modelo pode ser um pouco maior do que o reportado, sendo esta uma limitação metodológica importante.

---

## 5. Conclusões

### 5.1 Síntese e Adequação do Trabalho

Este estudo cumpriu seu objetivo principal de analisar a relação entre o PIB do agronegócio e o consumo de óleo diesel no Brasil (1996–2025). Os resultados mostram uma relação direta e estatisticamente significativa entre o crescimento real da cadeia produtiva do agro e a demanda nacional de combustível, com o PIB do agronegócio explicando **43,07%** do consumo de diesel.

O modelo linear simples estimado por MQO foi adequado para uma primeira aproximação analítica. Ele quantificou de forma simples e intuitiva que cada R$ 1 bilhão gerado pelo agronegócio exige cerca de **24,41 mil $m^3$ de diesel** adicionais ao sistema logístico e produtivo brasileiro. A normalidade dos resíduos foi validada pelo teste de Shapiro-Wilk (p = 0,7987), garantindo a confiabilidade estatística do teste t de Student.

### 5.2 Limitações do Trabalho

Apesar dos bons resultados obtidos, existem limitações econométricas importantes a serem pontuadas:
1. **Regressão Espúria e Não Estacionariedade:** Como ambas as séries possuem tendências de longo prazo, a alta correlação pode decorrer apenas do crescimento simultâneo ao longo do tempo. Seria necessário aplicar testes de raiz unitária (como ADF) e cointegração para verificar se há de fato uma relação causal de longo prazo.
2. **Autocorrelação Serial:** A análise visual de resíduos indicou que os erros não são totalmente independentes ao longo do tempo, o que afeta a precisão dos erros padrão estimados.
3. **Viés de Variável Omitida:** O modelo linear simples desconsidera outras variáveis fundamentais na dinâmica de combustíveis, tais como o preço real do óleo diesel, a frota geral de transporte do país e a eficiência média dos motores.

### 5.3 Sugestões para Trabalhos Futuros

Para contornar as limitações e expandir este trabalho, sugerem-se as seguintes abordagens em estudos futuros:
- Testar modelos **log-log** para estimar diretamente a elasticidade-renda do agronegócio sobre o consumo de diesel;
- Implementar testes de **raiz unitária (ADF)** nas séries e estimar um modelo com **primeiras diferenças** ou um Modelo de Correção de Erros (VEC) caso as séries sejam cointegradas;
- Incluir o **preço real do diesel** e a **área plantada** como variáveis explicativas em um modelo de regressão múltipla.

---

## Referências

BARROS, G. S. de C. et al. **PIB do Agronegócio Brasileiro: metodologia e estimação.** CEPEA/Esalq-USP, 2020.

CARDOSO, L. C. B.; JESUS, C. S. de. Elasticidades da Demanda por Diesel no Brasil. **Revista Brasileira de Economia**, v. 71, n. 3, p. 321-340, 2017. Disponível em: https://www.anpec.org.br/encontro/2018/submissao/files_I/i11-e00af90dec405c5d0626840b35c32359.pdf. Acesso em: 28 jul. 2026.

FUNDAÇÃO GETULIO VARGAS (FGV Agro). **Dinâmicas de Demanda e Oferta de Energia pelo Agronegócio.** São Paulo: FGV Agro, 2025. Disponível em: Relatório completo. Acesso em: 28 jul. 2026.

GASQUES, J. G. et al. Produtividade total dos fatores e transformações da agricultura brasileira: análise dos dados dos censos agropecuários. In: **A agricultura brasileira: desempenho, desafios e perspectivas.** Brasília: IPEA, 2010. p. 19-44. Disponível em: https://portalantigo.ipea.gov.br/agencia/images/stories/PDFs/livros/livros/191126_diagnostico_e_desafios_da_agricultura_brasileira.pdf. Acesso em: 28 jul. 2026.

STERN, D. I. The role of energy in economic growth. **Annals of the New York Academy of Sciences**, v. 1219, n. 1, p. 26-51, 2011.

WOOLDRIDGE, J. M. **Introductory Econometrics: A Modern Approach.** 5. ed. Mason: South-Western Cengage Learning, 2012.
