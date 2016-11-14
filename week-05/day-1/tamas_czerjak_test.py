import unittest
import tamas_czerjak_work

class TestWork(unittest.TestCase):
    def setUp(self):
        pass

    def test_anagramm_is_true(self):
        self.assertTrue(tamas_czerjak_work.anagramm('AsdasdasdaSdasd', ' sd aaad asd sda ssd'))

    def test_anagramm_is_false(self):
        self.assertFalse(tamas_czerjak_work.anagramm('asdasdasaasdasd', ' sd aaad asd sda ssd'))

    def test_anagramm_wrong_type(self):
        self.assertRaises(TypeError, tamas_czerjak_work.anagramm, '2', 2)

    def test_count_letters_is_equal(self):
        self.assertEqual(tamas_czerjak_work.count_letters(' sd aaaD Asd s4564da ssd'), {'s': 5, 'a': 5, 'd': 5})

    def test_count_letters_is_false(self):
        self.assertNotEqual(tamas_czerjak_work.count_letters(' sd aaad 1aSd  sda sfsd'), {' ': 5, 's': 5, 'a': 5, 'd': 5})

    def test_anagramm_return_dictionary(self):
        self.assertIsInstance(tamas_czerjak_work.count_letters(' sd aaad asd  sda sfsd'), dict)

if __name__ == '__main__':
    unittest.main()
