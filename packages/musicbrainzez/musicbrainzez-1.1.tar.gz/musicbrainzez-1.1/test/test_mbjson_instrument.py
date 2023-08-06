# coding=utf-8
# Tests for parsing instrument queries

import unittest
import os
from test import _common
from musicbrainzez.parser import mbjson


class GetInstrumentTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "instrument")

    def testData(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "9447c0af-5569-48f2-b4c5-241105d58c91.json")

        self.assertEqual(inst["id"], "9447c0af-5569-48f2-b4c5-241105d58c91")
        self.assertEqual(inst["name"], "bass saxophone")
        self.assertEqual(inst["type"], "Wind instrument")
        self.assertTrue(inst["description"].startswith("Second largest and lowest"))

    def testAliases(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "6505f98c-f698-4406-8bf4-8ca43d05c36f-aliases.json")

        aliases = inst["aliases"]
        self.assertEqual(len(aliases), 14)
        self.assertEqual(aliases[1]["locale"], "it")
        self.assertEqual(aliases[1]["type"], "Instrument name")
        self.assertTrue(aliases[1]["primary"])
        self.assertEqual(aliases[1]["sort-name"], "Basso")
        self.assertEqual(aliases[1]["name"], "Basso")


    def testTags(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "6505f98c-f698-4406-8bf4-8ca43d05c36f-tags.json")

        tags = inst["tags"]
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[0]["name"], "contra")
        self.assertEqual(tags[0]["count"], 1)

    def testUrlRels(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "d00cec5f-f9bc-4235-a54f-6639a02d4e4c-url-rels.json")

        rels = inst["relations"]
        self.assertEqual(len(rels), 4)
        self.assertEqual(rels[1]["type"], "information page")
        self.assertEqual(rels[1]["type-id"], "0e62afec-12f3-3d0f-b122-956207839854")
        self.assertTrue(rels[1]["url"]["resource"].startswith("https://en.wikisource"))

    # def testAnnotations(self):
    #     inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "d00cec5f-f9bc-4235-a54f-6639a02d4e4c-annotation.json")
    #     self.assertEqual(inst["annotation"]["text"], "Hornbostel-Sachs: 412.22")

    def testInstrumentRels(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "01ba56a2-4306-493d-8088-c7e9b671c74e-instrument-rels.json")

        rels = inst["relations"]
        self.assertEqual(len(rels), 3)
        self.assertEqual(rels[0]["type"], "children")
        self.assertEqual(rels[0]["type-id"], "12678b88-1adb-3536-890e-9b39b9a14b2d")
        self.assertEqual(rels[0]["instrument"]["id"], "ad09a4ed-d1b6-47c3-ac85-acb531244a4d")
        self.assertTrue(rels[0]["instrument"]["name"].startswith(b"kemen\xc3\xa7e".decode("utf-8")))

    def testDisambiguation(self):
        inst = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "dabdeb41-560f-4d84-aa6a-cf22349326fe.json")
        self.assertEqual(inst["disambiguation"], "lute")
