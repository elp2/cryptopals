import unittest

from cryptoelp_basics import base64_decode, base64_encode, hextets_to_chars, fixed_xor, chars_to_hextets

BASE64_ENCODE_DECODE_PAIRS = {
    "TQ==": "M",
    "TWFu": "Man",
    "YWI=": "ab",
    "TWFuTWFuTWFu": "ManManMan",
    "YWJj": "abc",
    "TWFu": "Man",
    "TWFu": "Man",
    "TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu": "Many hands make light work.",
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t": "I'm killing your brain like a poisonous mushroom",    
}

class TestCryptoelpBasics(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_base64_decode(self):
        for enc, dec in BASE64_ENCODE_DECODE_PAIRS.items():
            self.assertEqual(base64_decode(enc), dec)

    def test_base64_encode(self):
        for enc, dec in BASE64_ENCODE_DECODE_PAIRS.items():
            self.assertEqual(base64_encode(dec), enc)

    def test_hextets_to_chars(self):
        cow = "436f77"
        self.assertEqual(hextets_to_chars(cow), "Cow")

    def test_fixed_xor_simple(self):
        self.assertEqual(fixed_xor("a", "b"), fixed_xor("b", "a"))
        self.assertEqual(fixed_xor("a", "b"), chr(3))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
