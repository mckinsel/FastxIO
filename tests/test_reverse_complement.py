import os
import unittest

from . import TEST_DATA_DIR
from FastxIO import fastx

class TestReverseComplement(unittest.TestCase):

    def setUp(self):

        self.iupac_fasta = os.path.join(TEST_DATA_DIR, "iupac.fasta")
        self.gz_iupac_fasta = os.path.join(TEST_DATA_DIR, "iupac.fasta.gz")
    
    def _verify_rc(self, reader):

        record1 = reader.next()
        record2 = reader.next()
        rv_record = record2.reverseComplement()
        self.assertEqual(record1.sequence, rv_record.sequence)
        
        record3 = reader.next()
        rv_record = record3.reverseComplement()
        self.assertEqual(rv_record.sequence, "AAAAA")

        self.assertRaises(StopIteration, reader.next)

    def test_fasta_rc(self):
        reader = fastx.FastaReader(self.iupac_fasta)
        self._verify_rc(reader)
    
    def test_fastx_rc(self):
        reader = fastx.FastxReader(self.iupac_fasta)
        self._verify_rc(reader)

    def test_gz_fasta_rc(self):
        reader = fastx.FastaReader(self.gz_iupac_fasta)
        self._verify_rc(reader)

    def test_gz_fastx_rc(self):
        reader = fastx.FastxReader(self.gz_iupac_fasta)
        self._verify_rc(reader)
