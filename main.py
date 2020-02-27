from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from os import getenv, path
from modules.summarization import summarization
from modules.news_link import getNews

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)

def getParameter(body, param):
    if param not in body or body[param] == '':
        raise ValueError(param + ' is required')
    return body[param]

def InternalServerError():
    return jsonify({ 'message': 'something went wrong' }), 500


@app.route('/link', methods = ['POST'])
def link():
    try:
        body = request.get_json()
        url = getParameter(body, 'url')

        sentence = getNews(url)
        summarizer = summarization()
        summary = summarizer.fit(sentence)

        return jsonify({'message': 'summary of a link', 'data': summary })
    except ValueError as error:
        return jsonify({ 'message': str(error) }), 422
    except:
        return InternalServerError()

@app.route('/', methods = ['POST'])
def fromText():
    try:

        body = request.get_json()
        text = getParameter(body, 'text')
        summarizer = summarization()
        summary = summarizer.fit(text)

        return jsonify({'message': 'a summary of text', 'data': { 'summary': summary } })
    except ValueError as error:
        return jsonify({ 'message': str(error) }), 422
    except:
        return InternalServerError()

if __name__ == '__main__':
    app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=getenv('APP_PORT') or '5001')
