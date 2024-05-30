from cryptoelp_scoring import score_english_ascii_simple

import unittest

class TestCryptoelpScoring(unittest.TestCase):
    def setUp(self):
        pass

    def test_score_english_ascii_simple(self):
        self.assertEqual(score_english_ascii_simple("Test words"), 1)
        self.assertEqual(score_english_ascii_simple("###&"), 0)


if __name__ == "__main__":
    unittest.main()