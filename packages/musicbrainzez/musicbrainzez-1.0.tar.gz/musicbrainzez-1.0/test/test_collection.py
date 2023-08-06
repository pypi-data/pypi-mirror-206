import unittest
import musicbrainzez
from musicbrainzez import compat
from test import _common


class CollectionTest(unittest.TestCase):
    """ Test that requesting collections works properly """

    def setUp(self):
        musicbrainzez.set_useragent("a", "1")
        musicbrainzez.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.set_rate_limit(True)

    def test_auth_required(self):
        """ Check the auth_required method in isolation """
        ar = musicbrainzez.musicbrainz._get_auth_type("collection", "", [])
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_YES, ar)

        ar = musicbrainzez.musicbrainz._get_auth_type("collection",
                "foo/releases", [])
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_IFSET, ar)

        ar = musicbrainzez.musicbrainz._get_auth_type("artist", "5b11f4ce-a62d-471e-81fc-a69a8278c7da", [])
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_NO, ar)

        ar = musicbrainzez.musicbrainz._get_auth_type("artist", "5b11f4ce-a62d-471e-81fc-a69a8278c7da", ["user-tags"])
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_YES, ar)

        ar = musicbrainzez.musicbrainz._get_auth_type("artist", "5b11f4ce-a62d-471e-81fc-a69a8278c7da", ["aliases", "user-genres", "artist-rels"])
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_YES, ar)

    def test_my_collections(self):
        """ If you ask for your collections, you need to have
        authenticated first."""

        old_mb_request = musicbrainzez.musicbrainz._mb_request

        params = {}
        def local_mb_request(path, method='GET',
                auth_required=musicbrainzez.musicbrainz.AUTH_NO,
                client_required=False, args=None, data=None, body=None, api="json",
                user=None, password=None, client_id=None, access_token=None):
            params["auth_required"] = auth_required

        musicbrainzez.musicbrainz._mb_request = local_mb_request
        musicbrainzez.get_collections()
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_YES,
            params["auth_required"])

        musicbrainzez.musicbrainz._mb_request = old_mb_request

    def test_other_collection(self):
        """ If you ask for someone else's collection, you don't
        need to be authenticated."""

        old_mb_request = musicbrainzez.musicbrainz._mb_request

        params = {}
        def local_mb_request(path, method='GET',
                auth_required=musicbrainzez.musicbrainz.AUTH_NO,
                client_required=False, args=None, data=None, body=None, api="json",
                user=None, password=None, client_id=None, access_token=None):
            params["auth_required"] = auth_required

        musicbrainzez.musicbrainz._mb_request = local_mb_request
        musicbrainzez.get_releases_in_collection(
                "17905fdb-102d-40f0-91d3-eabcabc64fd3")
        # If _get_auth_type() returns AUTH_IFSET, then _mb_request()
        # should send the user credentials
        self.assertEqual(musicbrainzez.musicbrainz.AUTH_IFSET,
                params["auth_required"])

        musicbrainzez.musicbrainz._mb_request = old_mb_request

    def test_no_collection(self):
        """ If a collection doesn't exist, you get a 404 """

        exc = compat.HTTPError("", 404, "", "", _common.StringIO.StringIO(""))
        self.opener = _common.FakeOpener(exception=musicbrainzez.ResponseError(cause=exc))
        musicbrainzez.compat.build_opener = lambda *args: self.opener
        try:
            res = musicbrainzez.get_releases_in_collection("17905fdb-102d-40f0-91d3-eabcabc64f44")
            self.assertTrue(False, "Expected an exception")
        except musicbrainzez.ResponseError as e:
            self.assertEqual(e.cause.code, 404)

    def test_private_collection(self):
        """ If you ask for a collection that is private, you should
        get a 401"""

        exc = compat.HTTPError("", 401, "", "", _common.StringIO.StringIO(""))
        self.opener = _common.FakeOpener(exception=musicbrainzez.AuthenticationError(cause=exc))
        musicbrainzez.compat.build_opener = lambda *args: self.opener
        try:
            res = musicbrainzez.get_releases_in_collection("17905fdb-102d-40f0-91d3-eabcabc64fd3")
            self.assertTrue(False, "Expected an exception")
        except musicbrainzez.AuthenticationError as e:
            self.assertEqual(e.cause.code, 401)
