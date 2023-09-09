from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def session():
    return render_template('session.html', data = {'junk': 'junk value'})

def call_message_received(methods=['GET', 'POST']):
    return 'Message received.'

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print ('received message: ' + str(json))
    socketio.emit('my response', json, callback=call_message_received)

if __name__ == '__main__':
    socketio.run(app, debug = True)

