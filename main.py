from config import (
    SECRET_KEY,
)
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

@app.route('/')
def session():
    return render_template('session.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print ('received message: ' + str(json))
    socketio.emit('my response', json)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    socketio.run(app, debug = True)

