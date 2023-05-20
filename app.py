
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
@app.route('/api', methods=['POST', 'GET'])
def api():
    req = request.get_json() 
    print(req) 
    return 'Ola mundo'



if __name__ == '__main__':
    app.run(debug=False)






