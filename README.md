# Sistema de Análise de Crédito com Redes Bayesianas

Este projeto implementa um sistema de análise de crédito utilizando Redes Bayesianas. Ele permite avaliar a probabilidade de concessão de crédito a clientes de um banco com base em dados fornecidos pelo usuário. O sistema é dividido em duas partes: um backend que processa os dados e realiza a análise, e um frontend que fornece uma interface amigável para interação com o usuário.

## Funcionalidades

- Entrada de dados do cliente por meio de um formulário interativo.
- Processamento dos dados utilizando Redes Bayesianas para decisão de concessão de crédito.
- Interface gráfica intuitiva para entrada de dados e visualização do resultado.
- Backend implementado como uma API em Python.
- Frontend em Angular para a interação do usuário.

## Requisitos

### Backend
- Python 3.11
- Bibliotecas especificadas em `requirements.txt`

### Frontend
- Node.js v20.8
- NPM (Node Package Manager)

## Como Executar

### Backend (API)
1. Navegue até o diretório do backend:
   ```bash
   cd Server
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   python main.py
   ```
4. O backend estará disponível no endereço padrão: `http://localhost:8000`.
   > Use `http://localhost:8000/docs#` para acessar a FastAPI.

### Frontend (Interface Gráfica)
1. Navegue até o diretório do frontend:
   ```bash
   cd Client
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run start
   ```
4. A interface estará acessível no navegador em: `http://localhost:4200`.

## Dataset

O sistema utiliza datasets disponíveis no Kaggle para a construção e avaliação do modelo de Redes Bayesianas:
- [Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)
- [German Credit Data with Risk](https://www.kaggle.com/datasets/kabure/german-credit-data-with-risk)
