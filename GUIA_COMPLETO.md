# 🚀 Guia Completo - Tech Challenge FIAP Fase 1
## Passo a Passo Detalhado para Sucesso no Projeto

---

## 📋 **SUMÁRIO**

1. [Cronograma Sugerido](#cronograma)
2. [Fase 1: Configuração](#fase-1-configuração)
3. [Fase 2: Análise Exploratória](#fase-2-eda)
4. [Fase 3: Pré-processamento](#fase-3-preprocessamento)
5. [Fase 4: Modelagem](#fase-4-modelagem)
6. [Fase 5: Avaliação](#fase-5-avaliacao)
7. [Fase 6: Explicabilidade](#fase-6-explicabilidade)
8. [Fase 7: Documentação](#fase-7-documentacao)
9. [Fase 8: Entrega](#fase-8-entrega)

---

<a name="cronograma"></a>
## 📅 **CRONOGRAMA SUGERIDO (21 DIAS)**

### **Semana 1: Setup e Exploração**
| Dia | Atividade | Tempo | Entregável |
|-----|-----------|-------|------------|
| 1 | Setup inicial | 2-3h | Ambiente configurado |
| 2-3 | EDA Parte 1 | 6-8h | Estatísticas e visualizações |
| 4-5 | EDA Parte 2 | 6-8h | Correlações e insights |
| 6-7 | Pré-processamento | 6-8h | Pipeline pronto |

### **Semana 2: Modelagem e Avaliação**
| Dia | Atividade | Tempo | Entregável |
|-----|-----------|-------|------------|
| 8-9 | Modelagem básica | 6-8h | 2+ modelos treinados |
| 10-11 | Otimização | 6-8h | Modelos otimizados |
| 12-13 | Avaliação + SHAP | 6-8h | Métricas e explicabilidade |
| 14 | EXTRA: CNN (opcional) | 4-8h | Modelo de imagem |

### **Semana 3: Documentação e Entrega**
| Dia | Atividade | Tempo | Entregável |
|-----|-----------|-------|------------|
| 15-16 | Relatório técnico | 8-10h | Relatório completo |
| 17-18 | Vídeo | 6-8h | Vídeo gravado |
| 19-20 | Revisão final | 4-6h | Tudo revisado |
| 21 | Entrega | 2-3h | Projeto submetido |

---

<a name="fase-1-configuração"></a>
## 🔧 **FASE 1: CONFIGURAÇÃO E SETUP**

### **1.1 Criar Repositório Git**

```bash
# No GitHub/GitLab, criar novo repositório
# Nome: tech-challenge-fiap-fase1

# Localmente:
cd "c:\Users\Documents\PosTech - Fiap\Tech"
git clone [URL-DO-SEU-REPO]
cd tech_challenge_fiap_oficial

# Primeira configuração
git config user.name "Seu Nome"
git config user.email "seu@email.com"

# Primeiro commit
git add .
git commit -m "Initial commit: Project structure"
git push origin main
```

### **1.2 Configurar Ambiente Python**

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Se erro de política:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Atualizar pip
python -m pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Verificar
python -c "import pandas, sklearn, shap; print('✅ OK!')"
```

### **1.3 Baixar Dataset**

**Opção 1: Kaggle (manual)**
1. https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
2. Download → Extrair → Colocar em `data/raw/`

**Opção 2: Sklearn (código)**
```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.to_csv('data/raw/breast_cancer.csv', index=False)
```

### **✅ Checklist Fase 1**
- [ ] Repositório Git criado
- [ ] Ambiente Python configurado
- [ ] Dependências instaladas
- [ ] Dataset baixado
- [ ] Estrutura de pastas criada

---

<a name="fase-2-eda"></a>
## 📊 **FASE 2: ANÁLISE EXPLORATÓRIA (EDA)**

### **2.1 Criar Notebook: `01_EDA_exploracao.ipynb`**

Vou criar um template completo que você pode copiar diretamente.

### **✅ Checklist Fase 2**
- [ ] Dataset carregado
- [ ] Estatísticas descritivas
- [ ] Valores ausentes analisados
- [ ] Outliers identificados
- [ ] Distribuições visualizadas
- [ ] Correlações calculadas
- [ ] Insights documentados
- [ ] Mínimo 10 visualizações

---

<a name="fase-3-preprocessamento"></a>
## 🧹 **FASE 3: PRÉ-PROCESSAMENTO**

### **3.1 Criar Notebook: `02_preprocessamento.ipynb`**

**Estrutura:**
1. Carregar dados
2. Separar X e y
3. Train-test split (70/30)
4. Criar pipeline de pré-processamento
5. Aplicar transformações
6. Salvar dados processados

### **✅ Checklist Fase 3**
- [ ] Dados separados (treino/teste)
- [ ] Escalonamento aplicado
- [ ] Pipeline criado
- [ ] Dados salvos
- [ ] Reprodutibilidade garantida

---

<a name="fase-4-modelagem"></a>
## 🤖 **FASE 4: MODELAGEM**

### **4.1 Criar Notebook: `03_modelagem.ipynb`**

**Modelos a Implementar (escolha 2+):**

1. **Regressão Logística**
```python
from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression(random_state=42, max_iter=1000)
model_lr.fit(X_train, y_train)
```

2. **Random Forest**
```python
from sklearn.ensemble import RandomForestClassifier

model_rf = RandomForestClassifier(
    n_estimators=100, 
    random_state=42,
    n_jobs=-1
)
model_rf.fit(X_train, y_train)
```

3. **SVM**
```python
from sklearn.svm import SVC

model_svm = SVC(
    kernel='rbf',
    random_state=42,
    probability=True
)
model_svm.fit(X_train, y_train)
```

### **✅ Checklist Fase 4**
- [ ] 2+ modelos implementados
- [ ] Modelos treinados
- [ ] Predições realizadas
- [ ] Modelos salvos

---

<a name="fase-5-avaliacao"></a>
## 📈 **FASE 5: AVALIAÇÃO**

### **5.1 Criar Notebook: `04_avaliacao.ipynb`**

**Métricas Obrigatórias:**

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, confusion_matrix, roc_auc_score, 
    roc_curve, classification_report
)

# Para cada modelo:
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
```

### **✅ Checklist Fase 5**
- [ ] Accuracy calculado
- [ ] Recall calculado
- [ ] F1-Score calculado
- [ ] Confusion Matrix criada
- [ ] ROC Curve plotada
- [ ] AUC calculado
- [ ] Comparação de modelos

---

<a name="fase-6-explicabilidade"></a>
## 🔍 **FASE 6: EXPLICABILIDADE (OBRIGATÓRIO)**

### **6.1 Criar Notebook: `05_explicabilidade.ipynb`**

**Feature Importance:**
```python
# Para modelos tree-based (Random Forest, XGBoost)
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

# Visualizar
plt.figure(figsize=(10, 8))
plt.barh(feature_importance_df['feature'][:15], 
         feature_importance_df['importance'][:15])
plt.xlabel('Importância')
plt.title('Top 15 Features Mais Importantes')
plt.tight_layout()
plt.show()
```

**SHAP Values:**
```python
import shap

# Criar explainer
explainer = shap.Explainer(model, X_train)

# Calcular SHAP values
shap_values = explainer(X_test)

# Summary plot
shap.summary_plot(shap_values, X_test, feature_names=feature_names)

# Force plot para uma predição específica
idx = 0  # Primeiro exemplo
shap.force_plot(
    explainer.expected_value, 
    shap_values.values[idx], 
    X_test.iloc[idx],
    feature_names=feature_names
)

# Dependence plot
shap.dependence_plot(
    "pior_feature",  # feature mais importante
    shap_values.values,
    X_test,
    feature_names=feature_names
)
```

### **✅ Checklist Fase 6**
- [ ] Feature Importance calculado
- [ ] SHAP instalado e configurado
- [ ] SHAP values calculados
- [ ] Summary plot criado
- [ ] Force plots criados
- [ ] Interpretação documentada

---

<a name="fase-7-documentacao"></a>
## 📝 **FASE 7: DOCUMENTAÇÃO**

### **7.1 Relatório Técnico**

**Estrutura (criar arquivo `reports/relatorio_tecnico.md`):**

```markdown
# RELATÓRIO TÉCNICO
## Tech Challenge FIAP - Fase 1

### 1. INTRODUÇÃO
[Contextualização do problema]

### 2. DADOS
- Dataset utilizado
- Fonte
- Características
- Problema de classificação

### 3. ANÁLISE EXPLORATÓRIA
#### 3.1 Estatísticas Descritivas
[Tabelas e gráficos]

#### 3.2 Principais Insights
1. Insight 1
2. Insight 2
3. Insight 3

### 4. PRÉ-PROCESSAMENTO
- Tratamento de missing values
- Normalização
- Pipeline criado

### 5. MODELAGEM
#### 5.1 Modelos Utilizados
1. Regressão Logística
2. Random Forest
3. [Outros]

#### 5.2 Justificativa das Escolhas
[Por que cada modelo foi escolhido]

### 6. RESULTADOS
#### 6.1 Métricas de Performance
[Tabela comparativa]

#### 6.2 Melhor Modelo
[Justificativa]

### 7. EXPLICABILIDADE
#### 7.1 Feature Importance
[Gráficos e discussão]

#### 7.2 SHAP Values
[Interpretação]

### 8. DISCUSSÃO CRÍTICA
#### 8.1 O modelo pode ser usado na prática?
[Discussão]

#### 8.2 Como implementar?
[Sugestões]

#### 8.3 Papel do Médico
[Enfatizar palavra final]

#### 8.4 Limitações
[Honestidade sobre limitações]

### 9. CONCLUSÕES
[Resumo e próximos passos]

### 10. REFERÊNCIAS
[Bibliografia]
```

### **7.2 Preparar Vídeo (15 minutos)**

**Roteiro:**

1. **Introdução (2 min)**
   - Apresentação da equipe
   - Contexto do problema
   - Objetivos

2. **Demonstração dos Dados (3 min)**
   - Mostrar dataset
   - Principais características
   - EDA highlights

3. **Modelagem (4 min)**
   - Modelos utilizados
   - Pipeline
   - Treinamento

4. **Resultados (4 min)**
   - Métricas
   - Comparação de modelos
   - SHAP/explicabilidade

5. **Conclusões (2 min)**
   - Principais achados
   - Aplicabilidade prática
   - Trabalhos futuros

**Dicas para gravação:**
- Use OBS Studio ou Loom
- Resolução: mínimo 720p
- Áudio limpo e claro
- Teste antes de gravar
- Upload no YouTube (unlisted)

### **✅ Checklist Fase 7**
- [ ] Relatório técnico completo
- [ ] Roteiro do vídeo pronto
- [ ] Vídeo gravado
- [ ] Vídeo editado
- [ ] Upload no YouTube/Vimeo
- [ ] Link testado

---

<a name="fase-8-entrega"></a>
## 📤 **FASE 8: ENTREGA**

### **8.1 Checklist Final**

**Repositório Git:**
- [ ] README.md completo
- [ ] Todos os notebooks funcionando
- [ ] Código comentado
- [ ] requirements.txt
- [ ] .gitignore configurado
- [ ] Dataset ou link
- [ ] Modelos salvos (opcional)

**PDF de Entrega:**
```
TECH CHALLENGE - FASE 1
Equipe: [Nomes e RMs]

Link do Repositório:
[URL do GitHub]

Link do Vídeo:
[URL do YouTube/Vimeo]

Resumo Executivo:
[2-3 parágrafos sobre o projeto]

Principais Resultados:
- Acurácia: X%
- Recall: X%
- F1-Score: X%
- Melhor Modelo: [Nome]

Dataset Utilizado:
[Nome e link]
```

### **8.2 Verificação Pré-Entrega**

Execute este checklist 24h antes da entrega:

```python
# Script de verificação
import os

checks = {
    "README.md exists": os.path.exists("README.md"),
    "requirements.txt exists": os.path.exists("requirements.txt"),
    "Notebooks exist": all([
        os.path.exists(f"notebooks/0{i}_*.ipynb") 
        for i in range(1, 6)
    ]),
    "Data folder exists": os.path.exists("data/raw"),
    "Reports folder exists": os.path.exists("reports"),
}

for check, status in checks.items():
    print(f"{'✅' if status else '❌'} {check}")
```

### **✅ Checklist Final**
- [ ] Todos notebooks executam sem erro
- [ ] Repositório organizado
- [ ] README completo
- [ ] Vídeo uploadado
- [ ] PDF de entrega pronto
- [ ] Links testados
- [ ] Prazo respeitado
- [ ] Backup feito

---

## 🎯 **DICAS DE OURO**

### **Para Nota Máxima:**

1. **Seja Crítico**
   - Discuta limitações honestamente
   - Não exagere resultados
   - Reconheça vieses

2. **Contextualize Medicamente**
   - Fale sobre implicações clínicas
   - Mencione falsos negativos/positivos
   - Discuta segurança do paciente

3. **Explique Tudo**
   - Por que escolheu cada técnica
   - Por que cada métrica é importante
   - Como interpretar resultados

4. **Organize Profissionalmente**
   - Código limpo
   - Documentação clara
   - Repositório bem estruturado

5. **Vá Além do Básico**
   - Validação cruzada
   - Otimização de hiperparâmetros
   - Análise de erros
   - SHAP bem explicado

---

## 📚 **RECURSOS ADICIONAIS**

### **Documentação:**
- Scikit-learn: https://scikit-learn.org/stable/
- SHAP: https://shap.readthedocs.io/
- Pandas: https://pandas.pydata.org/docs/

### **Tutoriais:**
- Kaggle Learn: https://www.kaggle.com/learn
- Real Python: https://realpython.com/
- Towards Data Science: https://towardsdatascience.com/

### **Papers Relevantes:**
- Buscar no Google Scholar: "breast cancer machine learning"
- Buscar: "explainable AI healthcare"

---

**Última atualização: Abril 2026**  
**FIAP - Pós Tech - IA para Desenvolvedores**

**Boa sorte! Você consegue! 🚀**
