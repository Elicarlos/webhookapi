import sys
sys.path.append('..')
import requests
import pandas as pd
from flask import render_template
from flask import Flask, redirect, url_for, request, jsonify
import json
from models import User, LogCliente, create_tables
from peewee import PostgresqlDatabase




app = Flask(__name__)
app.config.from_object(__name__)
create_tables()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/', methods=['POST', 'GET'])
def api():
    response  = request.data
    response_str = response.decode('utf-8')
    response_json = json.loads(response_str)
    print(response_json)

    LogCliente.insira_varios(response_json)

    # df = pd.json_normalize(response_json)
    # print(df)
    

    return 'op'


@app.route('/relatorio/', methods=['GET'])
def relatorio():
    return render_template('result.html', logs_clientes=None)


@app.route('/search/', methods=['POST'])
def search():
    email = request.form['email']
    logs_clientes = LogCliente.select().where(LogCliente.email == email)

    return render_template('result.html', logs_clientes=logs_clientes)

if __name__ == '__main__':
    create_tables()
    # auth.User.create_table(fail_silently=True)
    app.run(debug=False)






