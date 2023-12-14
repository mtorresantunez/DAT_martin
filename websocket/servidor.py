from flask import Flask, render_template
from flask_sock import Sock
import httpx

app = Flask(__name__)
sock = Sock(app)


@app.route('/dogs')
def dogs():
    r = httpx.get('https://dog.ceo/api/breeds/image/random')
    d = r.json()
    return render_template('dogs.html', perrito=d.get('message'))



@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)