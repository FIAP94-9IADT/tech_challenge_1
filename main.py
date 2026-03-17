# =========================
# IMPORTAÇÃO DAS BIBLIOTECAS
# =========================
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# =========================
# 1. CARREGAMENTO DOS DADOS
# =========================
# Dataset já pronto do sklearn
data = load_breast_cancer()

# Criando DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# 0 = maligno | 1 = benigno
print("\n📊 Primeiras linhas:")
print(df.head())


# =========================
# 2. EXPLORAÇÃO DOS DADOS
# =========================
print("\n📈 Estatísticas:")
print(df.describe())

print("\n🔍 Valores nulos:")
print(df.isnull().sum())


# =========================
# 3. PRÉ-PROCESSAMENTO
# =========================
X = df.drop('target', axis=1)
y = df['target']

# Separação treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalização
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# =========================
# 4. MODELAGEM
# =========================

# Modelo 1: Regressão Logística
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)

# Modelo 2: Árvore de Decisão
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train, y_train)


# =========================
# 5. AVALIAÇÃO
# =========================

# Previsões
y_pred_lr = model_lr.predict(X_test)
y_pred_dt = model_dt.predict(X_test)

print("\n📊 RESULTADOS - REGRESSÃO LOGÍSTICA")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

print("\n📊 RESULTADOS - ÁRVORE DE DECISÃO")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))


# =========================
# 6. INTERPRETAÇÃO (FEATURE IMPORTANCE)
# =========================

importances = model_dt.feature_importances_
features = pd.Series(importances, index=data.feature_names)

print("\n🔥 Importância das Features:")
print(features.sort_values(ascending=False).head(10))