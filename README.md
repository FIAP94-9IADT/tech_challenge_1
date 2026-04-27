# Tech Challenge 1

Projeto em Python/Jupyter para classificacao de cancer de mama com foco em exploracao de dados, pre-processamento, comparacao entre modelos e explicabilidade.

## Estrutura

- `tech_challenge_breast_cancer.ipynb`: notebook principal do projeto.
- `requirements.txt`: dependencias Python do projeto.
- `setup_env.ps1`: cria o ambiente virtual local e instala as dependencias.
- `start_notebook.ps1`: abre o notebook com configuracoes locais do Jupyter.
- `validate_notebook.ps1`: executa uma validacao automatica das celulas de codigo.

## Requisitos

- Windows com PowerShell
- Python 3.11 ou superior instalado e disponivel como `py` ou `python`

## Como configurar

No diretorio do projeto, execute:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_env.ps1
```

Esse comando:

- cria um ambiente virtual local em `.venv`
- instala as bibliotecas do `requirements.txt`

## Como abrir o notebook

```powershell
powershell -ExecutionPolicy Bypass -File .\start_notebook.ps1
```

## Como validar a execucao

```powershell
powershell -ExecutionPolicy Bypass -File .\validate_notebook.ps1
```

## Observacoes

- O dataset esperado pelo notebook e `dataset/breast-cancer.csv`.
- Pastas locais de cache e configuracao do Jupyter/IPython/Matplotlib estao no `.gitignore`.
- O ambiente virtual `.venv` tambem nao e versionado.
