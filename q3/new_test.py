import unittest
from scrape import *
import io
import scrape as sc
from io import  StringIO
import sys


class Testing(unittest.TestCase):
    def test_for_new(self):
        with self.assertRaises(ValueError):
            scrap("anurag")
    def test_for_old(self):
        outp = io.StringIO()
        sys.stdout = outp
        scrap("anshul.d.sharma.7")
        sys.stdout = sys.__stdout__
        self.assertEqual(outp.getvalue(), "My name is Anshul Dutt Sharma and my current city is Roorkee\n")


if __name__ == "__main__":
    unittest.main()
