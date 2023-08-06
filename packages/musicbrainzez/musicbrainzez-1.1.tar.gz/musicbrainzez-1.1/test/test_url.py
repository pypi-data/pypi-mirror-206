# Tests for parsing of release queries

import unittest
import os
import musicbrainzez
from test import _common


class UrlTest(unittest.TestCase):
    """ Test that the correct URL is generated when a search query is made """

    def setUp(self):
        self.opener = _common.FakeOpener("<response/>")
        musicbrainzez.compat.build_opener = lambda *args: self.opener

        musicbrainzez.set_useragent("test", "1")
        musicbrainzez.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.set_rate_limit(True)

    def testGetRelease(self):
        musicbrainzez.get_release_by_id("5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b")
        self.assertEqual("https://musicbrainz.org/ws/2/release/5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b?fmt=json", self.opener.get_url())

        # one include
        musicbrainzez.get_release_by_id("5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b", includes=["artists"])
        self.assertEqual("https://musicbrainz.org/ws/2/release/5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b?fmt=json&inc=artists", self.opener.get_url())

        # more than one include
        musicbrainzez.get_release_by_id("5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b", includes=["artists", "recordings", "artist-credits"])
        expected = "https://musicbrainz.org/ws/2/release/5e3524ca-b4a1-4e51-9ba5-63ea2de8f49b?fmt=json&inc=artists+recordings+artist-credits"
        self.assertEqual(expected, self.opener.get_url())
