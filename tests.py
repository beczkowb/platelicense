import unittest

from . import app


class TestApp(unittest.TestCase):
    def test(self):
        test_str_1 = 'Ala ma kota a kot ma samochod o tablicach DF12345'
        test_str_2 = 'FF8K3JD Bla bla costam costam alfdskj'
        test_str_3 = 'FF8K3JD Bla bla VFKKDDVV costam alfdskj'
        test_str_4 = 'FF8K3JD Bla bla VFKKDDVV costam alfdskjGF345BB'

        result_str_1 = 'Ala ma kota a kot ma samochod o tablicach <PLATE>'
        result_str_2 = '<PLATE> Bla bla costam costam alfdskj'
        result_str_3 = '<PLATE> Bla bla <PLATE>V costam alfdskj'
        result_str_4 = '<PLATE> Bla bla <PLATE>V costam alfdskj<PLATE>'

        self.assertEqual(result_str_1,
                         app.get_result(test_str_1, app.find_plates(test_str_1)))
        self.assertEqual(result_str_2,
                         app.get_result(test_str_2, app.find_plates(test_str_2)))
        self.assertEqual(result_str_3,
                         app.get_result(test_str_3, app.find_plates(test_str_3)))
        self.assertEqual(result_str_4,
                         app.get_result(test_str_4, app.find_plates(test_str_4)))


if __name__ == '__main__':
    unittest.main()
