from .transcription import Transcribe as Trans
import googletrans
from googletrans import Translator


class Instacaptions(Trans):
    def __init__(self, source="english"):
        """Constructor

        :param source: What language the source wav files will be in,
            defaults to "english"
        :type source: str, optional
        """
        super().__init__(source)
        self.__translator = Translator()
        self.__codes = {v: k for k, v in googletrans.LANGUAGES.items()}

    def translate(self, transcription, target):
        """Given a string, uses google translate API to translate into the target language

        :param transcription: The string in the source language.
        :type transcription: str
        :param target: The desired language for the text to be translated into.
        :type target: str
        :return: Returns the translate text in the target language
        :rtype: str
        """
        if target in self.__codes:
            target = self.__codes[target]
        translation = self.__translator.translate(transcription, dest=target).text
        return translation

    def translate_wavs(self, wav_files, target):
        """Takes a str list of wav_files and will return a translated list of the
            transcriptions in the target language

        :param wav_files: A list of filepaths to .wav files
        :type wav_files: List of str
        :param target: The desired language for the text to be translated into.
        :type target: str
        :return: Returns a list of str of the translated transcriptions in the target language
        :rtype: list of str
        """
        if len(wav_files) == 0:
            return []
        translations = []
        transcriptions = self.transcribe(wav_files)

        for transcription in transcriptions:
            translation = self.translate(transcription[1], target)
            translations.append(translation)

        return translations
