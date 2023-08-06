# Tests for parsing of artist queries

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class GetArtistTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "artist")

    def testArtistAliases(self):
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "0e43fe9d-c472-4b62-be9e-55f971a023e1-aliases.json")
        aliases = res["aliases"]
        self.assertEqual(len(aliases), 34)

        a1 = aliases[1]
        self.assertEqual(a1["name"], "Prokofief")
        self.assertEqual(a1["sort-name"], "Prokofief")

        a17 = aliases[15]
        self.assertEqual(a17["name"], "Sergei Prokofiev")
        self.assertEqual(a17["sort-name"], "Prokofiev, Sergei")
        self.assertEqual(a17["locale"], "en")
        self.assertTrue(a17["primary"])

        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "2736bad5-6280-4c8f-92c8-27a5e63bbab2-aliases.json")
        self.assertFalse("alias" in res)

    def testArtistTargets(self):
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "b3785a55-2cf6-497d-b8e3-cfa21a36f997-artist-rels.json")
        self.assertTrue('target-credit' in res['relations'][0])
        self.assertEqual(res['relations'][2]["target-credit"], "TAO")
