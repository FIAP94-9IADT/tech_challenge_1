# 📚 ÍNDICE DE NAVEGAÇÃO - Tech Challenge FIAP

## 🎯 **Comece por Aqui!**

### **Novo no Projeto?**
1. 📄 Leia primeiro: [`README.md`](README.md)
2. ⚡ Início rápido: [`QUICKSTART.md`](QUICKSTART.md)  
3. 📋 Verifique requisitos: [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md)
4. 📖 Guia completo: [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md)

---

## 📂 **Estrutura de Arquivos**

### **📄 Documentação Principal**

| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [`README.md`](README.md) | Documentação principal do projeto | Primeiro arquivo a ler |
| [`QUICKSTART.md`](QUICKSTART.md) | Guia de início rápido (5 minutos) | Para começar imediatamente |
| [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md) | Passo a passo detalhado de 21 dias | Durante todo o desenvolvimento |
| [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md) | Checklist completo de requisitos | Para verificar o que falta |
| [`INDEX.md`](INDEX.md) | Este arquivo - índice de navegação | Para encontrar informações |

---

### **📓 Notebooks (em ordem de execução)**

| Notebook | Objetivo | Tempo Estimado |
|----------|----------|----------------|
| `01_EDA_exploracao.ipynb` | Análise exploratória de dados | 6-8 horas |
| `02_preprocessamento.ipynb` | Limpeza e pré-processamento | 4-6 horas |
| `03_modelagem.ipynb` | Treinamento de modelos | 6-8 horas |
| `04_avaliacao.ipynb` | Métricas e comparação | 4-6 horas |
| `05_explicabilidade.ipynb` | SHAP e feature importance | 4-6 horas |
| `EXTRA_visao_computacional.ipynb` | CNN com imagens (opcional) | 8-12 horas |

---

### **🐍 Módulos Python (`src/`)**

| Módulo | Funções Principais |
|--------|-------------------|
| `data_loader.py` | Carregamento de datasets |
| `preprocessing.py` | Limpeza e transformação |
| `models.py` | Definição e treinamento de modelos |
| `evaluation.py` | Cálculo de métricas |
| `explainability.py` | SHAP e interpretabilidade |
| `visualization.py` | Gráficos e visualizações |

---

### **📂 Estrutura de Pastas**

```
tech_challenge_fiap_oficial/
│
├── 📄 Documentação
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── GUIA_COMPLETO.md
│   ├── REQUISITOS_FIAP.md
│   └── INDEX.md (este arquivo)
│
├── 📂 data/
│   ├── raw/                    # Dados originais (coloque seu dataset aqui)
│   └── processed/              # Dados após pré-processamento
│
├── 📂 notebooks/
│   ├── 01_EDA_exploracao.ipynb
│   ├── 02_preprocessamento.ipynb
│   ├── 03_modelagem.ipynb
│   ├── 04_avaliacao.ipynb
│   ├── 05_explicabilidade.ipynb
│   └── EXTRA_visao_computacional.ipynb
│
├── 📂 src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   ├── explainability.py
│   └── visualization.py
│
├── 📂 models/
│   └── saved_models/           # Modelos treinados salvos
│
├── 📂 reports/
│   ├── figures/                # Gráficos salvos
│   ├── relatorio_tecnico.md    # Relatório final
│   └── eda_insights.md         # Insights da EDA
│
├── 📂 docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── 📄 Configuração
│   ├── requirements.txt        # Dependências Python
│   ├── .gitignore             # Arquivos ignorados pelo Git
│   └── .env.example           # Exemplo de variáveis de ambiente
│
└── 📂 docs/
    ├── video_instrucoes.md    # Instruções para gravação do vídeo
    └── referencias.md         # Referências bibliográficas
```

---

## 🎯 **Fluxo de Trabalho Recomendado**

### **Fase 1: Preparação (Dia 1)**
1. ✅ Ler [`README.md`](README.md)
2. ✅ Seguir [`QUICKSTART.md`](QUICKSTART.md)
3. ✅ Configurar ambiente
4. ✅ Baixar dataset

### **Fase 2: Desenvolvimento (Dias 2-14)**
1. ✅ Seguir [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md)
2. ✅ Executar notebooks na ordem
3. ✅ Marcar itens em [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md)
4. ✅ Documentar descobertas

### **Fase 3: Finalização (Dias 15-21)**
1. ✅ Completar relatório técnico
2. ✅ Gravar vídeo
3. ✅ Revisar checklist
4. ✅ Entregar projeto

---

## 📋 **Checklists Rápidos**

### **Setup Inicial**
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] Dataset baixado
- [ ] Repositório Git configurado

### **Desenvolvimento**
- [ ] EDA completo (Notebook 01)
- [ ] Pré-processamento (Notebook 02)
- [ ] 2+ modelos treinados (Notebook 03)
- [ ] Métricas calculadas (Notebook 04)
- [ ] SHAP implementado (Notebook 05)

