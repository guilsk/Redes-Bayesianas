import model
import discretizacao as d
import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
#import numpy as np
#np.seterr(divide='ignore', invalid='ignore')

#Criação da Rede Bayesiana
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

#Ler o arquivo csv  
def AbrirTabela():
    arquivo = "Server/Dados/credit_risk_dataset_discrete.csv"
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,HistóricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)
    inferencia = CriarModelo(dados)
    return inferencia

#Recebe a tabela
inferencia = AbrirTabela()

#Realiza a pesquisa na rede
def Pesquisa(inputData: model.InputData):
    percentualRenda = round(inputData.valor/inputData.renda, 2)
    resultado = inferencia.query(['GrauEmprestimo'], evidence={'RendaAnual': d.discretizar_renda_anual(inputData.renda), 'PropriedadeCasa': d.discretizar_posse_imovel(inputData.posseImoveis), 'DuracaoEmprego': d.discretizar_duracao_emprego(inputData.tempoEmpregado), 'IntencaoEmprestimo': d.discretizar_intencao(inputData.intencao), 'ValorEmprestimo': d.discretizar_valor_emprestimo(inputData.valor), 'TaxaJuro': d.discretizar_taxa_juros(inputData.taxaJuros), 'StatusEmprestimo': d.discretizar_status(inputData.statusCalote), 'RendaPercentual': d.discretizar_porcentagem_renda(percentualRenda), 'InadimplênciaHistórica': d.discretizar_historico_inadimplencia(inputData.caloteHistorico)})
    emprestimo = PossivelEmprestimo(resultado)
    return emprestimo

#Calcula o resultado final
def PossivelEmprestimo(reps):
    print(reps)
    if reps.values[0] >= 0.7:
        return True
    return False

#API
#Endereço da documentação API: http://localhost:8000/docs#
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem. Você pode especificar uma lista, ex: ["http://localhost:4200"]
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP, ex: GET, POST, PUT, DELETE
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)
#Endpoint
@app.post("/VerificarCredito", tags=["Rede Bayesiana"])
def  VerificarCredito(input: model.InputData) -> bool: return Pesquisa(input)
if( __name__ == "__main__"): uvicorn.run(app,port=8000)

