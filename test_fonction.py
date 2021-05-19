import unittest
from fonction import ouvrire_fichier


class TestMethods(unittest.TestCase):
    def test_ouvrire_fichier(self):
        self.assertIsInstance(ouvrire_fichier(), dict)
        self.assertNotIsInstance(ouvrire_fichier(), list)

    def test_resto_ouvert(self):
        self.assertIsInstance(resto_ouvert('Mon Dec 7 14:59:26 2010'), dict)
        self.assertNotIsInstance(resto_ouvert('Mon Dec 7 14:59:26 2010'), list)