from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO

ACCEPTABLE_FILENAMES = ['png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/',  methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and file.filename.rsplit('.', 1)[1] in ACCEPTABLE_FILENAMES:
        socketio.emit('refresh')
        file.save('static/image')
        print('yep')
    return redirect('..')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0', debug=True)