# ⚡ QUICKSTART - Tech Challenge FIAP
## Comece em 15 Minutos!

---

## 🎯 **O Que Você Vai Fazer Agora**

1. ✅ Configurar ambiente Python (5 min)
2. ✅ Baixar dataset (5 min)
3. ✅ Executar primeiro notebook (5 min)

**Tempo total**: 15 minutos

---

## 🚀 **Passo 1: Configurar Ambiente (5 min)**

### **Abra o PowerShell:**

```powershell
# Navegar para a pasta do projeto
cd "c:\Users\Documents\PosTech - Fiap\Tech\tech_challenge_fiap_oficial"

# Criar ambiente virtual
python -m venv venv

# Ativar (se der erro de política, veja abaixo)
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

### **💡 Se der erro de política:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Depois tente ativar novamente.

### **Verificar instalação:**
```powershell
python -c "import pandas, sklearn, shap; print('✅ Tudo certo!')"
```

---

## 📥 **Passo 2: Baixar Dataset (5 min)**

### **Opção A: Usar sklearn (MAIS RÁPIDO)**

Crie um arquivo `download_data.py`:

```python
from sklearn.datasets import load_breast_cancer
import pandas as pd
import os

# Criar pasta se não existir
os.makedirs('data/raw', exist_ok=True)

# Carregar dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Salvar
df.to_csv('data/raw/breast_cancer.csv', index=False)
print("✅ Dataset salvo em: data/raw/breast_cancer.csv")
print(f"📊 Dimensões: {df.shape}")
```

Execute:
```powershell
python download_data.py
```

### **Opção B: Baixar do Kaggle (manual)**

1. Acesse: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
2. Clique em "Download"
3. Extraia o CSV
4. Coloque em: `data/raw/breast_cancer.csv`

---

## 📓 **Passo 3: Abrir Jupyter (5 min)**

```powershell
# Iniciar Jupyter Notebook
jupyter notebook
```

Isso abrirá seu navegador automaticamente.

### **Navegue:**
1. Clique em `notebooks/`
2. Abra `01_EDA_exploracao.ipynb`
3. Execute a primeira célula (Shift + Enter)

---

## ✅ **Verificação Rápida**

Se tudo funcionou, você deve ver:

```
✅ Bibliotecas importadas com sucesso!
📦 Pandas version: 2.1.4
📦 NumPy version: 1.26.2
```

---

## 🎯 **Próximos Passos**

Agora que está tudo configurado:

1. **Execute o Notebook 01 completo** (2-3 horas)
   - Leia cada célula Markdown
   - Execute célula por célula
   - Anote suas observações

2. **Leia o Guia Completo**
   - Abra: `GUIA_COMPLETO.md`
   - Siga o cronograma de 21 dias

3. **Verifique Requisitos**
   - Abra: `REQUISITOS_FIAP.md`
   - Marque o que já fez
   - Planeje o que falta

---

## 🆘 **Problemas Comuns**

### **Erro: "python não é reconhecido"**
→ Python não instalado ou não no PATH
→ Baixe: https://www.python.org/downloads/
→ Marque "Add to PATH" na instalação

### **Erro ao ativar venv**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Jupyter não abre**
→ Copie a URL do terminal e cole no navegador
→ Exemplo: `http://localhost:8888/?token=abc123...`

### **ImportError ao executar notebook**
→ Certifique-se que o venv está ativado
→ Reinstale: `pip install -r requirements.txt --force-reinstall`

---

## 📚 **Documentação Completa**

Este é apenas o início rápido! Para documentação completa:

- **Visão Geral**: Leia `README.md`
- **Passo a Passo**: Leia `GUIA_COMPLETO.md`
- **Requisitos**: Leia `REQUISITOS_FIAP.md`
- **Navegação**: Leia `INDEX.md`

---

## 🎓 **Estrutura dos Notebooks**

Execute na ordem:

1. **`01_EDA_exploracao.ipynb`** → Explorar dados
2. **`02_preprocessamento.ipynb`** → Limpar dados
3. **`03_modelagem.ipynb`** → Treinar modelos
4. **`04_avaliacao.ipynb`** → Avaliar resultados
5. **`05_explicabilidade.ipynb`** → SHAP e insights

---

## 💡 **Dicas Rápidas**

### ✅ **Faça:**
- Execute célula por célula (Shift + Enter)
- Leia os comentários
- Anote suas observações
- Salve frequentemente (Ctrl + S)
- Faça backup do trabalho

### ❌ **Evite:**
- Executar tudo de uma vez
- Pular células
- Ignorar erros
- Esquecer de salvar
- Deixar para última hora

---

## 📊 **Comandos Úteis**

### **Jupyter:**
- `Shift + Enter`: Executar célula e ir para próxima
- `Ctrl + Enter`: Executar célula e permanecer nela
- `Esc + A`: Criar célula acima
- `Esc + B`: Criar célula abaixo
- `Esc + DD`: Deletar célula
- `Esc + M`: Converter para Markdown
- `Esc + Y`: Converter para código

### **PowerShell:**
```powershell
# Ativar venv
.\venv\Scripts\Activate.ps1

# Desativar venv
deactivate

# Ver pacotes instalados
pip list

# Jupyter
jupyter notebook
```

---

## 🎯 **Checklist de Hoje**

Para o primeiro dia, complete:

- [ ] Ambiente configurado
- [ ] Dataset baixado
- [ ] Jupyter funcionando
- [ ] Notebook 01 iniciado
- [ ] Primeiras células executadas
- [ ] Guia completo lido (overview)

---

## 📅 **Planejamento**

### **Hoje (Dia 1):**
- Setup completo (15 min) ✅
- Iniciar Notebook 01 (2-3 horas)

### **Amanhã (Dia 2-3):**
- Completar Notebook 01
- Documentar insights

### **Esta Semana:**
- Notebooks 01 e 02 completos
- EDA finalizado
- Pré-processamento pronto

---

## 🚀 **Pronto para Começar?**

Execute os comandos do Passo 1 AGORA! ⬆️

---

## 📞 **Precisa de Ajuda?**

1. **Problemas técnicos**: Stack Overflow
2. **Dúvidas do projeto**: `GUIA_COMPLETO.md`
3. **Requisitos**: `REQUISITOS_FIAP.md`
4. **Navegação**: `INDEX.md`

---

**Boa sorte! Você consegue! 🎯**

---

*Tempo estimado de leitura: 3 minutos*  
*Tempo estimado de execução: 15 minutos*  
*Última atualização: Abril 2026*
