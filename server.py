from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from requests import get

ACCEPTABLE_FILENAMES = ['png', 'jpg', 'jpeg', 'gif', 'jfif']

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/',  methods=['POST'])
def upload_file():
    if file := request.files.get('file'):
        if file.filename.rsplit('.', 1)[1] in ACCEPTABLE_FILENAMES:
            socketio.emit('refresh')
            file.save('static/image')
    elif url := request.form.get('url'):
        if url.rsplit('.', 1)[1] in ACCEPTABLE_FILENAMES:
            r = get(url)
            with open('static/image', 'wb') as file:
                file.write(r.content)
    return redirect('..')

@socketio.on('secret')
def secret(password):
    if password == 'lol':
        with open('code.js') as file:
            code = file.read()
            socketio.emit('run', code)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0', debug=True)