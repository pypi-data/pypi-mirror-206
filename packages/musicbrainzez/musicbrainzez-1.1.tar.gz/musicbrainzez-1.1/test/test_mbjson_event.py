# Tests for parsing of event results

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class EventTest(unittest.TestCase):

    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "event")

    def testCorrectId(self):
        event_id = "770fb0b4-0ad8-4774-9275-099b66627355"
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "%s-place-rels.json" % event_id)
        self.assertEqual(event_id, res["id"])

    def testPlace(self):
        event_id = "770fb0b4-0ad8-4774-9275-099b66627355"
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "%s-place-rels.json" % event_id)
        place = res["relations"][0]["place"]
        self.assertEqual("7643f13a-dcda-4db4-8196-3ffcc1b99ab7", place["id"])
        self.assertEqual(50.33556, place["coordinates"]["latitude"])
        self.assertEqual(6.9475, place["coordinates"]["longitude"])

    def testType(self):
        event_id = "770fb0b4-0ad8-4774-9275-099b66627355"
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "%s-place-rels.json" % event_id)
        self.assertEqual("Concert", res["type"])

    def testEventElements(self):
        filename = "e921686d-ba86-4122-bc3b-777aec90d231-tags+artist-rels.json"
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, filename)
        e = res
        keys = ["name", "life-span", "time", "setlist", "relations", "tags"]
        for k in keys:
            self.assertTrue(k in e, "key %s in dict" % (k, ))
