# ✅ Checklist Completo - Tech Challenge FIAP Fase 1

## 📋 REQUISITOS OBRIGATÓRIOS

### 1️⃣ **Escolha e Discussão de Dataset** ✓

- [ ] Dataset escolhido relacionado à saúde/segurança feminina
- [ ] Dataset público e acessível
- [ ] Problema bem definido (classificação)
- [ ] Discussão sobre relevância do problema
- [ ] Contextualização médica adequada

**Datasets Sugeridos pela FIAP:**
- [ ] Breast Cancer Wisconsin (Recomendado)
- [ ] PCOS Dataset
- [ ] Outro dataset relevante

---

### 2️⃣ **Exploração de Dados (EDA)** ✓

#### Carregamento e Visão Geral
- [ ] Dataset carregado com sucesso
- [ ] Dimensões do dataset documentadas (linhas x colunas)
- [ ] Tipos de dados identificados
- [ ] Primeiras e últimas linhas visualizadas

#### Análise Descritiva
- [ ] Estatísticas descritivas calculadas (média, mediana, std, min, max)
- [ ] Distribuição das variáveis analisada
- [ ] Distribuição da variável target analisada
- [ ] Balanceamento de classes verificado

#### Valores Ausentes
- [ ] Valores ausentes identificados
- [ ] Percentual de missing por coluna calculado
- [ ] Visualização de valores ausentes
- [ ] Estratégia de tratamento definida

#### Outliers
- [ ] Outliers identificados (boxplot, IQR, Z-score)
- [ ] Análise de impacto dos outliers
- [ ] Decisão sobre tratamento documentada

#### Correlações
- [ ] Matriz de correlação calculada
- [ ] Heatmap de correlação criado
- [ ] Correlações fortes identificadas
- [ ] Multicolinearidade verificada

#### Visualizações
- [ ] Histogramas das variáveis numéricas
- [ ] Boxplots para identificar outliers
- [ ] Gráficos de distribuição da variável target
- [ ] Pairplots ou scatter plots relevantes
- [ ] Mínimo 8-10 visualizações diferentes

#### Discussão
- [ ] Padrões identificados e discutidos
- [ ] Anomalias documentadas
- [ ] Insights relevantes para saúde feminina
- [ ] Hipóteses levantadas

---

### 3️⃣ **Pré-processamento de Dados** ✓

#### Limpeza
- [ ] Valores ausentes tratados (imputação, remoção, etc.)
- [ ] Duplicatas removidas (se existirem)
- [ ] Inconsistências corrigidas
- [ ] Estratégias de limpeza justificadas

#### Pipeline de Pré-processamento
- [ ] Pipeline criado em Python
- [ ] Pipeline documentado e reproduzível
- [ ] Transformações aplicadas de forma consistente
- [ ] Pipeline salvo para reutilização

#### Transformação de Variáveis
- [ ] Variáveis categóricas convertidas (One-Hot, Label Encoding)
- [ ] Variáveis numéricas normalizadas/padronizadas
- [ ] Feature Engineering realizado (se aplicável)
- [ ] Scaling aplicado quando necessário

#### Análise de Correlação
- [ ] Correlação entre features e target analisada
- [ ] Features altamente correlacionadas identificadas
- [ ] Decisões sobre seleção de features documentadas

#### Separação de Dados
- [ ] Dados divididos em treino e teste (70/30 ou 80/20)
- [ ] Estratificação aplicada (se necessário)
- [ ] Validação cruzada planejada
- [ ] Seed fixado para reprodutibilidade

---

### 4️⃣ **Modelagem** ✓

#### Escolha de Modelos
- [ ] **Mínimo 2 algoritmos** selecionados
- [ ] Justificativa da escolha de cada algoritmo
- [ ] Algoritmos adequados para classificação

**Modelos Implementados:**
- [ ] Modelo 1: _______________
- [ ] Modelo 2: _______________
- [ ] Modelo 3: _______________ (opcional)
- [ ] Modelo 4: _______________ (opcional)

#### Implementação
- [ ] Código limpo e organizado
- [ ] Parâmetros iniciais definidos
- [ ] Reprodutibilidade garantida (random_state)
- [ ] Comentários explicativos no código

#### Treinamento
- [ ] Modelos treinados com dados de treino
- [ ] Tempo de treinamento registrado
- [ ] Convergência verificada
- [ ] Modelos salvos

---

### 5️⃣ **Avaliação de Modelos** ✓

#### Métricas Obrigatórias
- [ ] **Accuracy** calculado
- [ ] **Recall** calculado
- [ ] **F1-Score** calculado
- [ ] **Precision** calculado (opcional mas recomendado)
- [ ] **Confusion Matrix** criada
- [ ] **ROC Curve** plotada
- [ ] **AUC Score** calculado

#### Discussão de Métricas
- [ ] Escolha da métrica principal justificada
- [ ] Consideração do contexto médico na escolha
- [ ] Trade-off entre precisão e recall discutido
- [ ] Importância de Recall (sensibilidade) em diagnóstico médico explicada

