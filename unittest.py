import unittest
import cap
class TestCap(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Duck')
