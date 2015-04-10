import urllib2
from flask import Flask, request
from platform import system
from recognizer import CMUSphinxRecognizer

application = Flask(__name__)

recognizers = {0: CMUSphinxRecognizer()}

@application.route('/v1/recognize/<int:recognizer_id>', methods=['GET', 'POST'])
def recognize(recognizer_id):
    recognizer = recognizers[recognizer_id]
    audio_type = request.headers['Content-Type']
    if request.method == 'GET':
        audio_data = urllib2.urlopen(request.args.get('url')).read()
    elif request.method == 'POST':
        audio_data = request.get_data()

    if audio_type == 'audio/x-wav':
        return recognizer.recognize_wav_to_json(audio_data)
    else:
        raise NotImplementedError

if __name__ == "__main__":
    if system() == 'Linux':
        application.run(host='0.0.0.0', threaded=True, debug=True)
    elif system() == 'Darwin':
        application.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
