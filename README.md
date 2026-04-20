# 🏥 Tech Challenge FIAP - Fase 1
## Sistema Inteligente de Suporte ao Diagnóstico - Saúde da Mulher

---

## 📋 Informações do Projeto

**Instituição**: FIAP - Faculdade de Informática e Administração Paulista  
**Curso**: Pós-Graduação Tech - Inteligência Artificial para Desenvolvedores  
**Fase**: 1  
**Peso**: 90% da nota de todas as disciplinas  
**Tipo**: Projeto em Grupo  
**Prazo**: [Inserir data de entrega]

### 👥 Equipe
- **Aluno 1**: [Nome] - RM: [RM]
- **Aluno 2**: [Nome] - RM: [RM]
- **Aluno 3**: [Nome] - RM: [RM]
- **Aluno 4**: [Nome] - RM: [RM]

---

## 🎯 Desafio

Uma rede de hospitais e centros de saúde especializados no atendimento à mulher busca implementar um **sistema inteligente de suporte ao diagnóstico e detecção de riscos**, capaz de ajudar profissionais de saúde na identificação precoce de condições que afetam a segurança e saúde feminina.

### 🔍 Contexto

Com um volume crescente de pacientes e a necessidade de identificar rapidamente situações de risco, desde doenças como **câncer de mama** até sinais de **violência doméstica** em prontuários médicos, a instituição precisa de soluções que:

- ✅ Acelerem a triagem
- ✅ Apoiem as decisões médicas
- ✅ Garantam um atendimento mais seguro e eficaz

### 🎯 Objetivo da Fase 1

Construir uma **solução inicial com foco em IA** para processamento de dados médicos relacionados à saúde e segurança da mulher, aplicando fundamentos essenciais de:
- Inteligência Artificial
- Machine Learning
- Visão Computacional (EXTRA)

---

## 📊 Estrutura do Projeto

```
tech_challenge_fiap_oficial/
│
├── 📄 README.md                          # Este arquivo
├── 📄 GUIA_COMPLETO.md                   # Guia passo a passo detalhado
├── 📄 REQUISITOS_FIAP.md                 # Checklist de requisitos
├── 📄 requirements.txt                   # Dependências Python
├── 📄 .gitignore                         # Arquivos ignorados
│
├── 📂 data/
│   ├── 📂 raw/                          # Dados originais
│   ├── 📂 processed/                    # Dados processados
│   └── 📄 DATA_SOURCES.md               # Fontes de dados
│
├── 📂 notebooks/
│   ├── 📓 01_EDA_exploracao.ipynb       # Análise Exploratória
│   ├── 📓 02_preprocessamento.ipynb     # Pré-processamento
│   ├── 📓 03_modelagem.ipynb            # Modelagem ML
│   ├── 📓 04_avaliacao.ipynb            # Avaliação e Métricas
│   ├── 📓 05_explicabilidade.ipynb      # SHAP e Feature Importance
│   └── 📓 EXTRA_visao_computacional.ipynb  # CNN (Opcional)
│
├── 📂 src/
│   ├── 🐍 __init__.py
│   ├── 🐍 data_loader.py               # Carregamento de dados
│   ├── 🐍 preprocessing.py             # Pré-processamento
│   ├── 🐍 models.py                    # Modelos ML
│   ├── 🐍 evaluation.py                # Métricas e avaliação
│   ├── 🐍 explainability.py            # SHAP e interpretabilidade
│   └── 🐍 visualization.py             # Visualizações
│
├── 📂 models/
│   └── 📂 saved_models/                # Modelos treinados salvos
│
├── 📂 reports/
│   ├── 📂 figures/                     # Gráficos e visualizações
│   ├── 📄 relatorio_tecnico.md         # Relatório técnico
│   └── 📄 apresentacao.pptx            # Slides da apresentação
│
├── 📂 docker/
│   ├── 📄 Dockerfile                   # Containerização (opcional)
│   └── 📄 docker-compose.yml
│
└── 📂 docs/
    ├── 📄 video_instrucoes.md          # Instruções para o vídeo
    └── 📄 referencias.md               # Referências bibliográficas
```