#### Comparação de Modelos
- [ ] Tabela comparativa de performance
- [ ] Visualização de comparação (gráficos)
- [ ] Melhor modelo identificado
- [ ] Critérios de seleção documentados

#### Validação Cruzada
- [ ] Cross-validation aplicada (k-fold)
- [ ] Média e desvio padrão das métricas
- [ ] Overfitting/Underfitting analisado

---

### 6️⃣ **Explicabilidade (OBRIGATÓRIO)** ✓

#### Feature Importance
- [ ] Feature Importance calculado
- [ ] Gráfico de importância de features
- [ ] Top features mais importantes identificadas
- [ ] Interpretação das features importantes

#### SHAP Values
- [ ] SHAP instalado e configurado
- [ ] SHAP values calculados
- [ ] Summary plot criado
- [ ] Force plot para exemplos específicos
- [ ] Dependence plots para features importantes
- [ ] Interpretação dos SHAP values

#### Interpretabilidade
- [ ] Explicação de como o modelo toma decisões
- [ ] Exemplos de predições explicadas
- [ ] Limitações do modelo documentadas
- [ ] Casos de uso prático discutidos

---

### 7️⃣ **Discussão Crítica** ✓

#### Análise de Resultados
- [ ] Resultados interpretados no contexto médico
- [ ] Limitações do modelo identificadas
- [ ] Riscos e considerações éticas discutidos
- [ ] Comparação com literatura médica (se aplicável)

#### Aplicabilidade Prática
- [ ] **Discussão: O modelo pode ser usado na prática?**
- [ ] **Como implementar na rotina médica?**
- [ ] **Papel do médico na decisão final enfatizado**
- [ ] Cenários de uso sugeridos
- [ ] Fluxo de trabalho proposto

#### Limitações
- [ ] Limitações do dataset documentadas
- [ ] Vieses identificados
- [ ] Generalização do modelo discutida
- [ ] Necessidade de validação clínica mencionada

---

### 8️⃣ **Código e Organização** ✓

#### Estrutura do Projeto
- [ ] Estrutura de pastas organizada
- [ ] README.md completo e informativo
- [ ] requirements.txt com todas dependências
- [ ] .gitignore configurado

#### Qualidade do Código
- [ ] Código limpo e legível
- [ ] Comentários explicativos
- [ ] Funções modulares e reutilizáveis
- [ ] Convenções de nomenclatura seguidas
- [ ] PEP 8 respeitado (ou formatado com Black)

#### Notebooks
- [ ] Notebooks executam sem erros
- [ ] Células organizadas logicamente
- [ ] Markdown explicativo entre células de código
- [ ] Outputs preservados
- [ ] Numeração e títulos claros

#### Reprodutibilidade
- [ ] Seeds fixados (random_state)
- [ ] Versões de bibliotecas documentadas
- [ ] Instruções de execução claras
- [ ] Dados acessíveis ou link fornecido

---

### 9️⃣ **Repositório Git** ✓

#### Estrutura do Repositório
- [ ] Repositório criado (GitHub, GitLab, Bitbucket)
- [ ] README.md na raiz do repositório
- [ ] Estrutura de pastas organizada
- [ ] .gitignore configurado

#### Conteúdo do Repositório
- [ ] Código-fonte completo
- [ ] Notebooks Jupyter
- [ ] Scripts Python (se aplicável)
- [ ] requirements.txt
- [ ] Dockerfile (se usar Docker)
- [ ] Dataset ou link para download
- [ ] Modelos treinados (ou instruções para treinar)

#### Documentação
- [ ] README com instruções de instalação
- [ ] README com instruções de execução
- [ ] Descrição do problema
- [ ] Descrição da solução
- [ ] Resultados principais documentados

#### Resultados
- [ ] Prints de resultados salvos
- [ ] Gráficos salvos em alta resolução
- [ ] Métricas documentadas
- [ ] Relatório técnico incluído

---

### 🔟 **Relatório Técnico** ✓

#### Estrutura do Relatório
- [ ] Introdução e contextualização
- [ ] Descrição do problema
- [ ] Revisão de literatura (breve)
- [ ] Metodologia

#### Conteúdo Obrigatório

**Análise Exploratória**
- [ ] Discussão dos dados
- [ ] Visualizações principais
- [ ] Insights identificados
- [ ] Desafios encontrados

**Pré-processamento**
- [ ] Estratégias aplicadas
- [ ] Justificativas das escolhas
- [ ] Transformações realizadas
- [ ] Pipeline descrito

**Modelagem**
- [ ] Modelos utilizados
- [ ] Justificativa da escolha
- [ ] Hiperparâmetros utilizados
- [ ] Processo de treinamento

**Resultados**
- [ ] Métricas de todos os modelos
- [ ] Comparação de performance
- [ ] Melhor modelo identificado
- [ ] Explicabilidade (SHAP, Feature Importance)

