import os
import unittest

from . import TEST_DATA_DIR
from FastxIO import fastx

class TestWindowsLineEndings(unittest.TestCase):

    def setUp(self):
        self.windows_fasta = os.path.join(TEST_DATA_DIR, "windows_endings.fasta") 
        self.gz_windows_fasta = os.path.join(TEST_DATA_DIR, "windows_endings.fasta.gz")

    
    def _verify_reads(self, reader):

        record_list = list(reader)

        self.assertEqual(len(record_list), 450)
        self.assertEqual(record_list[0].name, "lbc1")
        self.assertEqual(record_list[0].sequence, "TCAGACGATGCGTCAT")
        self.assertEqual(record_list[0].quality, "")
        
        self.assertEqual(record_list[-1].name, "lbc450")
        self.assertEqual(record_list[-1].sequence, "CACTACTAGCGTGTGC")
        self.assertEqual(record_list[-1].quality, "")

    def test_windows_fasta(self):

        reader = fastx.FastaReader(self.windows_fasta)
        self._verify_reads(reader)
    
    def test_windows_fastx(self):

        reader = fastx.FastxReader(self.windows_fasta)
        self._verify_reads(reader)

    def test_windows_gz_fasta(self):

        reader = fastx.FastaReader(self.gz_windows_fasta)
        self._verify_reads(reader)
    
    def test_windows_gz_fastx(self):

        reader = fastx.FastxReader(self.gz_windows_fasta)
        self._verify_reads(reader)
