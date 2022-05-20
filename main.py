import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'A API está no ar'


@app.route('/pegarVendas')
def contatos():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    print(total_vendas)
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


@app.route('/soma/<soma>', methods=['GET'])
def soma(soma):
    return jsonify({'soma': soma})


app.run()
