# ==============================
# IMPORTS
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten


# ==============================
# 1. CARREGAR DATASET
# ==============================

df = pd.read_csv('data/breast-cancer.csv')

# Converter target
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Remover ID
if 'id' in df.columns:
    df = df.drop('id', axis=1)

# Converter dados
df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.median())


# ==============================
# 2. SEPARAÇÃO
# ==============================

X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Normalizar
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 🔥 MUITO IMPORTANTE (CNN precisa disso)
X = X.reshape(X.shape[0], X.shape[1], 1)


# ==============================
# 3. DIVISÃO
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# 4. MODELO CNN
# ==============================

model = Sequential()

# Camada convolucional
model.add(Conv1D(filters=32, kernel_size=2, activation='relu', input_shape=(X.shape[1], 1)))

# Achatar
model.add(Flatten())

# Camadas densas
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)


# ==============================
# 5. TREINAMENTO
# ==============================

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=10,
    validation_split=0.2
)


# ==============================
# 6. AVALIAÇÃO
# ==============================

loss, acc = model.evaluate(X_test, y_test)

print("Accuracy:", acc)


# ==============================
# 7. PREVISÃO
# ==============================

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)


print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


# ==============================
# 8. GRÁFICO
# ==============================

plt.plot(history.history['accuracy'], label='Treino')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.legend()
plt.title("CNN - Acurácia")
plt.show()