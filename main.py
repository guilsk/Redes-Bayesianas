import pandas as pd  # pip install kaggle
import kagglehub  # pip install kagglehub
from urllib.request import urlopen  # pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
import Entrada as entrada

# Função para discretizar a RendaAnual
def discretizar_renda_anual(valor):
    if valor < 5000:
        return 'baixa'
    elif valor < 12000:
        return 'media'
    else:
        return 'alta'

# Download do dataset mais recente
path = kagglehub.dataset_download("laotse/credit-risk-dataset")
print("Path to dataset files:", path)

arquivo = path + "/credit_risk_dataset.csv"
temp = "Idade,RendaAnual,PropriedadeCasa,Duração do emprego (em anos),Intenção de empréstimo,GrauEmpréstimo,Valor do empréstimo,Taxa de juro,Status do empréstimo,Renda percentual,Inadimplência histórica,histórico de crédito"
colunas = temp.split(',')
dados = pd.read_csv(arquivo, names=colunas, skiprows=1)

# Discretizando a coluna 'RendaAnual' do dataset
dados['RendaAnual'] = dados['RendaAnual'].apply(discretizar_renda_anual)

# Construção do modelo BayesianNetwork
modelo = BayesianNetwork([
    ('GrauEmpréstimo', 'RendaAnual'),
    ('GrauEmpréstimo', 'PropriedadeCasa')
])

modelo.fit(dados)
inferencia = VariableElimination(modelo)

# Realizando a inferência
result_dist = inferencia.query(['GrauEmpréstimo'], evidence={'RendaAnual': discretizar_renda_anual(entrada.renda), 'PropriedadeCasa': entrada.imovel})
print(result_dist)
