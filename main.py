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
from sklearn.metrics import classification_report, confusion_matrix


# ==============================
# 1. CARREGAR O DATASET
# ==============================

df = pd.read_csv('data/breast-cancer.csv')

print("📊 Primeiras linhas:")
print(df.head())

print("\n📌 Colunas:")
print(df.columns)


# ==============================
# 2. PRÉ-PROCESSAMENTO (CORRIGIDO)
# ==============================

# ⚠️ PRIMEIRO tratar o target (antes de converter tudo!)
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Remover coluna ID se existir
if 'id' in df.columns:
    df = df.drop('id', axis=1)

# Converter restante para numérico
df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))

# Verificar nulos
print("\n🔍 Valores nulos:")
print(df.isnull().sum())

# Preencher com mediana (melhor que 0 para dados médicos)
df = df.fillna(df.median())


# ==============================
# 3. SEPARAÇÃO TARGET / FEATURES
# ==============================

y = df['diagnosis']
X = df.drop('diagnosis', axis=1)

print("\n🎯 Distribuição do target:")
print(y.value_counts())


# ==============================
# 4. ANÁLISE EXPLORATÓRIA
# ==============================

sns.countplot(x=y)
plt.title("Diagnóstico (0 = Benigno, 1 = Maligno)")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(X.corr(), cmap='coolwarm')
plt.title("Correlação entre variáveis")
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

# Regressão Logística
y_pred = model1.predict(X_test)

print("\n📊 Regressão Logística:")
print(classification_report(y_test, y_pred))
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# Árvore de Decisão
y_pred_tree = model2.predict(X_test)

print("\n🌳 Árvore de Decisão:")
print(classification_report(y_test, y_pred_tree))


# ==============================
# 9. EXPLICABILIDADE
# ==============================

importances = model2.feature_importances_

plt.figure(figsize=(10, 6))
plt.barh(range(len(importances)), importances)
plt.title("Importância das Variáveis")
plt.xlabel("Importância")
plt.ylabel("Índice das variáveis")
plt.show()


# ==============================
# FIM
# ==============================

print("\n✅ Pipeline executado com sucesso!")