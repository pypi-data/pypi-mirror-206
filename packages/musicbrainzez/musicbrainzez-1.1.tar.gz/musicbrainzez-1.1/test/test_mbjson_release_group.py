# Tests for parsing of release queries

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class GetReleaseGroupTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data",
                "release-group")

    # def testTypesExist(self):
    #     rg = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir,
    #                       "f52bc6a1-c848-49e6-85de-f8f53459a624.json")
    #     self.assertTrue("type" in rg)
    #     self.assertTrue("primary-type" in rg)
    #     self.assertTrue("secondary-type-list" in rg)

    # def testTypesResult(self):
    #     rg = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir,
    #                       "f52bc6a1-c848-49e6-85de-f8f53459a624.json")
    #     self.assertEqual("Soundtrack", rg["type"])
    #     self.assertEqual("Album", rg["primary-type"])
    #     self.assertEqual(["Soundtrack"], rg["secondary-type-list"])
