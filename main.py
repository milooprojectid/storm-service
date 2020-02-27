from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from os import getenv, path
from Summarization import summarization
from NewsLink import getNews

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def text():
    try:
        body = request.get_json()
        sentence = body['text'] if 'text' in body else ''
        if sentence == '':
            return jsonify({'message': 'news is required'})

        summary = summarization.fit(sentence)
        return jsonify({'message': summary, 'data': sentence})

    except:
        return jsonify({'message' : 'something wrong dude'})   


@app.route('/link', methods = ['POST'])
def link():

    try:
        body = request.get_json()
        link = body['text'] if 'text' in body else ''
        if lnk == '':
            return jsonify({'message': 'link news is required'})

        sentence = getNews(link)
        summary = summarization.fit(sentence)
        return jsonify({'message': summary, 'data': sentence})

    except:
        return jsonify({'message' : 'something wrong dude'})


if __name__ == '__main__':
    app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=getenv('APP_PORT') or '5001')
