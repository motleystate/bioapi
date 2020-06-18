import os
from unittest import TestCase

from bioapi.parsers.kegg import KeggPathwayParser


class TestKeggPathwayParser(TestCase):

    def _get_tested_entry(self, file_path):
        input_path = os.path.join(os.path.dirname(__file__), file_path)
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggPathwayParser(test_txt)
        test_parser.parse()
        return test_parser.validated_entry

    def _common_tests(self, tested_entry):
        # Test some of the attribute and content of the file
        self.assertEqual(tested_entry.name, 'Tyrosine metabolism')
        # Test some keys of dictionnary
        self.assertIn('M00042', tested_entry.modules.keys())
        self.assertIn('GO', tested_entry.dblinks.dict().keys())
        self.assertIn('H00163', tested_entry.diseases.keys())
        # Test references
        self.assertEqual(len(tested_entry.references), 4)
        self.assertEqual(tested_entry.references[0].pubmed_id, 8550403)
        self.assertEqual(tested_entry.references[0].doi, "10.1128/JB.178.1.111-120.1996")

    def test_parsing_ko(self):
        tested_entry = self._get_tested_entry('files/example_ko00350.txt')
        self._common_tests(tested_entry)
        # Test specifics
        self.assertEqual(tested_entry.entry_id, 'ko00350')
        # Keys of dict
        self.assertIn('ko00020', tested_entry.related_pathways.keys())
        self.assertIn('C00022', tested_entry.compounds.keys())
        self.assertIn('K14454', tested_entry.orthologs.keys())
        self.assertIn('ko00350', tested_entry.pathway_maps.keys())

    def test_parsing_map(self):
        tested_entry = self._get_tested_entry('files/example_map00350.txt')
        self._common_tests(tested_entry)
        # Test specifics
        self.assertEqual(tested_entry.entry_id, 'map00350')
        self.assertEqual(tested_entry.ko_pathway, 'ko00350')
        # Keys of dict
        self.assertIn('map00020', tested_entry.related_pathways.keys())
        self.assertIn('map00350', tested_entry.pathway_maps.keys())
