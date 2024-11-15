# Redes-Bayesianas

# Variáveis Significativas

## Booleanas:
### Status do empréstimo (calote) - loan_status:
Valores: {0 (em dia), 1 (calote)}
### Calote no histórico - cb_person_default_on_file:
Valores: {N (sem calote), Y (calote)}

## Números:
### Renda - person_income:
Tipo: Número inteiro
Valores: 0 <= x
### Tempo empregado (em anos) - person_emp_length:
Tipo: Número inteiro
Valores: 0 <= x
### Montante do empréstimo - loan_amnt:
Tipo: Número inteiro
Valores: 0 < x
### Taxa de juro:
Tipo: Número real
Valores: 1 < x

## Variáveis categóricas:
### Posse de imóveis - person_home_ownership:
Valores:
* OWN
* RENT
* MORTGAGE
* OTHER
### Intenção do empréstimo - loan_intent:
Valores:
* EDUCATION
* HOMEIMPROVEMENT
* MEDICAL
* PERSONAL
* VENTURE


### Imports necessários: kagglehub / pgmpy / uvicorn / FastAPI

```cmd
pip install -r requirements.txt
```
> Rode o comando acima para importar os módulos necessários.