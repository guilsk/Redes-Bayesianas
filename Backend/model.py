from typing import Literal
from pydantic import BaseModel, PositiveInt, NonNegativeInt, PositiveFloat

class InputData(BaseModel):
    valor: PositiveInt # Deve ser menor que a renda
    renda: NonNegativeInt # Deve ser maior que o valor
    tempoEmpregado: NonNegativeInt # Em anos

    taxaJuros: PositiveFloat # > 1

    statusCalote: bool # false: Em dia || true: Calote
    caloteHistorico: bool # false: Não há registro de calote || true: Há registro de calote

    posseImoveis: Literal['OWN','RENT','MORTGAGE','OTHER']
    intencao: Literal['EDUCATION','HOMEIMPROVEMENT','MEDICAL','PERSONAL','VENTURE','DEBTCONSOLIDATION']


class OutputData(BaseModel):
    result: bool # false: Não aceito || true: Aceito