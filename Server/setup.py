import pandas as pd
import discretizacao as d

def DiscretizarColunas(arquivo):
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,HistóricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1)
    dados = dados.dropna()
    dados['GrauEmprestimo'] = dados['GrauEmprestimo'].apply(d.discretizar_resultado)
    dados['RendaAnual'] = dados['RendaAnual'].apply(d.discretizar_renda_anual)
    dados['ValorEmprestimo'] = dados['ValorEmprestimo'].apply(d.discretizar_valor_emprestimo)
    dados['TaxaJuro'] = dados['TaxaJuro'].apply(d.discretizar_taxa_juros)
    dados['RendaPercentual'] = dados['RendaPercentual'].apply(d.discretizar_porcentagem_renda)
    dados['DuracaoEmprego'] = dados['DuracaoEmprego'].apply(d.discretizar_duracao_emprego)
    dados['StatusEmprestimo'] = dados['StatusEmprestimo'].apply(d.discretizar_status)
    dados['InadimplênciaHistórica'] = dados['InadimplênciaHistórica'].apply(d.discretizar_historico_inadimplencia)
    dados['PropriedadeCasa'] = dados['PropriedadeCasa'].apply(d.discretizar_posse_imovel)
    dados['IntencaoEmprestimo'] = dados['IntencaoEmprestimo'].apply(d.discretizar_intencao)
    #discretizar demais colunas
    dados.to_csv(arquivo[:-4]+'_discrete.csv', index=False)

DiscretizarColunas("./Dados/credit_risk_dataset.csv")