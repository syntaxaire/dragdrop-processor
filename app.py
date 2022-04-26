import logging

from flask import Flask, current_app, request

from processor import example


logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
log = logging.getLogger(__name__)

app = Flask('dragdrop-app', static_url_path='')  # serve the 'static' directory at /

# MAX_CONTENT_LENGTH determines the maximum size of file that Flask will accept as an upload.
# If this is exceeded, the browser will receive a 413 error on upload.
app.config['MAX_CONTENT_LENGTH'] = 100 * 1_000_000  # 100 megabytes


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/submitfiles', methods=['POST'])
def submitfiles():
    """Receive files submitted via POST on the page."""
    files = request.files.getlist('file')
    for file in files:
        example(file)
    return '', 200
