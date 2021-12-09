from flask import Flask, flash, render_template, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    rt = requests.get('https://aws.random.cat/meow')
    dados = rt.json()
    cat = dados['file']
    return render_template('index.html', gato=cat)
    


if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.run( debug=True)
