import unittest

import musicbrainzez
from test import _common


class SearchUrlTest(unittest.TestCase):
    """ Test that the correct URL is generated when a search query is made """

    def setUp(self):
        self.opener = _common.FakeOpener("<response/>")
        musicbrainzez.compat.build_opener = lambda *args: self.opener

        musicbrainzez.set_useragent("a", "1")
        musicbrainzez.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.set_rate_limit(True)

    def test_search_annotations(self):
        musicbrainzez.search_annotations("Pieds")
        self.assertEqual("https://musicbrainz.org/ws/2/annotation/?fmt=json&query=Pieds", self.opener.get_url())

        # Query fields
        musicbrainzez.search_annotations(entity="bdb24cb5-404b-4f60-bba4-7b730325ae47")
        # TODO: We escape special characters and then urlencode all query parameters, which may
        # not be necessary, but MusicBrainz accepts it and appears to return the same value as without
        expected_query = r'entity:(bdb24cb5\-404b\-4f60\-bba4\-7b730325ae47)'
        expected = 'https://musicbrainz.org/ws/2/annotation/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_annotations(foo="value")

    def test_search_artists(self):
        musicbrainzez.search_artists("Dynamo Go")
        self.assertEqual("https://musicbrainz.org/ws/2/artist/?fmt=json&query=Dynamo+Go", self.opener.get_url())

        musicbrainzez.search_artists(artist="Dynamo Go")
        expected_query = 'artist:(dynamo go)'
        expected = 'https://musicbrainz.org/ws/2/artist/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_artists(foo="value")

    def test_search_events(self):
        musicbrainzez.search_events("woodstock")
        self.assertEqual("https://musicbrainz.org/ws/2/event/?fmt=json&query=woodstock", self.opener.get_url())

        musicbrainzez.search_events(event="woodstock")
        expected_query = 'event:(woodstock)'
        expected = 'https://musicbrainz.org/ws/2/event/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_events(foo="value")

    def test_search_labels(self):
        musicbrainzez.search_labels("Waysafe")
        self.assertEqual("https://musicbrainz.org/ws/2/label/?fmt=json&query=Waysafe", self.opener.get_url())

        musicbrainzez.search_labels(label="Waysafe")
        expected_query = 'label:(waysafe)'
        expected = 'https://musicbrainz.org/ws/2/label/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_labels(foo="value")

    def test_search_places(self):
        musicbrainzez.search_places("Fillmore")
        self.assertEqual("https://musicbrainz.org/ws/2/place/?fmt=json&query=Fillmore", self.opener.get_url())

        musicbrainzez.search_places(place="Fillmore")
        expected_query = 'place:(fillmore)'
        expected = 'https://musicbrainz.org/ws/2/place/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_places(foo="value")

    def test_search_releases(self):
        musicbrainzez.search_releases("Affordable Pop Music")
        self.assertEqual("https://musicbrainz.org/ws/2/release/?fmt=json&query=Affordable+Pop+Music", self.opener.get_url())

        musicbrainzez.search_releases(release="Affordable Pop Music")
        expected_query = 'release:(affordable pop music)'
        expected = 'https://musicbrainz.org/ws/2/release/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_releases(foo="value")

    def test_search_release_groups(self):
        musicbrainzez.search_release_groups("Affordable Pop Music")
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/?fmt=json&query=Affordable+Pop+Music", self.opener.get_url())

        musicbrainzez.search_release_groups(releasegroup="Affordable Pop Music")
        expected_query = 'releasegroup:(affordable pop music)'
        expected = 'https://musicbrainz.org/ws/2/release-group/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_release_groups(foo="value")

    def test_search_recordings(self):
        musicbrainzez.search_recordings("Thief of Hearts")
        self.assertEqual("https://musicbrainz.org/ws/2/recording/?fmt=json&query=Thief+of+Hearts", self.opener.get_url())

        musicbrainzez.search_recordings(recording="Thief of Hearts")
        expected_query = 'recording:(thief of hearts)'
        expected = 'https://musicbrainz.org/ws/2/recording/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_recordings(foo="value")

    def test_search_works(self):
        musicbrainzez.search_works("Fountain City")
        self.assertEqual("https://musicbrainz.org/ws/2/work/?fmt=json&query=Fountain+City", self.opener.get_url())

        musicbrainzez.search_works(work="Fountain City")
        expected_query = 'work:(fountain city)'
        expected = 'https://musicbrainz.org/ws/2/work/?fmt=json&query=%s' % musicbrainzez.compat.quote_plus(expected_query)
        self.assertEqual(expected, self.opener.get_url())

        # Invalid query field
        with self.assertRaises(musicbrainzez.InvalidSearchFieldError):
            musicbrainzez.search_works(foo="value")
