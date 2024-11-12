import model
import discretizacao as d
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

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
    arquivo = "/credit_risk_dataset.csv"
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,históricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)
    inferencia = CriarModelo(dados)
    return inferencia

inferencia = AbrirTabela()

def Pesquisa(renda,imovel,duracaoEmprego,intencao,valor,taxaJuro,status,inadimplencia):
    percentualRenda = valor/renda
    resultado = inferencia.query(['GrauEmprestimo'], evidence={'RendaAnual': d.discretizar_renda_anual(renda), 'PropriedadeCasa': imovel, 'DuracaoEmprego': duracaoEmprego, 'IntencaoEmprestimo': intencao, 'ValorEmprestimo': valor, 'TaxaJuro': taxaJuro, 'StatusEmprestimo': status, 'RendaPercentual': percentualRenda, 'InadimplênciaHistórica': inadimplencia})
    emprestimo = PossivelEmprestimo(resultado)
    return emprestimo

def Pesquisa(inputData: model.InputData):
    return Pesquisa(inputData.renda, inputData.posseImoveis, inputData.tempoEmpregado, inputData.intencao, inputData.valor, inputData.taxaJuros, inputData.statusCalote, inputData.caloteHistorico)

def PossivelEmprestimo(reps):
    valor = 0
    for i in range(3):
        valor += reps.values[i]
    valor = valor*100

    if valor > 60.0:
        return True;
    else:
        return False;