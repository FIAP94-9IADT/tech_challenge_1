# ==============================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==============================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


# ==============================
# 1. CARREGAR O DATASET
# ==============================

df = pd.read_csv('data/diabetes.csv')

print("📊 Primeiras linhas:")
print(df.head())

print("\n📌 Colunas:")
print(df.columns)


# ==============================
# 2. PRÉ-PROCESSAMENTO
# ==============================

# Esse dataset já é numérico, mas vamos garantir
df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))

# Ver valores nulos
print("\n🔍 Valores nulos:")
print(df.isnull().sum())

# Preencher nulos (caso existam)
df = df.fillna(0)


# ==============================
# 3. TARGET (JÁ EXISTE)
# ==============================

# Aqui usamos a coluna correta
y = df['Outcome']
X = df.drop('Outcome', axis=1)

print("\n🎯 Distribuição do target:")
print(y.value_counts())


# ==============================
# 4. ANÁLISE EXPLORATÓRIA
# ==============================

sns.countplot(x=y)
plt.title("Distribuição de Diabetes (0 = Não, 1 = Sim)")
plt.show()


# ==============================
# 5. NORMALIZAÇÃO
# ==============================

scaler = StandardScaler()
X = scaler.fit_transform(X)


# ==============================
# 6. TREINO E TESTE
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# ==============================
# 7. MODELOS
# ==============================

# Regressão Logística
model1 = LogisticRegression(max_iter=1000)
model1.fit(X_train, y_train)

# Árvore de Decisão
model2 = DecisionTreeClassifier()
model2.fit(X_train, y_train)


# ==============================
# 8. AVALIAÇÃO
# ==============================

y_pred = model1.predict(X_test)

print("\n📊 Relatório de Classificação (Regressão Logística):")
print(classification_report(y_test, y_pred))


# ==============================
# 9. EXPLICABILIDADE
# ==============================

importances = model2.feature_importances_

plt.figure(figsize=(10, 6))
plt.barh(range(len(importances)), importances)
plt.title("Importância das Features")
plt.xlabel("Importância")
plt.ylabel("Features")
plt.show()


# ==============================
# FIM
# ==============================

print("\n✅ Pipeline executado com sucesso!")