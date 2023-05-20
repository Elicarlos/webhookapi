import sys
sys.path.append('..')
import requests
import pandas as pd
from flask import Flask, redirect, url_for, request, jsonify
import json
from models import User, LogCliente, create_tables
from peewee import PostgresqlDatabase




app = Flask(__name__)
app.config.from_object(__name__)
create_tables()


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
def relatorio_logs():
    logs = LogCliente.select()
    for log in logs:
        print(log.nome)

    # df = pd.json_normalize(response_json)
    # print(df)
    

    return 'relatorio'
# auth = Auth(app, db)

if __name__ == '__main__':
    create_tables()
    # auth.User.create_table(fail_silently=True)
    app.run(debug=False)






