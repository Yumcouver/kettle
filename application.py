import os

from flask import Flask, request
from platform import system
from recognizer.cmu_sphinx_recognizer import CMUSphinxRecognizer

application = Flask(__name__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

recognizers = {0: CMUSphinxRecognizer()}

@application.route('/v1/wav/<int:recognizer_id>', methods=['GET'])
def recognize_wav(recognizer_id):
    return recognizers[recognizer_id].recognize_wav_to_json(request.args.get('url'))

@application.route('/v1/raw/<int:recognizer_id>', methods=['POST'])
def recognize_raw(recognizer_id):
    return recognizers[recognizer_id].recognize_to_json(request.get_data())

if __name__ == "__main__":
    if system() == 'Linux':
        application.run(host='0.0.0.0', threaded=True, debug=True)
    elif system() == 'Darwin':
        application.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
