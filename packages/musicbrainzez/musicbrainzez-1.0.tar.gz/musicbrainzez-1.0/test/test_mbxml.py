import unittest
from musicbrainzez.parser import mbxml


class MbXML(unittest.TestCase):

    def test_read_error(self):
        error = '<?xml version="1.0" encoding="UTF-8"?><error><text>Invalid mbid.</text><text>For usage, please see: http://musicbrainz.org/development/mmd</text></error>'
        parts = mbxml.get_error_message(error)
        self.assertEqual(2, len(parts))
        self.assertEqual("Invalid mbid.", parts[0])
        self.assertEqual(True, parts[1].startswith("For usage"))
