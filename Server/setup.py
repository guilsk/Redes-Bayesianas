import numpy as np
import pandas as pd
import discretizacao as d

#Metado para descretizar o arquivo original e criar um novo descretizado

def DiscretizarColunas(arquivo):
    temp = "Idade,RendaAnual,PropriedadeCasa,DuracaoEmprego,IntencaoEmprestimo,GrauEmprestimo,ValorEmprestimo,TaxaJuro,StatusEmprestimo,RendaPercentual,InadimplênciaHistórica,HistóricoCredito"
    colunas = temp.split(',')
    dados = pd.read_csv(arquivo, names=colunas, skiprows=1).dropna()
    '''
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
    '''
    dados = codificar_dataframe(dados)
    #'''
    dados.to_csv(arquivo[:-4]+'_discrete.csv', index=False)

def codificar_dataframe(df):
    df_transformado = pd.DataFrame(index=df.index)  # Iniciar DataFrame transformado

    # Processar colunas numéricas
    numeric_cols = df.select_dtypes(include=['number']).columns
    #print(numeric_cols)
    for col in numeric_cols:
        n = len(df[col])  # Número de dados na coluna
        k = int(np.ceil(1 + np.log2(n)))  # Número de classes (Fórmula de Sturges)
        bins = np.linspace(df[col].min(), df[col].max(), k + 1)  # Criar os bins
        print(col,bins)
        df_transformado[col] = np.digitize(df[col], bins=bins, right=False)

    # Processar colunas categóricas
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    #print(categorical_cols)
    for col in categorical_cols:
        # Criar mapeamento para categorias únicas
        categorias = {cat: idx for idx, cat in enumerate(df[col].unique())}
        print(col,categorias)
        # Substituir valores pelas classes
        df_transformado[col] = df[col].map(categorias)+1
    
    return df_transformado

DiscretizarColunas("Server/Dados/credit_risk_dataset.csv")