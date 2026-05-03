# Tech Challenge 1

Projeto em Python/Jupyter para classificação de câncer de mama, com um notebook principal de Machine Learning tradicional e um notebook complementar com CNN aplicada a recortes mamográficos.

## Estrutura

- `tech_challenge_breast_cancer.ipynb`: notebook principal do projeto.
- `tech_challenge_breast_cancer_CNN.ipynb`: notebook complementar com CNN aplicada a recortes de mamografia.
- `requirements.txt`: dependências Python do projeto.
- `setup_env.ps1`: cria o ambiente virtual local e instala as dependências dos dois notebooks.

## Requisitos

- Windows com PowerShell
- Python 3.11 ou 3.12 instalado e disponível como `python` ou `py`

## Como configurar o ambiente

No PowerShell, entre primeiro na pasta do projeto:

```powershell
cd "C:\caminho\para\tech_challenge_1"
```

Depois execute:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_env.ps1
```

Esse comando:

- cria um ambiente virtual local em `.venv`
- instala todas as bibliotecas necessárias para os dois notebooks
- tenta instalar diretamente e, se houver problema de caminho longo, tenta novamente com caminho encurtado

Importante:

- este projeto requer Python 3.11 ou 3.12
- Python 3.13+ não é suportado neste ambiente por causa das dependências da etapa com CNN, especialmente `tensorflow` e `numpy`

## Como testar

Depois da configuração do ambiente, basta abrir os notebooks no VS Code ou Jupyter e executar as células normalmente.

Ordem sugerida:

1. `tech_challenge_breast_cancer.ipynb`
2. `tech_challenge_breast_cancer_CNN.ipynb`