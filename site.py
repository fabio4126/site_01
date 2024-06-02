from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Bem vindo ao Site'

@app.route('/boas')
def boas():
    return render_template('saudacao.html')

if __name__ == '__main__':
    app.run(debug=True)