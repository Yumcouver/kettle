import json
import urllib2

from tempfile import NamedTemporaryFile
from pocketsphinx import Decoder
from load_config import SPHINX_HMM, SPHINX_LM, SPHINX_DICT

class CMUSphinxRecognizer:
    def __init__(self):
        config = Decoder.default_config()
        config.set_string('-hmm', SPHINX_HMM)
        config.set_string('-lm', SPHINX_LM)
        config.set_string('-dict', SPHINX_DICT)
        self.decoder = Decoder(config)

    def recognize(self, raw_audio):
        file_path = self.save_file(raw_audio)
        with open(file_path, 'r') as wav_fp:
            self.decoder.decode_raw(wav_fp)
            hypothesis = self.decoder.hyp()
            return (hypothesis.hypstr, hypothesis.best_score, hypothesis.prob)

    def recognize_wav(self, url):
        response = urllib2.urlopen(url)
        return self.recognize(response.read()[44:])

    def save_file(self, data):
        tmp_fp = NamedTemporaryFile(delete=False)
        tmp_fp.write(data)
        tmp_fp.close()
        return tmp_fp.name

    def recognize_wav_to_json(self, url):
        response = urllib2.urlopen(url)
        return self.recognize_to_json(response.read()[44:])

    def recognize_to_json(self, raw_audio):
        (hypstr, best_score, prob) = self.recognize(raw_audio)
        return json.dumps({'transcript': hypstr, 'score': best_score, 'confidence': prob})
