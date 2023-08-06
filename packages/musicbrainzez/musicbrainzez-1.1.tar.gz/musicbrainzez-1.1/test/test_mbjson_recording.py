# coding=utf-8
# Tests for parsing of recording queries

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class GetRecordingTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "recording")

    def testRecordingRelationCreditedAs(self):
        # some performance relations have a "credited-as" attribute
        recording = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "f606f733-c1eb-43f3-93c1-71994ea611e3-artist-rels.json")

        rels = recording["relations"]

        self.assertEqual(4, len(rels))
        # Original attributes
        attributes = rels[0]["attributes"]
        self.assertEqual("piano", attributes[0])

        # New attribute dict format
        attributes = rels[0]["attribute-credits"]
        print(attributes)

        expected = {'piano': 'Yamaha and Steinway pianos'}
        self.assertEqual(expected, attributes)
