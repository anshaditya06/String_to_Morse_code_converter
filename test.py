import unittest
from main import text_to_morse, morse_to_text  # import your functions

class TestMorseConverter(unittest.TestCase):

    def test_text_to_morse_basic(self):
        self.assertEqual(text_to_morse("SOS"), "... --- ...")

    def test_text_to_morse_lowercase(self):
        self.assertEqual(text_to_morse("sos"), "... --- ...")

    def test_text_to_morse_with_space(self):
        self.assertEqual(text_to_morse("HI THERE"), ".... .. / - .... . .-. .")

    def test_morse_to_text_basic(self):
        self.assertEqual(morse_to_text("... --- ..."), "SOS")

    def test_unsupported_character(self):
        self.assertEqual(text_to_morse("~~~"), "")

    def test_round_trip(self):
        original = "HELLO WORLD"
        morse = text_to_morse(original)
        back_to_text = morse_to_text(morse)
        self.assertEqual(back_to_text, original)


if __name__ == "__main__":
    unittest.main()