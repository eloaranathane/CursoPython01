from flask import Flask, render_template

# Criação do app flask
app = Flask(__name__)

# Rota da página principal
@app.route('/')              # O @ é um decorator e semore precisa de um def
def home() :
    return "<h1>Bem vindo a minha API</h1>"     # <h1> tag de inicio e tag de fim, cria um título no site, vai até o h6, reduzindo as letras a cada numero

# Rota da página sobre 
@app.route('/sobre')
def sobre() :
    return "<h1> Criado por Eloara </h1>"

# Rota com variáveis na URL
@app.route('/ola/<nome>')
def ola(nome) :
    return f"<h1>Olá, {nome}!</h1><br/><h2>Bem vindo a minha pagina pessoal</h2><a href='http://www.google.com'>Google</a>"

# Iniciar o servidor
if __name__ == '__main__' :
    app.run(debug=True)      # debug=True atualiza apenas salvando o documento e dando f5 no site