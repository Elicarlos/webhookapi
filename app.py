
from flask import Flask, redirect, url_for, request, jsonify

from flask_peewee.auth import Auth
from flask_peewee.db import Database
from peewee import *

# configure our database
DATABASE = {
    'name': 'api.db',
    'engine': 'peewee.SqliteDatabase',
}



app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

@app.route('/api/', methods=['POST', 'GET'])
def api():
    data = request
 
    print(data)

    return 'op'

auth = Auth(app, db)

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    app.run(debug=False)






