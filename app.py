import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
	flash("Qual o seu nome?")
	return render_template("index.html")
@app.route("/seguir", methods=['POST', 'GET'])
def seguir():
	flash("Ola " + str(request.form['nome_input']) + " bem vindo!" )
	return render_template("index.html")

if __name__ == '__main__':
	
	app.run(debug=True)