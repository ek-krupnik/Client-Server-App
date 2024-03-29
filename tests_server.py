import unittest
import lib_server
from macros_server import *


class TestCountry(unittest.TestCase):
    def test_init_id(self):
        with self.assertRaises(TypeError):
            new_country = lib_server.Country('5', 'name', False)

    def test_init_name(self):
        with self.assertRaises(TypeError):
            new_country = lib_server.Country(5, lambda x: x ** 2, False)
        with self.assertRaises(IndexError):
            new_country = lib_server.Country(5, 'name', False)

    def test_init_infected(self):
        with self.assertRaises(TypeError):
            new_country = lib_server.Country(5, 'name', 'False')

    def test_id(self):
        new_country = lib_server.Country(5, 'France', False)
        self.assertEqual(new_country.id, 5)

    def test_name(self):
        new_country = lib_server.Country(5, 'France', False)
        self.assertEqual(new_country.name, 'France')

    def test_infected(self):
        new_country = lib_server.Country(5, 'France', False)
        self.assertFalse(new_country.infected)


class TestVirus(unittest.TestCase):

    def setUp(self):
        self.virus = lib_server.EuropeVirus()

    def tearDown(self):
        pass

    def test_get_id(self):
        with self.assertRaises(IndexError):
            test_id = self.virus.get_id('name')
        self.assertTrue(self.virus.get_id(LIST_COUNTRIES[0]) < len(LIST_COUNTRIES))

    def test_get_one_id(self):
        self.assertTrue(self.virus.get_id(LIST_COUNTRIES[0]), 0)

    def test_all_info(self):
        self.assertFalse(len(self.virus.countries) == 0)

    def test_info(self):
        with self.assertRaises(TypeError):
            self.virus.get_info('name')

    def test_spread(self):
        with self.assertRaises(TypeError):
            self.virus.spread('name')

    def test_go_days(self):
        with self.assertRaises(TypeError):
            self.virus.go_days('5')
        with self.assertRaises(ValueError):
            self.virus.go_days(-5)

    def test_get_links(self):
        with self.assertRaises(IndexError):
            self.virus.get_links('name')


if __name__ == '__main__':
    unittest.main()
