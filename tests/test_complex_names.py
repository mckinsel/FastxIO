import os
import unittest

from . import TEST_DATA_DIR
from FastxIO import fastx

class TestComplexNames(unittest.TestCase):

    def setUp(self):
        self.fasta_file = os.path.join(
            TEST_DATA_DIR,
            'other_features_genomic_R64-1-1_20110203.fasta')

        self.gz_fasta_file = os.path.join(
            TEST_DATA_DIR,
            'other_features_genomic_R64-1-1_20110203.fasta.gz')

        self.names_file = os.path.join(
            TEST_DATA_DIR,
            'other_features_genomic_R64-1-1_20110203.names')
    
    def _compare_names(self, reader, names):
        record_count = 0
        for record in reader:
            exp_name = names[record_count][:-1]
            err_msg = ("Expected name '{s}', but the reader returned '{r}'"
                       .format(s=exp_name, r=record.name))
            self.assertEqual(record.name, exp_name, err_msg)

            self.assertEqual(record.quality, "")

            record_count += 1

    def test_names_fasta(self):
        reader = fastx.FastaReader(self.fasta_file)
        names = open(self.names_file).readlines()
        self._compare_names(reader, names)

    def test_names_fastx(self):
        reader = fastx.FastxReader(self.fasta_file)
        names = open(self.names_file).readlines()
        self._compare_names(reader, names)
        
    def test_names_gz_fasta(self):
        reader = fastx.FastaReader(self.gz_fasta_file)
        names = open(self.names_file).readlines()
        self._compare_names(reader, names)

    def test_names_fastx(self):
        reader = fastx.FastxReader(self.gz_fasta_file)
        names = open(self.names_file).readlines()
        self._compare_names(reader, names)
