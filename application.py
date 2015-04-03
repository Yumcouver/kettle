import json

from flask import Flask
from platform import system
from os.path import dirname

application = Flask(__name__)

if __name__ == "__main__":
    if system() == 'Linux':
        application.run(host='0.0.0.0', threaded=True, debug=True)
    elif system() == 'Darwin':
        application.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
