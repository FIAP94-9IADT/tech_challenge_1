🧠 Breast Cancer Prediction - Machine Learning & Deep Learning

Sistema inteligente para predição de câncer de mama utilizando técnicas de Machine Learning, Deep Learning e visão computacional.

📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver modelos preditivos capazes de identificar tumores como benignos ou malignos, com base em dados clínicos e características extraídas de exames médicos.

A solução combina algoritmos clássicos de Machine Learning com redes neurais artificiais, além de explorar conceitos de visão computacional.

🎯 Objetivo

Construir modelos de classificação para prever:

diagnosis = 1 → Tumor maligno
diagnosis = 0 → Tumor benigno
🧪 Tecnologias Utilizadas
Python 3.x
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
TensorFlow / Keras
📊 Dataset

Dataset utilizado: Breast Cancer Dataset

Principais características:
Radius (raio do tumor)
Texture (textura)
Perimeter (perímetro)
Area (área)
Smoothness (suavidade)
Compactness
Concavity
Symmetry
Target:
diagnosis
M → Maligno (1)
B → Benigno (0)
⚙️ Pipeline do Projeto
📥 Carregamento dos dados
🔍 Análise exploratória (EDA)
🧹 Pré-processamento (limpeza e normalização)
✂️ Divisão em treino e teste
🤖 Treinamento dos modelos
📈 Avaliação de desempenho
🧠 Interpretabilidade
🤖 Modelos Utilizados
🔹 Machine Learning
Regressão Logística
Árvore de Decisão
🔹 Deep Learning
Rede Neural Artificial (TensorFlow/Keras)

Arquitetura:

Camada densa (ReLU)
Camada oculta (ReLU)
Camada de saída (Sigmoid)
🖼️ Visão Computacional

O projeto também explora conceitos de visão computacional aplicados à detecção de câncer de mama.

Foram utilizadas:

Redes Neurais Convolucionais (CNN)
Classificação de imagens médicas (benigno vs maligno)

Essa abordagem permite identificar padrões visuais em exames, simulando aplicações reais na área da saúde.

📊 Métricas de Avaliação
Accuracy
Precision
Recall
F1-score
Matriz de confusão
📈 Resultados

Os modelos apresentaram boa capacidade de classificação:

A regressão logística demonstrou estabilidade
A árvore de decisão forneceu interpretabilidade
A rede neural apresentou melhor desempenho geral

Variáveis como raio e textura do tumor tiveram maior impacto na predição.

🚀 Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/FIAP94-9IADT/tech_challenge_1.git
cd breast-cancer-prediction
2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Executar o projeto
python main.py
📁 Estrutura do Projeto
.
├── data/
│   └── breast-cancer.csv
├── main.py
├── requirements.txt
└── README.md
📌 Considerações
O modelo não substitui diagnóstico médico
Deve ser utilizado como ferramenta de apoio
Resultados dependem da qualidade dos dados
Pode ser expandido para aplicações clínicas reais
🧠 Aprendizados
Construção de pipelines de Machine Learning
Aplicação de Deep Learning em saúde
Pré-processamento de dados clínicos
Interpretação de modelos
Introdução à visão computacional
👨‍💻 Autor

Lucas Bastos Garcia

📄 Licença

Este projeto é de uso educacional.