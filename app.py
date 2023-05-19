
from flask import Flask, redirect, url_for, request

import requests

app = Flask(__name__)




@app.route('/webhook.cajuinacode', methods=['POST', 'GET'])
def hello_world():
    response = requests.get('https://webhook.site/e284cee9-0278-4c23-9a8f-23d5192c08e2')
    # print(dir(response))
    print(response.text)
    return 'Ola mundo'



if __name__ == '__main__':
    app.run(debug=True)






