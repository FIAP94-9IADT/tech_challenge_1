# 📊 Análise Exploratória e Interpretabilidade dos Dados

## 📌 Distribuição do Diagnóstico

![Distribuição do Diagnóstico](images/diagnostico.png)

O gráfico de distribuição do diagnóstico apresenta a quantidade de amostras classificadas como:

- **0 (Benigno)**
- **1 (Maligno)**

Observa-se que há um **maior número de casos benignos em relação aos malignos**, indicando um leve desbalanceamento no dataset.

Esse fator é importante pois pode influenciar o desempenho do modelo, tornando necessário o uso de métricas além da acurácia, como:

- Precision  
- Recall  
- F1-score  

---

## 🔍 Correlação entre Variáveis

![Matriz de Correlação](images/correlacao.png)

A matriz de correlação evidencia o grau de relação entre as variáveis do dataset.

### Principais observações:

- Variáveis como **radius_mean, perimeter_mean e area_mean** apresentam **alta correlação positiva**
- Isso indica possível **redundância de informação**
- Algumas variáveis possuem correlação moderada com o diagnóstico, contribuindo para a predição

### Importância dessa análise:

- Entender dependência entre variáveis  
- Evitar multicolinearidade  
- Melhorar a interpretabilidade do modelo  

---

## 🧠 Importância das Variáveis

![Importância das Variáveis](images/importancia.png)

O gráfico de importância das variáveis, gerado a partir do modelo de árvore de decisão, mostra quais atributos mais influenciam na classificação.

### Observações relevantes:

- Uma variável se destaca significativamente com maior peso na decisão do modelo  
- Isso indica que o modelo utiliza fortemente essa característica para classificar tumores  
- Outras variáveis possuem menor impacto individual, mas ainda contribuem no conjunto  

### Benefícios dessa análise:

- Entender como o modelo toma decisões  
- Identificar quais características clínicas são mais relevantes  
- Aumentar a transparência do modelo (explicabilidade)

---

## 📈 Conclusão da Análise

A análise exploratória demonstrou que:

- O dataset possui leve desbalanceamento  
- Existem variáveis altamente correlacionadas  
- Algumas características têm forte influência na classificação  

Esses fatores reforçam a importância do pré-processamento e da escolha adequada dos modelos, garantindo melhores resultados na predição de câncer de mama.