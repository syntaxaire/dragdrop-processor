from flask import Flask, current_app, request
from werkzeug.utils import secure_filename


app = Flask('dragdrop-app', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1_000_000  # allow up to 100 megabytes


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/submitfiles', methods=['POST'])
def submitfiles():
    """Receive files submitted via POST on the page."""
    files = request.files.getlist('file')
    for file in files:
        filename = secure_filename(file.filename)  # defeat filename tricks
        print(f'Filename: {filename}\nInfo: {file}\n')
    return '', 200
