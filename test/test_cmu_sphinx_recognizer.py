import urllib2

from unittest import TestCase
from recognizer import CMUSphinxRecognizer


class TestCMUSphinxRecognizer(TestCase):
    def test_recognize_wav_to_json(self):
        recognizer = CMUSphinxRecognizer()
        response = urllib2.urlopen('http://www21.online-convert.com/download-'
                                         'file/33da39bf9811c28cae85b6fb1bfc1ff0/'
                                         'converted-f16ab6e3.wav')
        print recognizer.recognize_wav_to_json(response.read())

    def test_recognize(self):
        recognizer = CMUSphinxRecognizer()
        with open('/Users/Torres/Desktop/L33P1.wav') as fp:
            print recognizer.recognize_wav_to_json(fp.read())
