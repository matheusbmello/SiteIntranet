# Site com os scripts: https://cdnjs.com/
#pip install python-socketio flask-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagens
@socketio.on("message")
def gerenciar_mensagens(mensagem):
    send(mensagem, broadcast=True)

# Criar a nossa 1° página = 1° rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Roda o nosso app
socketio.run(app, host="192.168.0.63")