
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)
@app.route('/api/', methods=['POST', 'GET'])
def api():
    data = request.get_json(silent=True) 

    return jsonify({data})



if __name__ == '__main__':
    app.run(debug=False)






