#Pega os valores do arquivo original csv e transforma em numeros para a rede funcionar

def discretizar_resultado(valor):
    if valor == 'A' or valor == 'B' or valor == 'C':
        return 1
    else:
        return 2

def discretizar_renda_anual(valor):
    if valor < 10000:
        return 1
    elif valor < 30000:
        return 2
    elif valor < 50000:
        return 3
    elif valor < 100000:
        return 4
    elif valor < 200000:
        return 5
    else:
        return 6
    
def discretizar_porcentagem_renda(valor):
    if valor < .1:
        return 1
    elif valor < .2:
        return 2
    elif valor < .3:
        return 3
    elif valor < .4:
        return 4
    else:
        return 5
    
def discretizar_valor_emprestimo(valor):
    if valor < 5000:
        return 1
    elif valor < 10000:
        return 2
    elif valor < 20000:
        return 3
    elif valor < 25000:
        return 4
    else:
        return 5
    
def discretizar_taxa_juros(valor):
    if valor < 5:
        return 4
    elif valor < 10:
        return 3
    elif valor < 15:
        return 2
    else:
        return 1
    
def discretizar_duracao_emprego(valor):
    if valor < 7:
        return 1
    elif valor < 13:
        return 2
    else:
        return 3
    
def discretizar_status(valor):
    if valor == 1 or valor == True:
        return 1
    elif valor == 0 or valor == False:
        return 2
    else:
        return None
    
def discretizar_historico_inadimplencia(valor):
    if valor == 'Y' or valor == True:
        return 1
    elif valor == 'N' or valor == False:
        return 2
    else:
        return None
    
def discretizar_posse_imovel(valor):
    return ['OWN','RENT','MORTGAGE','OTHER'].index(valor)+1

def discretizar_intencao(valor):
    return ['EDUCATION','HOMEIMPROVEMENT','MEDICAL','PERSONAL','VENTURE','DEBTCONSOLIDATION'].index(valor)+1