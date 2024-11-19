import main
import model
import discretizacao as d
dados = model.InputData(
    valor=10000,
    renda=40000,
    tempoEmpregado=2,
    taxaJuros=10,
    statusCalote=False,
    caloteHistorico=False,
    posseImoveis='RENT',
    intencao='MEDICAL'
)
print(main.Pesquisa(dados))