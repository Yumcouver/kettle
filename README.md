kettle
==
Server providing api for speech to text using different recognizer

#### Recognizer id
- 0: [CMU Sphinx](http://cmusphinx.sourceforge.net)
- 1: [Kaldi](http://kaldi.sourceforge.net)

### API reference
For now, the format of audio should be compatible with recognizer.<br/>
Later, the server should handle the conversion.


#### Send audio stream to server
```
POST /v1/raw/<recognizer_id>
```
> ##### Body<br/>
data of audio

#### Send url of audio to server, server downloads the audio by itself
```
GET /v1/wav/<recognizer_id>
```
> ##### Parameters
Name  | Type | Description
|-----|------|------------
url   |string|**(required)** url of audio
