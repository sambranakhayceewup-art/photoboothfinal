"""PetalPop: Python Flask web application and print-ready photo processing."""
from io import BytesIO
import base64
import binascii
from flask import Flask, jsonify, request, send_file
from PIL import Image, UnidentifiedImageError

app = Flask(__name__, static_folder='.', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024

@app.get('/')
def home():
    return app.send_static_file('index.html')

@app.get('/api/health')
def health():
    return jsonify(status='ok', app='PetalPop', engine='Python Flask')

@app.post('/api/print-ready')
def print_ready():
    """Convert the browser's final decorated canvas into a 300-DPI PNG.

    No image is retained on the server; processed bytes are returned immediately.
    """
    data = request.get_json(silent=True) or {}
    encoded = data.get('image', '')
    if not isinstance(encoded, str) or not encoded.startswith('data:image/png;base64,'):
        return jsonify(error='A PNG image is required.'), 400
    try:
        raw = base64.b64decode(encoded.split(',', 1)[1], validate=True)
        if len(raw) > 20 * 1024 * 1024:
            return jsonify(error='Image is too large.'), 413
        with Image.open(BytesIO(raw)) as source:
            if source.format != 'PNG' or source.width * source.height > 30_000_000:
                return jsonify(error='Unsupported image dimensions or format.'), 400
            result = source.convert('RGB')
            output = BytesIO()
            result.save(output, format='PNG', dpi=(300, 300), optimize=True)
            output.seek(0)
    except (ValueError, binascii.Error, UnidentifiedImageError, OSError):
        return jsonify(error='Invalid image data.'), 400
    return send_file(output, mimetype='image/png', as_attachment=True,
                     download_name='PetalPop_Print_300DPI.png')

@app.errorhandler(413)
def too_large(_):
    return jsonify(error='Image exceeds the upload limit.'), 413

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
