from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

ACCEPTABLE_FILENAMES = ['.png', '.jpg', '.jpeg', '.gif']

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/',  methods=['POST'])
def upload_file():
    if (
        'file' not in request.files or
        (file := request.files.get('file')) or
        file.filename.rsplit('.', 1)[1] in ACCEPTABLE_FILENAMES
       ):
        filename = secure_filename(file.filename)
        file.save('download/'+filename)
        return redirect('..')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)