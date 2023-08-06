# Tests for parsing of release queries

import unittest
import os
import musicbrainzez
from musicbrainzez.parser import mbjson
from test import _common


class GetReleaseTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), "data", "release")

    def testArtistCredit(self):
        """
        If the artist credit is the same in the track and recording, make sure that
        the information is replicated in both objects, otherwise have distinct ones.
        """

        # If no artist-credit in the track, copy in the recording one
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "833d4c3a-2635-4b7a-83c4-4e560588f23a-recordings+artist-credits.json")
        tracks = res["media"][0]["tracks"]
        t1 = tracks[1]
        self.assertEqual(t1["artist-credit"], t1["recording"]["artist-credit"])

        # Recording AC is different to track AC
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "fbe4490e-e366-4da2-a37a-82162d2f41a9-recordings+artist-credits.json")
        tracks = res["media"][0]["tracks"]
        t1 = tracks[1]
        self.assertNotEqual(t1["artist-credit"], t1["recording"]["artist-credit"])

    def testTrackId(self):
        """
        Test that the id attribute of tracks is read.
        """
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "212895ca-ee36-439a-a824-d2620cd10461-recordings.json")
        tracks = res["media"][0]["tracks"]
        map(lambda t: self.assertTrue("id" in t), tracks)

    # def testTrackLength(self):
    #     """
    #     Test that if there is a track length, then `track_or_recording_length` has
    #     that, but if not then fill the value from the recording length
    #     """
    #     res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "b66ebe6d-a577-4af8-9a2e-a029b2147716-recordings.json")
    #     tracks = res["media"][0]["tracks"]

    #     # No track length and recording length
    #     t1 = tracks[0]
    #     self.assertTrue("length" not in t1)
    #     self.assertEqual("180000", t1["recording"]["length"])
    #     self.assertEqual("180000", t1["track_or_recording_length"])

    #     # Track length and recording length same
    #     t2 = tracks[1]
    #     self.assertEqual("279000", t2["length"])
    #     self.assertEqual("279000", t2["recording"]["length"])
    #     self.assertEqual("279000", t2["track_or_recording_length"])

    #     # Track length and recording length different
    #     t3 = tracks[2]
    #     self.assertEqual("60000", t3["length"])
    #     self.assertEqual("80000", t3["recording"]["length"])
    #     self.assertEqual("60000", t3["track_or_recording_length"])

    #     # No track lengths
    #     t4 = tracks[3]
    #     self.assertTrue("length" not in t4["recording"])
    #     self.assertTrue("length" not in t4)
    #     self.assertTrue("track_or_recording_length" not in t4)

    def testTrackTitle(self):
        pass

    def testTrackNumber(self):
        """
        Test that track number (number or text) and track position (always an increasing number)
        are both read properly
        """
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "212895ca-ee36-439a-a824-d2620cd10461-recordings.json")
        tracks = res["media"][0]["tracks"]
        # This release doesn't number intro tracks as numbered tracks,
        # so position and number get 'out of sync'
        self.assertEqual([1, 2, 3], [t["position"] for t in tracks[:3]])
        self.assertEqual(['', '1', '2'], [t["number"] for t in tracks[:3]])

        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "a81f3c15-2f36-47c7-9b0f-f684a8b0530f-recordings.json")
        tracks = res["media"][0]["tracks"]
        self.assertEqual([1, 2], [t["position"] for t in tracks])
        self.assertEqual(['A', 'B'], [t["number"] for t in tracks])

        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "9ce41d09-40e4-4d33-af0c-7fed1e558dba-recordings.json")
        tracks = res["media"][0]["data-tracks"]
        self.assertEqual(list(range(1, 199)), [t["position"] for t in tracks])
        self.assertEqual(list(map(str, range(1, 199))), [t["number"] for t in tracks])

    def testVideo(self):
        """
        Test that the video attribute is parsed.
        """
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "fe29e7f0-eb46-44ba-9348-694166f47885-recordings.json")
        trackswithoutvideo = res["media"][0]["tracks"]
        trackswithvideo = res["media"][2]["tracks"]
        map(lambda t: self.assertTrue("video" not in ["recording"]), trackswithoutvideo)
        map(lambda t: self.assertEqual("true", t["recording"]["video"]), trackswithvideo)

    def testPregapTrack(self):
        """
        Test that the pregap track is parsed if it exists.
        """
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "8eb2b179-643d-3507-b64c-29fcc6745156-recordings.json")
        medium = res["media"][0]
        self.assertTrue("pregap" in medium)
        self.assertEqual(0, medium["pregap"]["position"])
        self.assertEqual("0", medium["pregap"]["number"])
        self.assertEqual(35000, medium["pregap"]["length"])
        self.assertEqual("[untitled]", medium["pregap"]["recording"]["title"])

    def testDataTracklist(self):
        """
        Test that data tracklist are parsed.
        """
        res = _common.open_and_parse_test_data(mbjson.JsonParser(), self.datadir, "9ce41d09-40e4-4d33-af0c-7fed1e558dba-recordings.json")
        medium = res["media"][0]
        self.assertTrue("data-tracks" in medium)
        self.assertEqual(198, len(medium["data-tracks"]))
