# Tech Challenge - Classificação de Risco em Câncer de Mama

## Visão Geral
Este diretório contém a entrega do Tech Challenge com uma solução inicial de machine learning para apoio à classificação de risco em câncer de mama, usando o dataset em `dataset/breast-cancer.csv`.

A implementação principal está no notebook `main.ipynb`.

## Arquivos deste Diretório
- `dataset/breast-cancer.csv`: dataset utilizado no projeto.
- `main.ipynb`: notebook final com análise, modelagem, avaliação e explicabilidade.
- `README.md`: instruções de uso.

## Requisitos
- Python 3.11
- Jupyter Notebook ou JupyterLab

Bibliotecas Python usadas no notebook:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- shap

## Instalação das Dependências
```bash
python3.11 -m pip install pandas numpy matplotlib seaborn scikit-learn shap jupyter
```

## Como Executar
1. No terminal, vá até a **pasta raiz deste repositório** 

2. Inicie o Jupyter:
```bash
python3.11 -m jupyter notebook
```

3. Abra o notebook:
- `main.ipynb`

4. Execute as células em ordem, do início ao fim.

## O que o Notebook Entrega
- Exploração inicial dos dados (estatísticas e distribuições).
- Pré-processamento com pipeline.
- Análise de correlação com heatmap geral e heatmap focado.
- Treinamento e avaliação de três modelos:
  - Regressão Logística
  - KNN
  - Random Forest
- Métricas por modelo (accuracy, recall, F1-score), relatório de classificação e matriz de confusão.
- Visualização de árvore do Random Forest com `plot_tree`.
- Explicabilidade com importância de variáveis e SHAP.
- Simulação final de uso do modelo com entrada manual e saída:
  - **Benigno** ou **Maligno**
  - probabilidade estimada de malignidade.


