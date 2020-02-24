from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from os import getenv, path

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def text():
    return jsonify({'message': 'a summary of text', 'data': None })

@app.route('/link', methods = ['POST'])
def link():
    return jsonify({'message': 'a summary of url link', 'data': None })


if __name__ == '__main__':
    app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=getenv('APP_PORT') or '5001')
