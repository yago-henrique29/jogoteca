from flask import Flask, render_template

app = Flask(__name__)

class jogos:
        def __init__(self, nome, categoria, console):
                self.nome = nome
                self.categoria = categoria
                self.console = console


jogo1 = jogos('Lol', 'Moba', 'PC')
jogo2 = jogos('Cs', 'FPS', 'PC')
jogo3 = jogos('Dota', 'Moba', 'PC')
lista = [jogo1, jogo2, jogo3]

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

app.run()