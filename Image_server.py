from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    file.save(os.path.join('uploads', file.filename))
    return 'Image uploaded', 200

@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    return send_file(os.path.join('uploads', filename))

if __name__ == '__main__':
    app.run()
