#!/usr/bin/env python
"""A simple script that searches for a work in the MusicBrainz
database.

    $ ./releasesearch.py WORK_ID series-rel
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
        sys.exit("usage: {} WORK_ID [includes]".format(sys.argv[0]))
    work = args[0]
    includes = args[1:]

    result = mb.get_work_by_id(work,
                                           includes=includes)
    print(result.decode("utf-8"))
