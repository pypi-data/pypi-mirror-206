import unittest
import musicbrainzez
from test import _common


class UrlTest(unittest.TestCase):
    """ Test that the correct URL is generated when a search query is made """

    def setUp(self):
        self.opener = _common.FakeOpener("<response/>")
        musicbrainzez.compat.build_opener = lambda *args: self.opener

        musicbrainzez.set_useragent("a", "1")
        musicbrainzez.set_rate_limit(False)

    def tearDown(self):
        musicbrainzez.set_rate_limit(True)

    def testGetArtist(self):
        artistid = "952a4205-023d-4235-897c-6fdb6f58dfaa"
        musicbrainzez.get_artist_by_id(artistid)
        self.assertEqual("https://musicbrainz.org/ws/2/artist/952a4205-023d-4235-897c-6fdb6f58dfaa?fmt=json", self.opener.get_url())

        # Test an include
        musicbrainzez.get_artist_by_id(artistid, "recordings")
        self.assertEqual("https://musicbrainz.org/ws/2/artist/952a4205-023d-4235-897c-6fdb6f58dfaa?fmt=json&inc=recordings", self.opener.get_url())

        # More than one include
        musicbrainzez.get_artist_by_id(artistid, ["recordings", "aliases"])
        expected ="https://musicbrainz.org/ws/2/artist/952a4205-023d-4235-897c-6fdb6f58dfaa?fmt=json&inc=recordings+aliases"
        self.assertEqual(expected, self.opener.get_url())

        # with valid filters
        musicbrainzez.get_artist_by_id(artistid, ["release-groups"],
                release_type=["album"])
        self.assertTrue("type=album" in self.opener.get_url())

        # with invalid filters
        self.assertRaises(musicbrainzez.UsageError,
                musicbrainzez.get_artist_by_id,
                artistid, ["release-groups"], release_status=["official"])

    def testGetEvent(self):
        event_id = "a4a0927c-8ad7-48dd-883c-7126cc0b9c6b"
        musicbrainzez.get_event_by_id(event_id)
        self.assertEqual("https://musicbrainz.org/ws/2/event/a4a0927c-8ad7-48dd-883c-7126cc0b9c6b?fmt=json", self.opener.get_url())

        # one include
        musicbrainzez.get_event_by_id(event_id, ["artist-rels"])
        self.assertEqual("https://musicbrainz.org/ws/2/event/a4a0927c-8ad7-48dd-883c-7126cc0b9c6b?fmt=json&inc=artist-rels", self.opener.get_url())

        musicbrainzez.get_event_by_id(event_id, ["artist-rels", "event-rels", "ratings", "tags"])
        self.assertEqual("https://musicbrainz.org/ws/2/event/a4a0927c-8ad7-48dd-883c-7126cc0b9c6b?fmt=json&inc=artist-rels+event-rels+ratings+tags", self.opener.get_url())

    def testGetPlace(self):
        place_id = "43e166a5-a024-4cbb-9a1f-d4947b4ff489"
        musicbrainzez.get_place_by_id(place_id)
        self.assertEqual("https://musicbrainz.org/ws/2/place/43e166a5-a024-4cbb-9a1f-d4947b4ff489?fmt=json", self.opener.get_url())

        musicbrainzez.get_place_by_id(place_id, ["event-rels"])
        self.assertEqual("https://musicbrainz.org/ws/2/place/43e166a5-a024-4cbb-9a1f-d4947b4ff489?fmt=json&inc=event-rels", self.opener.get_url())

    def testGetLabel(self):
        label_id = "aab2e720-bdd2-4565-afc2-460743585f16"
        musicbrainzez.get_label_by_id(label_id)
        self.assertEqual("https://musicbrainz.org/ws/2/label/aab2e720-bdd2-4565-afc2-460743585f16?fmt=json", self.opener.get_url())

        # one include
        musicbrainzez.get_label_by_id(label_id, "releases")
        self.assertEqual("https://musicbrainz.org/ws/2/label/aab2e720-bdd2-4565-afc2-460743585f16?fmt=json&inc=releases", self.opener.get_url())

        # with valid filters
        musicbrainzez.get_label_by_id(label_id, ["releases"],
                release_type=["ep", "single"], release_status=["official"])
        self.assertTrue("type=ep%7Csingle" in self.opener.get_url())
        self.assertTrue("status=official" in self.opener.get_url())

    def testGetRecording(self):
        musicbrainzez.get_recording_by_id("93468a09-9662-4886-a227-56a2ad1c5246")
        self.assertEqual("https://musicbrainz.org/ws/2/recording/93468a09-9662-4886-a227-56a2ad1c5246?fmt=json", self.opener.get_url())

        # one include
        musicbrainzez.get_recording_by_id("93468a09-9662-4886-a227-56a2ad1c5246", includes=["artists"])
        self.assertEqual("https://musicbrainz.org/ws/2/recording/93468a09-9662-4886-a227-56a2ad1c5246?fmt=json&inc=artists", self.opener.get_url())


    def testGetReleasegroup(self):
        musicbrainzez.get_release_group_by_id("9377d65d-ffd5-35d6-b64d-43f86ef9188d")
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/9377d65d-ffd5-35d6-b64d-43f86ef9188d?fmt=json", self.opener.get_url())

        # one include
        release_group_id = "9377d65d-ffd5-35d6-b64d-43f86ef9188d"
        musicbrainzez.get_release_group_by_id(release_group_id,
                includes=["artists"])
        self.assertEqual("https://musicbrainz.org/ws/2/release-group/9377d65d-ffd5-35d6-b64d-43f86ef9188d?fmt=json&inc=artists", self.opener.get_url())

        # with valid filters
        musicbrainzez.get_release_group_by_id(release_group_id,
                release_type=["compilation", "live"])
        self.assertTrue("type=compilation%7Clive" in self.opener.get_url())

        # with invalid filters
        self.assertRaises(musicbrainzez.UsageError,
                musicbrainzez.get_release_group_by_id,
                release_group_id, release_status=["official", "promotion"])


    def testGetWork(self):
        musicbrainzez.get_work_by_id("c6dfad5a-f915-41c7-a1c0-e2b606948e69")
        self.assertEqual("https://musicbrainz.org/ws/2/work/c6dfad5a-f915-41c7-a1c0-e2b606948e69?fmt=json", self.opener.get_url())

    def testGetByDiscid(self):
        musicbrainzez.get_releases_by_discid("I5l9cCSFccLKFEKS.7wqSZAorPU-")
        self.assertEqual("https://musicbrainz.org/ws/2/discid/I5l9cCSFccLKFEKS.7wqSZAorPU-?fmt=json", self.opener.get_url())

        includes = ["artists"]
        musicbrainzez.get_releases_by_discid("I5l9cCSFccLKFEKS.7wqSZAorPU-", includes)
        self.assertEqual("https://musicbrainz.org/ws/2/discid/I5l9cCSFccLKFEKS.7wqSZAorPU-?fmt=json&inc=artists", self.opener.get_url())

        musicbrainzez.get_releases_by_discid("discid", toc="toc")
        self.assertEqual("https://musicbrainz.org/ws/2/discid/discid?fmt=json&toc=toc", self.opener.get_url())

        musicbrainzez.get_releases_by_discid("discid", toc="toc", cdstubs=False)
        self.assertEqual("https://musicbrainz.org/ws/2/discid/discid?cdstubs=no&fmt=json&toc=toc", self.opener.get_url())


    def testGetInstrument(self):

        musicbrainzez.get_instrument_by_id("6505f98c-f698-4406-8bf4-8ca43d05c36f")
        self.assertEqual("https://musicbrainz.org/ws/2/instrument/6505f98c-f698-4406-8bf4-8ca43d05c36f?fmt=json", self.opener.get_url())

        # Tags
        musicbrainzez.get_instrument_by_id("6505f98c-f698-4406-8bf4-8ca43d05c36f", includes="tags")
        self.assertEqual("https://musicbrainz.org/ws/2/instrument/6505f98c-f698-4406-8bf4-8ca43d05c36f?fmt=json&inc=tags", self.opener.get_url())

        # some rels
        musicbrainzez.get_instrument_by_id("6505f98c-f698-4406-8bf4-8ca43d05c36f", includes=["instrument-rels", "url-rels"])
        self.assertEqual("https://musicbrainz.org/ws/2/instrument/6505f98c-f698-4406-8bf4-8ca43d05c36f?fmt=json&inc=instrument-rels+url-rels", self.opener.get_url())

        # alias, annotation
        musicbrainzez.get_instrument_by_id("d00cec5f-f9bc-4235-a54f-6639a02d4e4c", includes=["aliases", "annotation"])
        self.assertEqual("https://musicbrainz.org/ws/2/instrument/d00cec5f-f9bc-4235-a54f-6639a02d4e4c?fmt=json&inc=aliases+annotation", self.opener.get_url())

        # Ratings are used on almost all other entites but instrument
        self.assertRaises(musicbrainzez.UsageError,
                musicbrainzez.get_instrument_by_id,
                "dabdeb41-560f-4d84-aa6a-cf22349326fe", includes=["ratings"])

