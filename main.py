import pandas as pd
import kagglehub  # pip install kagglehub
from pgmpy.models import BayesianNetwork # pip install pgmpy
from pgmpy.inference import VariableElimination

def DownloadTabela():
    path = kagglehub.dataset_download("laotse/credit-risk-dataset")
    return path

def CriarModelo(dados):

    modelo = BayesianNetwork([
    ('GrauEmprestimo', 'RendaAnual'),
    ('GrauEmprestimo', 'PropriedadeCasa')
    ])
    
    modelo.fit(dados)
    inferencia = VariableElimination(modelo)
    return inferencia

def AbrirTabela():

    path = DownloadTabela()
    arquivo = path + "/credit_risk_dataset.csv"
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,históricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)

    dados['RendaAnual'] = dados['RendaAnual'].apply(discretizar_renda_anual)
    
    inferencia = CriarModelo(dados)
    return inferencia

def discretizar_renda_anual(valor):
    if valor < 5000:
        return 'baixa'
    elif valor < 12000:
        return 'media'
    else:
        return 'alta'

def Pesquisa(renda,imovel):
    inferencia = AbrirTabela()
    resultado = inferencia.query(['GrauEmprestimo'], evidence={'RendaAnual': discretizar_renda_anual(renda), 'PropriedadeCasa': imovel})
    print(resultado)

Pesquisa(10000,'RENT')