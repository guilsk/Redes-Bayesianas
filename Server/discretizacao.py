#Pega os valores do arquivo original csv e transforma em numeros para a rede funcionar
import numpy as np
import pandas as pd

arquivo = "Server/Dados/credit_risk_dataset.csv"
temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,HistóricoCredito"
colunas = temp.split(',')
dados = pd.read_csv(arquivo, names=colunas, skiprows=1).dropna()

def discretizar_resultado(valor):
    return discretizar_categorico(valor, 'GrauEmprestimo')

def discretizar_renda_anual(valor):
    return discretizar_numerico(valor, 'RendaAnual')
    
def discretizar_porcentagem_renda(valor):
    return discretizar_numerico(valor, 'RendaPercentual')
    
def discretizar_valor_emprestimo(valor):
    return discretizar_numerico(valor, 'ValorEmprestimo')
    
def discretizar_taxa_juros(valor):
    return discretizar_numerico(valor, 'TaxaJuro')
    
def discretizar_duracao_emprego(valor):
    return discretizar_numerico(valor, 'DuracaoEmprego')
    
def discretizar_status(valor):
    if valor == True:
        valor = 1
    if valor == False:
        valor = 0
    return discretizar_numerico(valor, 'StatusEmprestimo')
    
def discretizar_historico_inadimplencia(valor):
    if valor == True:
        valor = 'Y'
    if valor == False:
        valor = 'N'
    return discretizar_categorico(valor, 'InadimplênciaHistórica')
    
def discretizar_posse_imovel(valor):
    return discretizar_categorico(valor, 'PropriedadeCasa')

def discretizar_intencao(valor):
    return discretizar_categorico(valor, 'IntencaoEmprestimo')

#'''
def discretizar_numerico(valor, coluna):
    n = len(dados[coluna])
    k = int(np.ceil(1 + np.log2(n)))
    bins = np.linspace(dados[coluna].min(), dados[coluna].max(), k + 1)
    return np.digitize(valor, bins=bins, right=False)
'''
def discretizar_numerico(valor, vMin, vMax, k):
    cat = 1
    intervalo = (vMax-vMin)/k
    vCat = vMin+intervalo
    while valor > vCat:
        cat += 1
        vCat += intervalo
    return cat
#'''
def discretizar_categorico(valor, coluna):
    categorias = {cat: idx for idx, cat in enumerate(dados[coluna].unique())}
    return categorias.get(valor, 0)+1