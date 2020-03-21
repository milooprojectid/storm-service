from flask import Flask, jsonify, make_response, request
from os import getenv, path
from modules.summarization import summarization
from modules.news_link import getNews
from validators import url

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

        # if is a link, override value
        if (url(text)):
            text = getNews(text)

        summarizer = summarization()
        summary = summarizer.fit(text)

        return jsonify({'message': 'a summary of text', 'data': { 'summary': summary } })
    except ValueError as error:
        return jsonify({ 'message': str(error) }), 422
    except:
        return InternalServerError()

class StormRestServer():
    @staticmethod
    def serve():
        port = getenv('APP_PORT') or '5001'
        print("serving grpc server at " + port)
        app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=port)
