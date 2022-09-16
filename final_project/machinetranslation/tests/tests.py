import unittest
from machinetranslation import translator as tr

class test_translations(unittest.TestCase):
    def test_f2e_1(self):
        test = tr.french_to_english("Je vais a la boulangerie avec mon pere et mon mere.")
        self.assertEqual(test,"I am going to the bakery with my father and my mother.")

    def test_f2e_2(self):
        test = tr.french_to_english("J'aime la physique")
        self.assertEqual(test,"I love physics")

    def test_e2f_1(self):
        test = tr.english_to_french("What does AI stands for?")
        self.assertEqual(test,"Qu'est-ce que l'IA signifie?")

    def test_e2f_2(self):
        test = tr.english_to_french("What am I supposed to code?")
        self.assertEqual(test,"Qu'est-ce que je suis censé coder?")

    def test_null_1(self):
        test = tr.french_to_english()
        self.assertTrue(test is not None)
        self.assertRaises(Exception)
        self.assertNotEqual("Missing text input! Rerun the code with a text next time.",test)

    def test_null_2(self):
        test = tr.english_to_french()
        self.assertTrue(test is not None)
        self.assertRaises(Exception)
        self.assertNotEqual("Missing text input! Rerun the code with a text next time.",test)

    def test_hello(self):
        test = tr.english_to_french("Hello")
        self.assertEqual(test,"Bonjour")

    def test_bonjour(self):
        test = tr.french_to_english("Bonjour")
        self.assertEqual(test,"Hello")

if __name__ == "__main__":
    unittest.main()
