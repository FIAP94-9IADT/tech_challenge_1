# ==============================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ==============================
# 1. CARREGAR DATASET
# ==============================

df = pd.read_csv('data/diabetes.csv')

print("📊 Primeiras linhas:")
print(df.head())

print("\n📌 Colunas:")
print(df.columns)


# ==============================
# 2. ANÁLISE EXPLORATÓRIA
# ==============================

# Distribuição do target
sns.countplot(x='Outcome', data=df)
plt.title("Distribuição de Diabetes (0 = Não, 1 = Sim)")
plt.show()

# Correlação
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlação entre variáveis")
plt.show()


# ==============================
# 3. PRÉ-PROCESSAMENTO
# ==============================

# Separar variáveis
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Normalização
scaler = StandardScaler()
X = scaler.fit_transform(X)


# ==============================
# 4. DIVISÃO DOS DADOS
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# ==============================
# 5. CRIAR MODELO (REDE NEURAL)
# ==============================

model = Sequential()

# Camada de entrada + oculta
model.add(Dense(16, input_dim=X.shape[1], activation='relu'))

# Camada oculta
model.add(Dense(8, activation='relu'))

# Saída (classificação binária)
model.add(Dense(1, activation='sigmoid'))


# ==============================
# 6. COMPILAR MODELO
# ==============================

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)


# ==============================
# 7. TREINAMENTO
# ==============================

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=10,
    validation_split=0.2,
    verbose=1
)


# ==============================
# 8. AVALIAÇÃO
# ==============================

loss, accuracy = model.evaluate(X_test, y_test)

print(f"\n📊 Loss: {loss}")
print(f"📊 Accuracy: {accuracy}")


# ==============================
# 9. PREVISÕES
# ==============================

y_pred = model.predict(X_test)

# Converter probabilidades para 0 ou 1
y_pred = (y_pred > 0.5).astype(int)


# ==============================
# 10. MATRIZ DE CONFUSÃO
# ==============================

from sklearn.metrics import confusion_matrix, classification_report

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ==============================
# 11. GRÁFICO DE TREINAMENTO
# ==============================

plt.plot(history.history['accuracy'], label='Treino')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.title('Acurácia do Modelo')
plt.legend()
plt.show()


# ==============================
# FIM
# ==============================

print("\n✅ Pipeline executado com sucesso!")