**Interpretação**
- [ ] Análise crítica dos resultados
- [ ] Aplicabilidade prática
- [ ] Limitações
- [ ] Considerações éticas

**Conclusões**
- [ ] Resumo dos principais achados
- [ ] Contribuições do trabalho
- [ ] Trabalhos futuros
- [ ] Recomendações

---

### 1️⃣1️⃣ **Vídeo de Demonstração** ✓

#### Especificações Técnicas
- [ ] Duração: **Máximo 15 minutos**
- [ ] Upload no YouTube ou Vimeo
- [ ] Link público ou não listado
- [ ] Qualidade de áudio adequada
- [ ] Qualidade de vídeo adequada (mínimo 720p)

#### Conteúdo do Vídeo

**Introdução (1-2 min)**
- [ ] Apresentação da equipe
- [ ] Contextualização do problema
- [ ] Objetivos do projeto

**Demonstração (8-10 min)**
- [ ] Demonstração do sistema em execução
- [ ] Carregamento e exploração dos dados
- [ ] Processo de modelagem
- [ ] Resultados obtidos
- [ ] Explicabilidade (SHAP)
- [ ] Fluxo completo end-to-end

**Conclusões (2-3 min)**
- [ ] Principais resultados
- [ ] Discussão crítica
- [ ] Aplicabilidade prática
- [ ] Trabalhos futuros

#### Apresentação
- [ ] Slides de apoio (se necessário)
- [ ] Narração clara e objetiva
- [ ] Demonstração técnica fluida
- [ ] Tempo respeitado (máx 15 min)

---

## 🌟 EXTRAS (OPCIONAIS - Podem Aumentar a Nota)

### ⭐ **Visão Computacional com CNN**

#### Implementação
- [ ] Dataset de imagens baixado (CBIS-DDSM)
- [ ] Pré-processamento de imagens
- [ ] Augmentation de dados
- [ ] CNN implementada (TensorFlow/Keras ou PyTorch)
- [ ] Transfer Learning aplicado (opcional)

#### Treinamento
- [ ] Modelo treinado com sucesso
- [ ] Early stopping aplicado
- [ ] Checkpoints salvos
- [ ] Training history visualizado

#### Avaliação
- [ ] Métricas calculadas (Accuracy, Precision, Recall, F1)
- [ ] Confusion Matrix
- [ ] Visualização de predições
- [ ] Grad-CAM ou técnica de visualização (opcional)

#### Comparação
- [ ] Comparação com modelo tabular
- [ ] Discussão de vantagens/desvantagens
- [ ] Aplicabilidade de cada abordagem

---

### ⭐ **Melhorias Adicionais**

#### Otimização de Hiperparâmetros
- [ ] Grid Search ou Random Search
- [ ] Optuna/Hyperopt implementado
- [ ] Melhores parâmetros documentados

#### Ensemble Methods
- [ ] Voting Classifier
- [ ] Stacking
- [ ] Blending

#### Balanceamento de Classes
- [ ] SMOTE aplicado
- [ ] Undersampling/Oversampling
- [ ] Class weights ajustados

#### Deploy
- [ ] API REST criada (FastAPI/Flask)
- [ ] Interface web (Streamlit)
- [ ] Containerização (Docker)

---

## 📊 **Checklist de Qualidade**

### Antes de Entregar

#### Revisão Técnica
- [ ] Todos os notebooks executam sem erros
- [ ] Todos os requisitos obrigatórios atendidos
- [ ] Código revisado e testado
- [ ] Resultados validados

#### Documentação
- [ ] README completo e claro
- [ ] Relatório técnico finalizado
- [ ] Comentários no código
- [ ] Referências bibliográficas

#### Entregas
- [ ] Repositório Git público/acessível
- [ ] Vídeo gravado e uploadado
- [ ] PDF com link do repo e vídeo
- [ ] Todos os arquivos organizados

#### Revisão Final
- [ ] Ortografia e gramática revisadas
- [ ] Gráficos em alta qualidade
- [ ] Formatação consistente
- [ ] Prazo de entrega respeitado

---

## 🎯 **Pontuação Estimada**

| Critério | Peso | Status | Notas |
|----------|------|--------|-------|
| Exploração de Dados | 20% | ☐ | |
| Pré-processamento | 15% | ☐ | |
| Modelagem | 25% | ☐ | |
| Avaliação + Explicabilidade | 20% | ☐ | |
| Código e Organização | 10% | ☐ | |
| Relatório e Vídeo | 10% | ☐ | |
| **EXTRA**: CNN | +10% | ☐ | Opcional |

---

## ✅ **Status Geral do Projeto**

- [ ] 🔴 Não iniciado
- [ ] 🟡 Em andamento
- [ ] 🟢 Completo
- [ ] ✅ Revisado e pronto para entrega

---

**Data de Início**: ___/___/___  
**Data de Entrega**: ___/___/___  
**Dias Restantes**: ___

---

**Lembre-se**: Este projeto vale **90% da nota de TODAS as disciplinas da fase!**

**Dedique tempo adequado e organize-se bem! 🚀**
