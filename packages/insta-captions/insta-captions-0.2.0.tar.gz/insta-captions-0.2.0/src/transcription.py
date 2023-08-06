import numpy as np
import wave
from deepspeech import Model as dsm


class Transcribe:
    _models = {
        "english": "data/language_models/deepspeech-0.9.3-models.pbmm",
        "mandarin": "data/language_models/deepspeech-0.9.3-models-zh-CN.pbmm",
    }

    _lm = {
        "english": "data/language_models/deepspeech-0.9.3-models.scorer",
        "mandarin": "data/language_models/deepspeech-0.9.3-models-zh-CN.scorer",
    }

    _alphabeta = {
        "english": {"alpha": 0.931289039105002, "beta": 1.1834137581510284},
        "mandarin": {"alpha": 0.6940122363709647, "beta": 4.777924224113021},
    }

    _beam_width = 100

    __model = None

    __transcriptions = []

    def __init__(self, language="english"):
        """Constructor

        :param language: What language should this instance transcribe in
          must be "english" or "mandarin", defaults to "english"
        :type language: str, optional
        :raises ValueError: If "english" or "mandarin" is not set, a ValueError is raised
        """
        if not (language == "english" or language == "mandarin"):
            raise ValueError("language param must be either \'english\' or \'mandarin\' .")

        self.__model = dsm(self._models[language])
        self.__model.enableExternalScorer(self._lm[language])
        self.__model.setScorerAlphaBeta(self._alphabeta[language]["alpha"], self._alphabeta[language]["beta"])
        self.__model.setBeamWidth(self._beam_width)

    def read_from_wav(self, filename):
        with wave.open(filename, "rb") as w:
            rate = w.getframerate()
            frames = w.getnframes()
            buffer = w.readframes(frames)
        return rate, buffer

    def wav_to_text(self, model, filename):
        rate, buffer = self.read_from_wav(filename)
        wav_data = np.frombuffer(buffer, dtype=np.int16)
        return model.stt(wav_data)

    def get_transcriptions(self):
        """A getter function that returns a history of transcriptions from the transcribe() function

        :return: A list of transcriptions from each time a Transcribe instance calls transcribe()
        :rtype: list
        """
        return self.__transcriptions

    def get_model(self):
        """A getter function that gets the DeepSpeech model created in the constructor.

        :return: DeepSpeech model object
        :rtype: :class: `deepspeech.Model`
        """
        return self.__model

    def transcribe(self, wav_files):
        """Given a list of .wav filepaths, returns a list of tuples where each tuple is (filepath, transcription).
        Both filepath and transcription are strings.

        :param wav_files: A list of filepaths to .wav files
        :type wav_files: List of strings (filepaths)
        :return: A list of tuples where value 1 is the filepath and value 2 is the transcribed string
        :rtype: list of tuples
        """
        if len(wav_files) == 0:
            return []
        else:
            try:
                transcriptions = []
                for audiofile in wav_files:
                    transcription = self.wav_to_text(self.__model, audiofile)
                    transcriptions.append((audiofile, transcription))
            except FileNotFoundError:
                print("Invalid File")
            else:
                self.__transcriptions.append(transcriptions)
                return transcriptions
