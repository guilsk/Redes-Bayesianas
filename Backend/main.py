import model
import discretizacao as d
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
#import numpy as np
#np.seterr(divide='ignore', invalid='ignore')

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
    arquivo = "Backend\Dados\credit_risk_dataset_discrete.csv"
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,HistóricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)
    inferencia = CriarModelo(dados)
    return inferencia

inferencia = AbrirTabela()

def Pesquisa(inputData: model.InputData):
    percentualRenda = round(inputData.valor/inputData.renda, 2)
    resultado = inferencia.query(['GrauEmprestimo'], evidence={'RendaAnual': d.discretizar_renda_anual(inputData.renda), 'PropriedadeCasa': d.discretizar_posse_imovel(inputData.posseImoveis), 'DuracaoEmprego': d.discretizar_duracao_emprego(inputData.tempoEmpregado), 'IntencaoEmprestimo': d.discretizar_intencao(inputData.intencao), 'ValorEmprestimo': d.discretizar_valor_emprestimo(inputData.valor), 'TaxaJuro': d.discretizar_taxa_juros(inputData.taxaJuros), 'StatusEmprestimo': d.discretizar_status(inputData.statusCalote), 'RendaPercentual': d.discretizar_porcentagem_renda(percentualRenda), 'InadimplênciaHistórica': d.discretizar_historico_inadimplencia(inputData.caloteHistorico)})
    emprestimo = PossivelEmprestimo(resultado)
    return emprestimo

def PossivelEmprestimo(reps):
    print(reps)
    #'''
    if reps.values[0] >= 0.6:
        return True
    return False
    '''
    valor = 0
    for i in range(3):
        valor += reps.values[i]
    valor = valor*100

    if valor > 60.0:
        return True
    else:
        return False
    #'''

modelo = model.InputData(valor = 1600, renda = 10000,tempoEmpregado = 6, taxaJuros = 14.74, statusCalote = True, caloteHistorico = False, posseImoveis = 'OWN', intencao = 'VENTURE')
print(Pesquisa(modelo))

#API
#Endereço da documentação API: http://localhost:8000/docs#
app = FastAPI()
#Endpoint
@app.post("/VerificarCredito", tags=["Rede Bayesiana"])
def  Pesquisa(input: model.InputData) -> bool: return Pesquisa(input)
if( __name__ == "__main__"): uvicorn.run(app,port=8000)