---

## 🎓 Disciplinas e Conteúdos Aplicados

### **Machine Learning**
- ✅ Aula 1: Conceitos básicos e aplicações
- ✅ Aula 2: Regressão linear e métricas de validação
- ✅ Aula 3: Redução de dimensionalidade
- ✅ Aula 4: Feature Scaling

### **Machine Learning Avançado**
- ✅ Aula 1: Modelos de Classificação
- ✅ Aula 2: KNN, SVM
- ✅ Aula 3: K-means
- ✅ Aula 4: Modelos Baseados em Árvores
- ✅ Aula 5: Validação Cruzada e Pipeline no Sklearn
- ✅ Aula 6: Classification report e métricas de classificação
- ✅ Aula 7: AUC score e ROC Curve

---

## 📦 Entregas Técnicas Obrigatórias

### ✅ **1. Processamento de Dados Médicos**

**Classificação com Machine Learning (OBRIGATÓRIO)**
- Escolher base de dados relacionada à saúde feminina
- Realizar classificação de riscos/diagnósticos
- Usar algoritmos de aprendizado de máquina

**Visão Computacional com CNN (EXTRA - Opcional)**
- Diagnóstico com dados de imagem
- Mamografias, ultrassons
- Redes Neurais Convolucionais (CNN)
- **Pode aumentar sua nota** se não atingir pontuação máxima

---

### 📊 **2. Dados e Modelos**

#### **Escolha de Dataset**
- Um ou mais datasets públicos
- Relacionados à segurança e saúde da mulher
- Discussão do problema a ser resolvido

**Datasets Sugeridos pela FIAP:**

**Opção 1: Câncer de Mama (RECOMENDADO)**
```
Dataset: Breast Cancer Wisconsin
Link: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
Problema: Diagnóstico (Maligno ou Benigno)
Tipo: Classificação Binária
Variáveis: 30 features numéricas
```

**Opção 2: Síndrome dos Ovários Policísticos (PCOS)**
```
Dataset: PCOS Dataset
Link: https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos
Problema: Detecção de SOP
Tipo: Classificação Binária
```

**Opção 3: Outro Dataset de Sua Preferência**
- Deve estar relacionado à saúde/segurança feminina
- Deve permitir classificação

**EXTRA - Visão Computacional:**
```
Dataset: CBIS-DDSM Breast Cancer
Link: https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset
Tipo: Imagens de mamografias
Técnica: CNN (Convolutional Neural Networks)
```

---

### 🔍 **3. Exploração de Dados (EDA)**

**Requisitos:**
- [ ] Carregar a base de dados
- [ ] Explorar características do dataset
- [ ] Analisar estatísticas descritivas
- [ ] Visualizar distribuições relevantes
- [ ] **Discutir os resultados**
- [ ] Identificar padrões específicos relacionados à saúde feminina

**Análises Esperadas:**
- Distribuição das variáveis
- Análise de valores ausentes
- Identificação de outliers
- Correlação entre variáveis
- Balanceamento de classes

---

### 🧹 **4. Pré-processamento de Dados**

**Requisitos:**
- [ ] Limpeza dos dados
- [ ] Tratamento de valores ausentes
- [ ] Tratamento de inconsistências (se necessário)
- [ ] **Pipeline de pré-processamento em Python**
- [ ] Conversão de variáveis categóricas
- [ ] Conversão de variáveis numéricas
- [ ] Formatos adequados para modelagem
- [ ] **Análise de correlação**

**Técnicas a Considerar:**
- Imputação de valores ausentes
- Normalização/Padronização
- Encoding de variáveis categóricas
- Feature Engineering (se aplicável)
- Balanceamento de classes (se necessário)

