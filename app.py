
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)
@app.route('/api/', methods=['POST', 'GET'])
def api():
    data = request.data
    print(dir(data))
    print(data)

    return 'op'



if __name__ == '__main__':
    app.run(debug=False)






