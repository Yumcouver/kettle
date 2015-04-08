kettle
==
Server providing api for speech to text using different recognizer

Recognizer Id:
```
0: CMU Sphinx
1: Kaldi
```

API reference:
For now, the format of audio should be compatible with recognizer
Later, the server should handle the conversion.

Send audio stream to server
```
POST /v1/raw/<recognizer_id>
BODY data of audio
```
Send url of audio to server
```
GET /v1/wav/<recognizer_id>?url=
```
