import pandas as pd
import kagglehub
from urllib.request import urlopen
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination


# Download latest version
arquivo = kagglehub.dataset_download("laotse/credit-risk-dataset")

temp = "Idade,Renda Anual,Propriedade Casa,Duração do emprego (em anos),Intenção de empréstimo,Grau de empréstimo,Valor do empréstimo,Taxa de juro,Status do empréstimo,Renda percentual,Inadimplência histórica,histórico de crédito"
colunas = temp.split(',')
dados = pd.read_csv(arquivo, names=colunas)
