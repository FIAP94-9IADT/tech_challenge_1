# Tech Challenge 1

Projeto em Python/Jupyter para classificação de câncer de mama, com um notebook principal de Machine Learning tradicional e um notebook complementar com CNN aplicada a recortes mamográficos.

## Estrutura

- `tech_challenge_breast_cancer.ipynb`: notebook principal do projeto.
- `tech_challenge_breast_cancer_CNN.ipynb`:  CNN aplicada a recortes de mamografia.
- `requirements.txt`: dependências Python do projeto.
- `setup_env.ps1`: cria o ambiente virtual local e instala as dependências dos dois notebooks.

## Requisitos

- Windows com PowerShell
- Python 3.11 ou superior instalado e disponivel como `py` ou `python`

## Como configurar o ambiente

No diretório do projeto, execute:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_env.ps1
```

Esse comando:

- Cria um ambiente virtual local em `.venv`
- Instala todas as bibliotecas necessárias para os dois notebooks

## Como testar

Depois da configuração do ambiente, basta abrir os notebooks no VS Code e executar as celulas normalmente.

Ordem sugerida:

1. `tech_challenge_breast_cancer.ipynb`
2. `tech_challenge_breast_cancer_CNN.ipynb`