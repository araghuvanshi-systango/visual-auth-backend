import base64
from io import StringIO
import io
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/', methods=['POST', 'GET'])
def index():
    print("hello")
    return render_template('index.html')


@socketio.on('image')
def image(data_image):
    sbuf = StringIO()
    sbuf.write(data_image)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    try:
        pimg = Image.open(b)
        plt.imshow(np.array(pimg))
        plt.show()
    except:
        pass


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1')
