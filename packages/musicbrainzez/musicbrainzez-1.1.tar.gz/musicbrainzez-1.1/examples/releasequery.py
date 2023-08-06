#!/usr/bin/env python
"""A simple script that searches for a release in the MusicBrainz
database and prints out a few details about the first 5 matching release.

    $ ./releasesearch.py "the beatles" revolver
    Revolver, by The Beatles
    Released 1966-08-08 (Official)
    MusicBrainz ID: b4b04cbf-118a-3944-9545-38a0a88ff1a2
"""
from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzez as mb
import sys

mb.set_useragent(
    "python-mb.example",
    "0.1",
    "python-mb@example.com",
)

mb.set_format("json")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        sys.exit("usage: {} RELEASE_ID [includes]".format(sys.argv[0]))
    release = args[0]
    includes = args[1:]

    result = mb.get_release_by_id(release,
                                           includes=includes)
    print(result.decode("utf-8"))
