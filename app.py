from flask import Flask, flash, render_template, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    response = requests.get('https://cataas.com/cat?json=true')
    dados = response.json()
    cat = dados['_id']
    cat = f'https://cataas.com/cat?_id={cat}'
    return render_template('index.html', gato=cat)
    


if __name__ == '__main__':
    app.run(debug=True)
