.. toctree::
   :maxdepth: 4
   :caption: Contents:

About
==========================================

insta-captions transcriptions are possible with DeepSpeech. For installation of DeepSpeech,
refer to their documentation. I use their pre-trained models on english and mandarin.
These models are included in this repository via Git LFS due to large file size.



Installation
==========================================

To install insta-captions, run:
::

   pip install insta-captions



insta-captions.Transcribe
==========================================
.. automodule:: transcription
   :members:


Examples
==========================================

Here is an example of the transcribe function in the `Transcribe` class.

The .wav files used in this example are found in the following `insta-captions github directory <https://github.com/DavidCendejas/insta-captions/tree/main/data/audio/english_examples>`_

.. code-block:: python
   
   from insta-captions import Transcribe as Trans
   
   wav_files = 
   [
      './8455-210777-0068.wav',
      './4507-16021-0012.wav',
      './2830-3980-0043.wav',
   ]
   
   t = Trans() # default language is "english"
   transcriptions = t.transcribe(wav_files)

   print(transcriptions)
   >>> [
      ('./2830-3980-0043.wav', 'experience proves this'),
      ('./4507-16021-0012.wav', 'why should one halt on the way'),
      ('./8455-210777-0068.wav', 'your paris sufficient i said')
      ]
