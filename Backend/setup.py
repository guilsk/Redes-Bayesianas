import pandas as pd
import discretizacao as d

def DiscretizarColunas(arquivo):
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,históricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)
    dados['RendaAnual'] = dados['RendaAnual'].apply(d.discretizar_renda_anual)
    #discretizar demais colunas
    dados.to_csv(arquivo[:-4]+'_discrete.csv', index=False)

DiscretizarColunas("Backend\Dados\credit_risk_dataset.csv")