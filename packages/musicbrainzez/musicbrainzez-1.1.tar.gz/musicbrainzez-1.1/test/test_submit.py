import unittest
import musicbrainzez
from musicbrainzez import musicbrainz
from test import _common


class SubmitTest(unittest.TestCase):

    def setUp(self):
        self.orig_opener = musicbrainzez.compat.build_opener
        musicbrainz.set_useragent("test_client", "1.0")
        musicbrainz.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.compat.build_opener = self.orig_opener
        musicbrainz._useragent = ""
        musicbrainz._client = ""
        musicbrainz.set_rate_limit(True)

    def test_submit_tags(self):
        self.opener = _common.FakeOpener("<response/>")
        musicbrainzez.compat.build_opener = lambda *args: self.opener
        def make_xml(**kwargs):
            self.assertEqual({'artist_tags': {'mbid': ['one', 'two']}}, kwargs)
        oldmake_tag_request = musicbrainz.mbsubmission.make_tag_request
        musicbrainz.mbsubmission.make_tag_request = make_xml

        musicbrainz.submit_tags(artist_tags={"mbid": ["one", "two"]},
                                user="user", password="password")
        musicbrainz.mbsubmission.make_tag_request = oldmake_tag_request

    def test_submit_single_tag(self):
        self.opener = _common.FakeOpener("<response/>")
        musicbrainzez.compat.build_opener = lambda *args: self.opener
        def make_xml(**kwargs):
            self.assertEqual({'artist_tags': {'mbid': ['single']}}, kwargs)
        oldmake_tag_request = musicbrainz.mbsubmission.make_tag_request
        musicbrainz.mbsubmission.make_tag_request = make_xml

        musicbrainz.submit_tags(artist_tags={"mbid": "single"},
                                user="user", password="password")
        musicbrainz.mbsubmission.make_tag_request = oldmake_tag_request
