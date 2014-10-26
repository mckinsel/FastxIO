import os
import unittest

from . import TEST_DATA_DIR
from FastxIO import fastx

class TestFastq(unittest.TestCase):

    def setUp(self):
        self.fastq_file = os.path.join(TEST_DATA_DIR, "test.fastq")
        self.gz_fastq_file = os.path.join(TEST_DATA_DIR, "test.fastq.gz")
        self.windows_fastq_file = os.path.join(TEST_DATA_DIR, "test_windows_endings.fastq")
        self.gz_windows_fastq_file = os.path.join(TEST_DATA_DIR, "test_windows_endings.fastq.gz")
    
    def _verify_fastq(self, reader):
        
        rec_list = list(reader)

        self.assertEqual(len(rec_list), 250)

        self.assertEqual(rec_list[0].name, "IRIS:7:1:17:394#0/1")
        self.assertEqual(rec_list[0].sequence, "GTCAGGACAAGAAAGACAANTCCAATTNACATTATG")
        self.assertEqual(rec_list[0].quality, "aaabaa`]baaaaa_aab]D^^`b`aYDW]abaa`^")

        self.assertEqual(rec_list[-1].name, "IRIS:7:1:39:1454#0/1")
        self.assertEqual(rec_list[-1].sequence, "TCATTGCTAAAGACTTGTGTCTTCCCGACCAGAGGG")
        self.assertEqual(rec_list[-1].quality, "abbaaababaaaaaaaaaa`aaa___^__]]^[^^Y")

    def test_read_fastq(self):
        reader = fastx.FastqReader(self.fastq_file)
        self._verify_fastq(reader)
    
    def test_read_fastx(self):
        reader = fastx.FastxReader(self.fastq_file)
        self._verify_fastq(reader)

    def test_read_gz_fastq(self):
        reader = fastx.FastqReader(self.gz_fastq_file)
        self._verify_fastq(reader)
    
    def test_read_gz_fastx(self):
        reader = fastx.FastxReader(self.gz_fastq_file)
        self._verify_fastq(reader)

    def test_read_windows_fastq(self):
        reader = fastx.FastqReader(self.windows_fastq_file)
        self._verify_fastq(reader)
    
    def test_read_windows_fastx(self):
        reader = fastx.FastxReader(self.windows_fastq_file)
        self._verify_fastq(reader)

    def test_read_gz_windows_fastq(self):
        reader = fastx.FastqReader(self.gz_windows_fastq_file)
        self._verify_fastq(reader)
    
    def test_read_gz_windows_fastx(self):
        reader = fastx.FastxReader(self.gz_windows_fastq_file)
        self._verify_fastq(reader)
