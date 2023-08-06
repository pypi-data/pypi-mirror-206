import unittest

import musicbrainzez
from test import _common


class BrowseTest(unittest.TestCase):

    def setUp(self):
        self.opener = _common.FakeOpener()
        musicbrainzez.compat.build_opener = lambda *args: self.opener

        musicbrainzez.set_useragent("a", "1")
        musicbrainzez.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.set_rate_limit(True)

    def test_browse(self):
        area = "74e50e58-5deb-4b99-93a2-decbb365c07f"
        musicbrainzez.browse_events(area=area)
        self.assertEqual("https://musicbrainz.org/ws/2/event/?area=74e50e58-5deb-4b99-93a2-decbb365c07f&fmt=json", self.opener.get_url())

    def test_browse_includes(self):
        area = "74e50e58-5deb-4b99-93a2-decbb365c07f"
        musicbrainzez.browse_events(area=area, includes=["aliases", "area-rels"])
        self.assertEqual("https://musicbrainz.org/ws/2/event/?area=74e50e58-5deb-4b99-93a2-decbb365c07f&fmt=json&inc=aliases+area-rels", self.opener.get_url())

    def test_browse_single_include(self):
        area = "74e50e58-5deb-4b99-93a2-decbb365c07f"
        musicbrainzez.browse_events(area=area, includes="aliases")
        self.assertEqual("https://musicbrainz.org/ws/2/event/?area=74e50e58-5deb-4b99-93a2-decbb365c07f&fmt=json&inc=aliases", self.opener.get_url())

    def test_browse_multiple_by(self):
        """It is an error to choose multiple entities to browse by"""
        self.assertRaises(Exception,
                musicbrainzez.browse_artists, recording="1", release="2")

    def test_browse_limit_offset(self):
        """Limit and offset values"""
        area = "74e50e58-5deb-4b99-93a2-decbb365c07f"
        musicbrainzez.browse_events(area=area, limit=50, offset=100)
        self.assertEqual("https://musicbrainz.org/ws/2/event/?area=74e50e58-5deb-4b99-93a2-decbb365c07f&fmt=json&limit=50&offset=100", self.opener.get_url())

    def test_browse_artist(self):
        release = "9ace7c8c-55b4-4c5d-9aa8-e573a5dde9ad"
        musicbrainzez.browse_artists(release=release)
        self.assertEqual("https://musicbrainz.org/ws/2/artist/?fmt=json&release=9ace7c8c-55b4-4c5d-9aa8-e573a5dde9ad", self.opener.get_url())

        recording = "6da2cc31-9b12-4b66-9e26-074150f73406"
        musicbrainzez.browse_artists(recording=recording)
        self.assertEqual("https://musicbrainz.org/ws/2/artist/?fmt=json&recording=6da2cc31-9b12-4b66-9e26-074150f73406", self.opener.get_url())

        release_group = "44c90c72-76b5-3c13-890e-3d37f21c10c9"
        musicbrainzez.browse_artists(release_group=release_group)
        self.assertEqual("https://musicbrainz.org/ws/2/artist/?fmt=json&release-group=44c90c72-76b5-3c13-890e-3d37f21c10c9", self.opener.get_url())

        work = "deb27b88-cf41-4f7c-b3aa-bc3268bc3c02"
        musicbrainzez.browse_artists(work=work)
        self.assertEqual("https://musicbrainz.org/ws/2/artist/?fmt=json&work=deb27b88-cf41-4f7c-b3aa-bc3268bc3c02", self.opener.get_url())

    def test_browse_event(self):
        area = "f03d09b3-39dc-4083-afd6-159e3f0d462f"
        musicbrainzez.browse_events(area=area)
        self.assertEqual("https://musicbrainz.org/ws/2/event/?area=f03d09b3-39dc-4083-afd6-159e3f0d462f&fmt=json", self.opener.get_url())

        artist = "0383dadf-2a4e-4d10-a46a-e9e041da8eb3"
        musicbrainzez.browse_events(artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/event/?artist=0383dadf-2a4e-4d10-a46a-e9e041da8eb3&fmt=json", self.opener.get_url())

        place = "8a6161bb-fb50-4234-82c5-1e24ab342499"
        musicbrainzez.browse_events(place=place)
        self.assertEqual("https://musicbrainz.org/ws/2/event/?fmt=json&place=8a6161bb-fb50-4234-82c5-1e24ab342499", self.opener.get_url())

    def test_browse_label(self):
        release = "c9550260-b7ae-4670-ac24-731c19e76b59"
        musicbrainzez.browse_labels(release=release)
        self.assertEqual("https://musicbrainz.org/ws/2/label/?fmt=json&release=c9550260-b7ae-4670-ac24-731c19e76b59", self.opener.get_url())

    def test_browse_recording(self):
        artist = "47f67b22-affe-4fe1-9d25-853d69bc0ee3"
        musicbrainzez.browse_recordings(artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/recording/?artist=47f67b22-affe-4fe1-9d25-853d69bc0ee3&fmt=json", self.opener.get_url())

        release = "438042ef-7ccc-4d03-9391-4f66427b2055"
        musicbrainzez.browse_recordings(release=release)
        self.assertEqual("https://musicbrainz.org/ws/2/recording/?fmt=json&release=438042ef-7ccc-4d03-9391-4f66427b2055", self.opener.get_url())

    def test_browse_place(self):
        area = "74e50e58-5deb-4b99-93a2-decbb365c07f"
        musicbrainzez.browse_places(area=area)
        self.assertEqual("https://musicbrainz.org/ws/2/place/?area=74e50e58-5deb-4b99-93a2-decbb365c07f&fmt=json", self.opener.get_url())

    def test_browse_release(self):
        artist = "47f67b22-affe-4fe1-9d25-853d69bc0ee3"
        musicbrainzez.browse_releases(artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/release/?artist=47f67b22-affe-4fe1-9d25-853d69bc0ee3&fmt=json", self.opener.get_url())
        musicbrainzez.browse_releases(track_artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/release/?fmt=json&track_artist=47f67b22-affe-4fe1-9d25-853d69bc0ee3", self.opener.get_url())

        label = "713c4a95-6616-442b-9cf6-14e1ddfd5946"
        musicbrainzez.browse_releases(label=label)
        self.assertEqual("https://musicbrainz.org/ws/2/release/?fmt=json&label=713c4a95-6616-442b-9cf6-14e1ddfd5946", self.opener.get_url())

        recording = "7484fcfd-1968-4401-a44d-d1edcc580518"
        musicbrainzez.browse_releases(recording=recording)
        self.assertEqual("https://musicbrainz.org/ws/2/release/?fmt=json&recording=7484fcfd-1968-4401-a44d-d1edcc580518", self.opener.get_url())

        release_group = "1c1b54f7-e56a-3ce8-b62c-e45c378e7f76"
        musicbrainzez.browse_releases(release_group=release_group)
        self.assertEqual("https://musicbrainz.org/ws/2/release/?fmt=json&release-group=1c1b54f7-e56a-3ce8-b62c-e45c378e7f76", self.opener.get_url())

    def test_browse_release_group(self):
        artist = "47f67b22-affe-4fe1-9d25-853d69bc0ee3"
        musicbrainzez.browse_release_groups(artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/?artist=47f67b22-affe-4fe1-9d25-853d69bc0ee3&fmt=json", self.opener.get_url())

        release = "438042ef-7ccc-4d03-9391-4f66427b2055"
        musicbrainzez.browse_release_groups(release=release)
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/?fmt=json&release=438042ef-7ccc-4d03-9391-4f66427b2055", self.opener.get_url())

        release = "438042ef-7ccc-4d03-9391-4f66427b2055"
        rel_type = "ep"
        musicbrainzez.browse_release_groups(release=release, release_type=rel_type)
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/?fmt=json&release=438042ef-7ccc-4d03-9391-4f66427b2055&type=ep", self.opener.get_url())

    def test_browse_url(self):
        resource = "http://www.queenonline.com"
        musicbrainzez.browse_urls(resource=resource)
        self.assertEqual("https://musicbrainz.org/ws/2/url/?fmt=json&resource=http%3A%2F%2Fwww.queenonline.com", self.opener.get_url())

        # Resource is urlencoded, including ? and =
        resource = "http://www.splendidezine.com/review.html?reviewid=1109588405202831"
        musicbrainzez.browse_urls(resource=resource)
        self.assertEqual("https://musicbrainz.org/ws/2/url/?fmt=json&resource=http%3A%2F%2Fwww.splendidezine.com%2Freview.html%3Freviewid%3D1109588405202831", self.opener.get_url())

    def test_browse_work(self):
        artist = "0383dadf-2a4e-4d10-a46a-e9e041da8eb3"
        musicbrainzez.browse_works(artist=artist)
        self.assertEqual("https://musicbrainz.org/ws/2/work/?artist=0383dadf-2a4e-4d10-a46a-e9e041da8eb3&fmt=json", self.opener.get_url())

    def test_browse_includes_is_subset_of_includes(self):
        """Check that VALID_BROWSE_INCLUDES is a strict subset of
           VALID_INCLUDES"""
        for entity, includes in musicbrainzez.VALID_BROWSE_INCLUDES.items():
            for i in includes:
                self.assertTrue(i in musicbrainzez.VALID_INCLUDES[entity], "entity %s, %s in BROWSE_INCLUDES but not VALID_INCLUDES" % (entity, i))
