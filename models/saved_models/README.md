# Modelos Salvos

Esta pasta armazena modelos treinados.

## Arquivos:
- `*.pkl` - Modelos salvos com pickle
- `*.joblib` - Modelos salvos com joblib (recomendado)
- `*.h5` - Modelos Keras/TensorFlow
- `*.pth` / `*.pt` - Modelos PyTorch

## Uso:
```python
import joblib

# Salvar modelo
joblib.dump(model, 'models/saved_models/random_forest.joblib')

# Carregar modelo
model = joblib.load('models/saved_models/random_forest.joblib')
```

## ⚠️ Nota:
Modelos não são commitados ao Git por padrão (muito grandes).
Forneça instruções de como treinar ou link para download.
