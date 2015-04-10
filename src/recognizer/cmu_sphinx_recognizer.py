from tempfile import NamedTemporaryFile
from pocketsphinx import Decoder
from load_config import SPHINX_HMM, SPHINX_LM, SPHINX_DICT
from recognizer.base_recognizer import BaseRecognizer


class CMUSphinxRecognizer(BaseRecognizer):
    def __init__(self):
        config = Decoder.default_config()
        config.set_string('-hmm', SPHINX_HMM)
        config.set_string('-lm', SPHINX_LM)
        config.set_string('-dict', SPHINX_DICT)
        self.decoder = Decoder(config)

    def recognize(self, raw_audio):
        file_path = self.__save_file(raw_audio)
        with open(file_path, 'r') as wav_fp:
            self.decoder.decode_raw(wav_fp)
            hypothesis = self.decoder.hyp()
            return hypothesis.hypstr, hypothesis.best_score, hypothesis.prob

    @staticmethod
    def __save_file(data):
        tmp_fp = NamedTemporaryFile(delete=False)
        tmp_fp.write(data)
        tmp_fp.close()
        return tmp_fp.name
