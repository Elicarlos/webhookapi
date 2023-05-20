
from flask import Flask, redirect, url_for, request

import requests

app = Flask(__name__)




@app.route('/api/', methods=['POST', 'GET'])
def api():  
   
    return 'Ola mundo'



if __name__ == '__main__':
    app.run(debug=False)






