from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from os import getenv, path

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)

def getParameter(body, param):
    if param not in body or body[param] == '':
        raise ValueError(param + ' is required')
    return body[param]

def InternalServerError():
    return jsonify({ 'message': 'something went wrong' }), 500

@app.route('/', methods = ['POST'])
def fromText():
    try:
        body = request.get_json()
        text = getParameter(body, 'text')

        return jsonify({'message': 'a summary of text', 'data': { 'summary': text } })

    except ValueError as error:
        return jsonify({ 'message': str(error) }), 422
    except:
        return InternalServerError()

@app.route('/link', methods = ['POST'])
def fromLink():
    try:
        body = request.get_json()
        url = getParameter(body, 'url')

        return jsonify({'message': 'a summary of a link', 'data': { 'summary': url } })

    except ValueError as error:
        return jsonify({ 'message': str(error) }), 422
    except:
        return InternalServerError()

if __name__ == '__main__':
    app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=getenv('APP_PORT') or '5001')
