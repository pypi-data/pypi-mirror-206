# Tests for parsing of label queries

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class GetLabelTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "label")

    def testLabelAliases(self):
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "022fe361-596c-43a0-8e22-bad712bb9548-aliases.json")
        aliases = res["aliases"]
        self.assertEqual(len(aliases), 5)

        a0 = aliases[0]
        self.assertEqual(a0["name"], "EMI")
        self.assertEqual(a0["sort-name"], "EMI")

        a3 = aliases[3]
        self.assertEqual(a3["name"], "EMI Records (UK)")
        self.assertEqual(a3["sort-name"], "EMI Records (UK)")

        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "e72fabf2-74a3-4444-a9a5-316296cbfc8d-aliases.json")
        aliases = res["aliases"]
        self.assertEqual(len(aliases), 2)

        a0 = aliases[0]
        self.assertEqual(a0["name"], "Ki/oon Records Inc.")
        self.assertEqual(a0["sort-name"], "Ki/oon Records Inc.")
        self.assertEqual(a0["begin"], "2001-10")
        self.assertEqual(a0["end"], "2012-04")


