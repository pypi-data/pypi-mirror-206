from src.instacaptions import Instacaptions as IC
import unittest


class TestInstacaptions(unittest.TestCase):
    def test_translate(self):
        insta = IC()
        test1 = insta.translate("I love this class", target="es")  # to spanish
        test2 = insta.translate("我討厭這個班級", target="english")
        self.assertEqual("Amo esta clase", test1)
        self.assertEqual("I hate this class", test2)

    def test_translate_wavs(self):
        wavs = [
            "data/audio/english_examples/2830-3980-0043.wav",
            "data/audio/english_examples/4507-16021-0012.wav",
            "data/audio/english_examples/8455-210777-0068.wav",
        ]

        insta = IC()
        translations = insta.translate_wavs(wavs, "spanish")
        self.assertEqual("La experiencia lo demuestra", translations[0])
        self.assertEqual("¿Por qué se debe detener en el camino?", translations[1])
        self.assertEqual("tu parís suficiente dije", translations[2])