### **Entrega**
- [ ] Relatório técnico pronto
- [ ] Vídeo gravado e uploadado
- [ ] Repositório organizado
- [ ] PDF de entrega criado

---

## 🆘 **Problemas Comuns e Soluções**

### **"Não sei por onde começar"**
→ Leia [`QUICKSTART.md`](QUICKSTART.md) e execute os comandos

### **"Erro ao instalar dependências"**
→ Verifique versão do Python (3.10+)
→ Use ambiente virtual
→ `pip install --upgrade pip`

### **"Dataset não carrega"**
→ Verifique caminho do arquivo
→ Tente diferentes encodings: `encoding='utf-8'` ou `'latin-1'`

### **"Não entendo o que fazer"**
→ Leia [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md) seção por seção
→ Siga cronograma de 21 dias

### **"Meu modelo não está bom"**
→ Verifique pré-processamento
→ Tente diferentes algoritmos
→ Faça feature engineering
→ Otimize hiperparâmetros

---

## 📊 **Marcos do Projeto**

### **Milestone 1: EDA Completo (Dia 7)**
- [ ] Notebook 01 finalizado
- [ ] Insights documentados
- [ ] Visualizações salvas

### **Milestone 2: Modelos Treinados (Dia 14)**
- [ ] Notebooks 02-05 finalizados
- [ ] 2+ modelos comparados
- [ ] SHAP implementado
- [ ] Métricas calculadas

### **Milestone 3: Documentação (Dia 18)**
- [ ] Relatório técnico completo
- [ ] Vídeo gravado
- [ ] Repositório organizado

### **Milestone 4: Entrega (Dia 21)**
- [ ] Tudo revisado
- [ ] PDF de entrega pronto
- [ ] Projeto submetido

---

## 🎓 **Recursos de Aprendizado**

### **Conceitos Fundamentais**
- [Análise Exploratória de Dados](https://www.kaggle.com/learn/data-cleaning)
- [Feature Engineering](https://www.kaggle.com/learn/feature-engineering)
- [Machine Learning Intro](https://www.kaggle.com/learn/intro-to-machine-learning)

### **Bibliotecas Específicas**
- [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)

### **Machine Learning em Saúde**
- Buscar: "machine learning healthcare tutorials"
- Kaggle: notebooks sobre diagnóstico médico
- Papers: Google Scholar "breast cancer machine learning"

---

## 🔗 **Links Úteis**

### **Datasets**
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

### **Ferramentas**
- [GitHub](https://github.com/)
- [Google Colab](https://colab.research.google.com/) (alternativa ao Jupyter local)
- [Kaggle Notebooks](https://www.kaggle.com/code) (outra alternativa)

### **Comunidades**
- [Stack Overflow](https://stackoverflow.com/questions/tagged/machine-learning)
- [Kaggle Forums](https://www.kaggle.com/discussions)
- [Reddit r/MachineLearning](https://reddit.com/r/MachineLearning)

---

## 📞 **Ajuda e Suporte**

### **Dúvidas Técnicas**
1. Consulte a documentação oficial das bibliotecas
2. Busque no Stack Overflow
3. Verifique notebooks do Kaggle
4. Pergunte no fórum da FIAP

### **Dúvidas sobre o Projeto**
1. Releia [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md)
2. Consulte [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md)
3. Pergunte para colegas (sem copiar código!)
4. Entre em contato com tutor/professor

---

## ✅ **Checklist de Leitura**

Marque conforme for lendo os documentos:

- [ ] [`README.md`](README.md) - Visão geral do projeto
- [ ] [`QUICKSTART.md`](QUICKSTART.md) - Início rápido
- [ ] [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md) - Checklist de requisitos
- [ ] [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md) - Guia passo a passo
- [ ] [`INDEX.md`](INDEX.md) - Este arquivo

---

## 🎯 **Próximos Passos**

### **Se você está começando agora:**
1. Leia [`README.md`](README.md) (10 minutos)
2. Execute [`QUICKSTART.md`](QUICKSTART.md) (15 minutos)
3. Baixe o dataset (10 minutos)
4. Comece o Notebook 01 (2-3 horas)

### **Se você já começou:**
1. Verifique [`REQUISITOS_FIAP.md`](REQUISITOS_FIAP.md)
2. Marque o que já foi feito
3. Identifique o que falta
4. Siga o cronograma do [`GUIA_COMPLETO.md`](GUIA_COMPLETO.md)

### **Se você está finalizando:**
1. Revise todos os notebooks
2. Complete o relatório técnico
3. Grave o vídeo
4. Verifique checklist final
5. Entregue!

---

**Última atualização: Abril 2026**  
**FIAP - Pós-Graduação Tech - IA para Desenvolvedores**

**Boa sorte no seu Tech Challenge! 🚀**

---

**Dúvida de navegação?** Use `Ctrl+F` para buscar palavras-chave neste arquivo!
