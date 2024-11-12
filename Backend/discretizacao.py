def discretizar_renda_anual(valor):
    if valor < 5000:
        return 'baixa'
    elif valor < 12000:
        return 'media'
    else:
        return 'alta'