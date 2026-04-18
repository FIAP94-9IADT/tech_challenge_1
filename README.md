# 🧠 Diabetes Prediction - Machine Learning & Deep Learning

Sistema inteligente para predição de diabetes utilizando técnicas de Machine Learning e Deep Learning.

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver modelos preditivos capazes de identificar a presença de diabetes em pacientes com base em características clínicas como:

* Número de gestações
* Pressão arterial
* Índice de massa corporal (IMC)
* Idade
* Nível de glicose

A solução utiliza tanto algoritmos clássicos de Machine Learning quanto redes neurais artificiais com TensorFlow.

---

## 🎯 Objetivo

Construir e comparar diferentes modelos de classificação para prever se um paciente possui diabetes (`Outcome = 1`) ou não (`Outcome = 0`).

---

## 🧪 Tecnologias Utilizadas

* Python 3.x
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn
* TensorFlow / Keras

---

## 📊 Dataset

O projeto utiliza o dataset **Pima Indians Diabetes Dataset**, contendo informações médicas de pacientes do sexo feminino.

### Principais colunas:

* `Pregnancies`
* `Glucose`
* `BloodPressure`
* `SkinThickness`
* `Insulin`
* `BMI`
* `DiabetesPedigreeFunction`
* `Age`
* `Outcome` (Target)

---

## ⚙️ Pipeline do Projeto

1. 📥 Carregamento dos dados
2. 🔍 Análise exploratória (EDA)
3. 🧹 Pré-processamento (limpeza e normalização)
4. ✂️ Divisão em treino e teste
5. 🤖 Treinamento dos modelos
6. 📈 Avaliação de desempenho
7. 🧠 Interpretabilidade

---

## 🤖 Modelos Utilizados

### 🔹 Machine Learning

* Regressão Logística
* Árvore de Decisão

### 🔹 Deep Learning

* Rede Neural Artificial (TensorFlow/Keras)

Arquitetura da rede neural:

* Camada densa (ReLU)
* Camada oculta (ReLU)
* Camada de saída (Sigmoid)

---

## 📊 Métricas de Avaliação

* Accuracy
* Precision
* Recall
* F1-score
* Matriz de confusão

---

## 📈 Resultados

Os modelos apresentaram boa capacidade de classificação, sendo capazes de identificar padrões relevantes nos dados.

A rede neural demonstrou melhor desempenho geral em comparação aos modelos tradicionais.

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/diabetes-prediction.git
cd diabetes-prediction
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o projeto

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
.
├── data/
│   └── diabetes.csv
├── main.py
├── requirements.txt
└── README.md
```

---

## 📌 Considerações

* O modelo não substitui diagnóstico médico.
* Deve ser utilizado como ferramenta de apoio à decisão.
* Pode ser expandido para uso em sistemas clínicos reais.

---

## 🧠 Aprendizados

* Construção de pipelines de Machine Learning
* Comparação entre modelos clássicos e redes neurais
* Pré-processamento e análise de dados
* Avaliação de modelos

---

## 👨‍💻 Autor

**Lucas Bastos Garcia**
Desenvolvedor focado em IA, segurança e sistemas inteligentes.

---

## 📄 Licença

Este projeto é de uso educacional.
