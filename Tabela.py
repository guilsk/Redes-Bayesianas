import pandas as pd  #pip install kaggle 
import kagglehub #pip install kagglehub   
from urllib.request import urlopen #pip install pgmpy 
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

 
# Download latest version
path = kagglehub.dataset_download("laotse/credit-risk-dataset")

print("Path to dataset files:", path)

arquivo = path + "/credit_risk_dataset.csv"

temp = "Idade,Renda Anual,Propriedade Casa,Duração do emprego (em anos),Intenção de empréstimo,Grau de empréstimo,Valor do empréstimo,Taxa de juro,Status do empréstimo,Renda percentual,Inadimplência histórica,histórico de crédito"
colunas = temp.split(',')
dados = pd.read_csv(arquivo, names=colunas)
print(dados)
