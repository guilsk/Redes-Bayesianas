import pandas as pd
import kagglehub
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

def DownloadTabela():
    path = kagglehub.dataset_download("laotse/credit-risk-dataset")
    return path

def CriarModelo(dados):

    modelo = BayesianNetwork([
    ('GrauEmprestimo', 'RendaAnual'),
    ('GrauEmprestimo', 'PropriedadeCasa'),
    ('GrauEmprestimo', 'DuracaoEmprego'),
    ('GrauEmprestimo', 'IntencaoEmprestimo'),
    ('GrauEmprestimo', 'ValorEmprestimo'),
    ('GrauEmprestimo', 'TaxaJuro'),
    ('GrauEmprestimo', 'StatusEmprestimo'),
    ('GrauEmprestimo', 'RendaPercentual'),
    ('GrauEmprestimo', 'InadimplênciaHistórica'),
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
    #discretizar demais colunas
    
    inferencia = CriarModelo(dados)
    return inferencia

def discretizar_renda_anual(valor):
    if valor < 5000:
        return 'baixa'
    elif valor < 12000:
        return 'media'
    else:
        return 'alta'
    
# criar funções para discretizar demais colunas

def Pesquisa(renda,imovel,duracaoEmprego,intencao,valor,taxaJuro,status,inadimplencia):
    inferencia = AbrirTabela()
    percentualRenda = valor/renda
    resultado = inferencia.query(['GrauEmprestimo'], evidence={'RendaAnual': discretizar_renda_anual(renda), 'PropriedadeCasa': imovel, 'DuracaoEmprego': duracaoEmprego, 'IntencaoEmprestimo': intencao, 'ValorEmprestimo': valor, 'TaxaJuro': taxaJuro, 'StatusEmprestimo': status, 'RendaPercentual': percentualRenda, 'InadimplênciaHistórica': inadimplencia})
    emprestimo = PossivelEmprestimo(resultado)
    return emprestimo

def PossivelEmprestimo(reps):
    valor = 0
    for i in range(3):
        valor += reps.values[i]
    valor = valor*100

    if valor > 60.0:
        return True;
    else:
        return False;