import os
import unittest

from . import TEST_DATA_DIR
from FastxIO import fastx

class TestMixed(unittest.TestCase):

    def setUp(self):

        self.mixed_file = os.path.join(TEST_DATA_DIR, "mixed.txt")
        self.gz_mixed_file = os.path.join(TEST_DATA_DIR, "mixed.txt.gz")
    
    
    def _verify_mixed(self, reader):
        
        rec = reader.next()
        self.assertEqual(rec.name, "IRIS:7:1:17:394#0/1") 
        self.assertEqual(rec.sequence, "GTCAGGACAAGAAAGACAANTCCAATTNACATTATG")
        self.assertEqual(rec.quality, "aaabaa`]baaaaa_aab]D^^`b`aYDW]abaa`^")

        rec = reader.next()
        self.assertEqual(rec.name, "lbc1") 
        self.assertEqual(rec.sequence, "TCAGACGATGCGTCAT")
        self.assertEqual(rec.quality, "")

        rec = reader.next()
        self.assertEqual(rec.name, "IRIS:7:1:17:800#0/1") 
        self.assertEqual(rec.sequence, "GGAAACACTACTTAGGCTTATAAGATCNGGTTGCGG")
        self.assertEqual(rec.quality, "ababbaaabaaaaa`]`ba`]`aaaaYD\\\\_a``XT")

        rec = reader.next()
        self.assertEqual(rec.name, "lbc2") 
        self.assertEqual(rec.sequence, "CTATACATGACTCTGC")
        self.assertEqual(rec.quality, "")

        self.assertRaises(StopIteration, reader.next)

    def test_mixed(self):
        reader = fastx.FastxReader(self.mixed_file)
        self._verify_mixed(reader)

    def test_gz_mixed(self):
        reader = fastx.FastxReader(self.gz_mixed_file)
        self._verify_mixed(reader)
