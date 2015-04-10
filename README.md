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
>
```
POST /v1/recognize/<recognizer_id>
```
##### Header
Name          | Type | Description
----          | ---- | -----------
Content-Type  |string| [format of audio](http://webdesign.about.com/od/multimedia/a/mime-types-by-content-type.htm)
##### Body<br/>
data of audio


#### Send url of audio to server, server downloads the audio by itself
>
```
GET /v1/recognize/<recognizer_id>
```
##### Header
Name          | Type | Description
----          | ---- | -----------
Content-Type  |string| [format of audio](http://webdesign.about.com/od/multimedia/a/mime-types-by-content-type.htm)
##### Parameters
Name  | Type | Description
----  | ---- | -----------
url   |string|**(required)** url of audio

### Research Stack
##### [Speech recognizer comparison](http://suendermann.com/su/pdf/oasis2014.pdf)
Word error rates on the VM1 test set and the WSJ1 november ’93 test set.

  Recognizer                                                         | VM1  | WSJ1 
  ----------                                                         | ---  | ----
[HDecode](http://htk.eng.cam.ac.uk/extensions/)     v3.4.1     (HMM) | 22.9 | 19.8 
[Julius](http://julius.sourceforge.jp/en_index.php) v4.3       (HMM) | 27.2 | 23.1 
[pocketsphinx](http://cmusphinx.sourceforge.net) v0.8          (HMM) | 23.9 | 21.4 
[Sphinx-4](http://cmusphinx.sourceforge.net)                   (HMM) | 26.9 | 22.7 
[Kaldi](http://kaldi.sourceforge.net)                   (Deep neural)| 12.7 |  6.5 
