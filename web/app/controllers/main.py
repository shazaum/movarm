from app import app, db
from app.controllers.models import MovimentoManual
from flask import render_template, request
from flask_migrate import Migrate
from flask import Response
from app.library import MovArm
from time import sleep


app.secret_key = "awfweQWFFr"

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# for how safely store JWTs in cookies
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
# Set the secret key to sign the JWTs with
app.config['JWT_SECRET_KEY'] = 'awfweQWFFr'

Migrate(app, db)

moveUp = 10
moveDown = 11
moveRight = 12
moveLeft = 13

movimento = MovArm(moveUp, moveDown, moveRight, moveLeft)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/reports", methods=["GET", "POST"])
def reports():
    movimentoManual = MovimentoManual.query.all()

    print(dir(movimentoManual))

    moveup = 0
    movedown = 0
    moveright = 0
    moveleft = 0
    for mov in movimentoManual:
        if mov.moveup == 1:
            moveup += 1
        if mov.movedown == 1:
            movedown += 1
        if mov.moveright == 1:
            moveright += 1
        if mov.moveleft == 1:
            moveleft += 1

    movimentos = {"moveup":moveup,"movedown":movedown,"moveright":moveright,"moveleft":moveleft}


    return render_template('reports.html', movimentos=movimentos, movimentomanual=movimentoManual )

def incluir(movimento):
    db.session.add(movimento)
    db.session.commit()

@app.route("/botao", methods=['GET', 'POST'])
def funcao():

    #def __init__(self, moveup, movedown, moveright, moveleft):
    direcao = request.get_json()
    print(direcao)

    if direcao['command'] == "cima":
        movimento.moving("up", True)
        movimento.moving("up", False)
        movimento = MovimentoManual(1,0,0,0)
        incluir(movimento)
    if direcao['command'] == "baixo":
        movimento.moving("down", True)
        movimento.moving("down", False)
        movimento = MovimentoManual(0,1,0,0)
        incluir(movimento)
    if direcao['command'] == "direita":
        movimento.moving("right", True)
        movimento.moving("right", False)
        movimento = MovimentoManual(0,0,1,0)
        incluir(movimento)
    if direcao['command'] == "esquerda":
        movimento.moving("left", True)
        movimento.moving("left", False)
        movimento = MovimentoManual(0,0,0,1)
        incluir(movimento)
    
    if direcao['command'] == "1":
        movimento.moving("left", True)
        sleep(3)
        movimento.moving("left", False)
        movimento = MovimentoManual(0,0,0,1)
        incluir(movimento)

        movimento.moving("up", True)
        sleep(2)
        movimento.moving("up", False)
        movimento = MovimentoManual(1,0,0,0)
        incluir(movimento)

        movimento.moving("down", True)
        sleep(2)
        movimento.moving("down", False)
        movimento = MovimentoManual(0,1,0,0)
        incluir(movimento)

    if direcao['command'] == "2":
        movimento.moving("left", True)
        sleep(3)
        movimento.moving("left", False)
        movimento = MovimentoManual(0,0,0,1)
        incluir(movimento)

        movimento.moving("up", True)
        sleep(5)
        movimento.moving("up", False)
        movimento = MovimentoManual(1,0,0,0)
        incluir(movimento)

        movimento.moving("down", True)
        sleep(2)
        movimento.moving("down", False)
        movimento = MovimentoManual(0,1,0,0)
        incluir(movimento)

    if direcao['command'] == "3":
        movimento.moving("left", True)
        sleep(5)
        movimento.moving("left", False)
        movimento = MovimentoManual(0,0,0,1)
        incluir(movimento)

        movimento.moving("up", True)
        sleep(2)
        movimento.moving("up", False)
        movimento = MovimentoManual(1,0,0,0)
        incluir(movimento)

        movimento.moving("down", True)
        sleep(2)
        movimento.moving("down", False)
        movimento = MovimentoManual(0,1,0,0)
        incluir(movimento)

    return Response("{'Status':'ok'}", status=200, mimetype='application/json')