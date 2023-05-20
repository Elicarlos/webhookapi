import sys
sys.path.append('..')
import requests
import pandas as pd
from flask import Flask, redirect, url_for, request, jsonify
import json
from models import *

# from flask import Auth
# from flask_peewee.db import Database
# from peewee import *

# configure our database
# DATABASE = {
#     'name': 'api.db',
#     'engine': 'peewee.SqliteDatabase',
# }



app = Flask(__name__)
app.config.from_object(__name__)

# db = Database(app)

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

# auth = Auth(app, db)

if __name__ == '__main__':
    # auth.User.create_table(fail_silently=True)
    app.run(debug=False)