---

### 🤖 **5. Modelagem**

**Requisitos:**
- [ ] Criar modelos preditivos de classificação
- [ ] Utilizar **DUAS OU MAIS técnicas**
- [ ] Separação clara entre treino e teste

**Algoritmos Sugeridos (escolha 2+):**
- ✅ Regressão Logística
- ✅ Árvore de Decisão (Decision Tree)
- ✅ Random Forest
- ✅ KNN (K-Nearest Neighbors)
- ✅ SVM (Support Vector Machine)
- ✅ Gradient Boosting (XGBoost, LightGBM)
- ✅ Naive Bayes

**Estrutura:**
```python
# Separação treino/teste (70/30 ou 80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Treinar múltiplos modelos
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Treinar e avaliar cada modelo
for name, model in models.items():
    model.fit(X_train, y_train)
    # Avaliar...
```

---

### 📈 **6. Treinamento e Avaliação**

**Requisitos:**
- [ ] Treinar modelo com conjunto de treinamento
- [ ] Avaliar com dados de teste
- [ ] Usar métricas adequadas:
  - **Accuracy**
  - **Recall**
  - **F1-Score**
  - Precision
  - Confusion Matrix
  - ROC Curve e AUC
- [ ] **Discutir escolha da métrica** considerando o problema
- [ ] **Interpretação dos resultados**
- [ ] **Explicabilidade da previsão**:
  - Feature Importance
  - SHAP values
- [ ] **Discussão crítica dos resultados**

**Perguntas a Responder:**
1. ❓ O modelo pode ser utilizado na prática?
2. ❓ Como implementar na rotina médica?
3. ❓ Quais as limitações do modelo?
4. ❓ Como garantir que o médico tenha a palavra final?

---

## 📤 Entregáveis da Fase 1

### 📄 **1. Arquivo PDF com:**

#### **A. Link do Repositório Git**
Contendo:
- ✅ Código-fonte completo
- ✅ README.md com instruções de execução
- ✅ Dockerfile (se usar Docker)
- ✅ Dataset ou link para download
- ✅ Resultados obtidos (prints, gráficos, análises)

#### **B. Relatório Técnico**
Explicando:
- ✅ Discussões da análise exploratória
- ✅ Estratégias de pré-processamento
- ✅ Modelos usados e por quê
- ✅ Resultados e interpretação dos dados

---

### 🎥 **2. Vídeo de Demonstração**

**Especificações:**
- 📹 Upload no YouTube ou Vimeo (público ou não listado)
- ⏱️ Duração: **Até 15 minutos**
- 🎬 Conteúdo:
  - Demonstração do sistema em execução
  - Breve explicação do fluxo
  - Principais resultados
  - Conclusões

**Estrutura Sugerida (15 min):**
1. Introdução (1 min)
2. Contexto e problema (2 min)
3. Dados e exploração (3 min)
4. Modelagem (3 min)
5. Resultados (4 min)
6. Conclusões e próximos passos (2 min)

---

## 🛠️ Tecnologias e Bibliotecas

### **Essenciais (Obrigatórias)**
```python
# Manipulação de Dados
pandas
numpy

# Visualização
matplotlib
seaborn
plotly

# Machine Learning
scikit-learn

# Explicabilidade
shap

# Jupyter
jupyter
notebook
```

### **Para Visão Computacional (EXTRA)**
```python
# Deep Learning
tensorflow
keras
# ou
pytorch
torchvision

# Processamento de Imagem
opencv-python
pillow
```

### **Utilitários**
```python
# Otimização de hiperparâmetros
optuna

# Salvamento de modelos
joblib
pickle

# Geração de relatórios
papermill
```

---

## 🚀 Como Executar o Projeto

### **1. Clonar o Repositório**
```bash
git clone [url-do-repositorio]
cd tech_challenge_fiap_oficial
```

