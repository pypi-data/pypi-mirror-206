# insta-captions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![issues](https://img.shields.io/github/issues/DavidCendejas/insta-captions)

[![Build Status](https://github.com/DavidCendejas/insta-captions/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/DavidCendejas/insta-captions/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/DavidCendejas/insta-captions/branch/main/graph/badge.svg?token=Z2HN4RCJGZ)](https://codecov.io/gh/DavidCendejas/insta-captions)
[![PyPI](https://img.shields.io/pypi/v/insta-captions)](https://pypi.org/project/insta-captions/)
[![Documentation Status](https://readthedocs.org/projects/insta-captions/badge/?version=latest)](https://insta-captions.readthedocs.io/en/latest/?badge=latest)

insta-captions is a tool that will allow for the instant transcription and translation of audio files to and from different languages.

View more on our [documentation page](https://insta-captions.readthedocs.io/en/latest/)

## Installation

"pip install insta-captions"

## Overview

`insta-captions` is a library that deals with the conversion of audio into "captions". I have been learning Mandarin, my third language. Part of my learning process, as well as maintenance for Spanish, is to watch videos, shows, and movies in the language I am trying to deepen. Sometimes, however, I need to watch content in English but want to read it in another language, and there is no easy way to do this if captions are not provided by the video maker, which is the crux of this issue.

The main feature that I envision for this project would be for audio to be converted into text of any (supported) language regardless of the language of the input audio. This involves two, albeit involved, steps:

- given an audio file, convert that audio into text of language it is in
- given text of one language, translate into another

## Installation and Running

insta-captions transcriptions are possible with [DeepSpeech](https://github.com/mozilla/DeepSpeech). For installation of DeepSpeech, refer to their [documentation](https://deepspeech.readthedocs.io/en/r0.9/?badge=latest). I use their [pre-trained models](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3) on english and mandarin. These models are included in this repository via Git LFS due to large file size.

Additional libraries used are numpy to convert the buffer of the .wav files into int16 numpy arrays as this is what DeepSpeech speech-to-text accepts.

## Example Usage
Using a .wav file from the data folder,
```
    from insta-captions import Transcribe as Trans
    t = Trans()
    print(t.transcribe('./8455-210777-0068.wav'))
    >>> [('./2830-3980-0043.wav', 'experience proves this')]
```



## make commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make format`: autoformat this library using `black`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make test`: run automated tests with `unittest`
- `make coverage`: run automated tests with `unittest` and collect coverage information