import json


class BaseRecognizer:
    def recognize(self, raw_audio):
        raise NotImplementedError

    def recognize_to_json(self, raw_audio):
        (hypstr, best_score, prob) = self.recognize(raw_audio)
        return json.dumps({'transcript': hypstr, 'score': best_score, 'confidence': prob})

    def recognize_wav(self, wav_data):
        return self.recognize(self.__wav_to_raw(wav_data))

    def recognize_wav_to_json(self, wav_data):
        return self.recognize_to_json(self.__wav_to_raw(wav_data))

    @staticmethod
    def __wav_to_raw(wav_data):
        return wav_data[44:]