### **2. Criar Ambiente Virtual**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### **3. Instalar Dependências**
```powershell
pip install -r requirements.txt
```

### **4. Baixar Dataset**
- Acesse o Kaggle
- Baixe o dataset escolhido
- Coloque em `data/raw/`

### **5. Executar Notebooks**
```powershell
jupyter notebook
```

Abra os notebooks na ordem:
1. `01_EDA_exploracao.ipynb`
2. `02_preprocessamento.ipynb`
3. `03_modelagem.ipynb`
4. `04_avaliacao.ipynb`
5. `05_explicabilidade.ipynb`

---

## 📊 Critérios de Avaliação

### **1. Exploração de Dados (20%)**
- Análise completa e bem documentada
- Visualizações relevantes
- Identificação de padrões

### **2. Pré-processamento (15%)**
- Pipeline bem estruturado
- Tratamento adequado de dados
- Justificativas das escolhas

### **3. Modelagem (25%)**
- Uso de 2+ algoritmos
- Implementação correta
- Comparação entre modelos

### **4. Avaliação (20%)**
- Métricas apropriadas
- Discussão crítica
- Explicabilidade (SHAP, Feature Importance)

### **5. Código e Organização (10%)**
- Código limpo e documentado
- Estrutura organizada
- Reprodutibilidade

### **6. Relatório e Apresentação (10%)**
- Clareza na comunicação
- Qualidade do vídeo
- Documentação completa

### **EXTRA: Visão Computacional (+10%)**
- Implementação de CNN
- Resultados com imagens
- Comparação com modelo tabular

---

## 💡 Dicas Importantes

### ✅ **Faça:**
1. Escolha um problema claro e bem definido
2. Documente TUDO (código, decisões, resultados)
3. Discuta os resultados de forma CRÍTICA
4. Enfatize que o médico tem a palavra final
5. Use validação cruzada
6. Teste múltiplos algoritmos
7. Apresente explicabilidade (SHAP)
8. Organize o código profissionalmente

### ❌ **Evite:**
1. Pular a análise exploratória
2. Não tratar dados ausentes
3. Usar apenas um modelo
4. Ignorar desbalanceamento de classes
5. Não justificar escolhas
6. Código desorganizado
7. Falta de discussão crítica
8. Overfitting sem detectar

---

## 🎯 Próximos Passos

1. [ ] Ler completamente o `GUIA_COMPLETO.md`
2. [ ] Escolher dataset (Breast Cancer recomendado)
3. [ ] Configurar ambiente
4. [ ] Seguir os notebooks na ordem
5. [ ] Documentar durante todo o processo
6. [ ] Preparar relatório técnico
7. [ ] Gravar vídeo de demonstração
8. [ ] Revisar entregas
9. [ ] Submeter no prazo!

---

## 📚 Referências

### **Documentação Oficial**
- Scikit-learn: https://scikit-learn.org/
- SHAP: https://shap.readthedocs.io/
- Pandas: https://pandas.pydata.org/
- Seaborn: https://seaborn.pydata.org/

### **Artigos e Papers**
- [Adicionar artigos relevantes sobre saúde feminina e ML]
- [Papers sobre interpretabilidade em ML médico]

### **Datasets**
- Kaggle: https://www.kaggle.com/
- UCI ML Repository: https://archive.ics.uci.edu/ml/

---

## 📞 Contato da Equipe

**Aluno 1**: [email]  
**Aluno 2**: [email]  
**Aluno 3**: [email]  
**Aluno 4**: [email]

**Repositório**: [URL do GitHub]  
**Vídeo**: [URL do YouTube/Vimeo]

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do Tech Challenge da FIAP - Fase 1.

---

**🏥 Lembrando: O objetivo é criar uma ferramenta de APOIO à decisão médica, NUNCA substituir o profissional de saúde!**

---

*Última atualização: Abril 2026*  
*FIAP - Pós-Graduação Tech - IA para Desenvolvedores*
