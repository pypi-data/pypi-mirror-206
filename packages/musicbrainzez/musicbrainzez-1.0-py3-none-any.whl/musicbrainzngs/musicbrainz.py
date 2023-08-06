# This file is part of the musicbrainzez library. It is a deprecated interface
# that gives retrocompatibility to the musicbrainzngs library

# Copyright (C) Louis Rannou

from musicbrainzez import musicbrainz as ezmb
from musicbrainzez.parser import mbxml, mbjson

_version = ezmb._version

# Constants
AUTH_YES = ezmb.AUTH_YES
AUTH_NO = ezmb.AUTH_NO
AUTH_IFSET = ezmb.AUTH_IFSET
AUTH_REQUIRED_INCLUDES = ezmb.AUTH_REQUIRED_INCLUDES

# Exceptions.
MusicBrainzError = ezmb.MusicBrainzError
UsageError = ezmb.UsageError
InvalidSearchFieldError = ezmb.InvalidSearchFieldError
InvalidIncludeError = ezmb.InvalidIncludeError
InvalidFilterError = ezmb.InvalidFilterError
WebServiceError = ezmb.WebServiceError
NetworkErrorNetworkError = ezmb.NetworkError
ResponseError = ezmb.ResponseError
AuthenticationError = ezmb.AuthenticationError


# Global authentication and endpoint details.

user = password = ""

def auth(u, p):
	"""Set the username and password to be used in subsequent queries to
	the MusicBrainz XML API that require authentication.
	"""
	global user, password
	user = u
	password = p

set_useragent = ezmb.set_useragent

def set_hostname(new_hostname, use_https=False):
    """Set the hostname for MusicBrainz webservice requests.
    Defaults to 'musicbrainz.org', accessing over https.
    For backwards compatibility, `use_https` is False by default.

    :param str new_hostname: The hostname (and port) of the MusicBrainz server to connect to
    :param bool use_https: `True` if the host should be accessed using https. Default is `False`

    Specify a non-standard port by adding it to the hostname,
    for example 'localhost:8000'."""
    return ezmb.set_hostname(new_hostname, use_https)

set_rate_limit = ezmb.set_rate_limit


# Parsing setup

def mb_parser_xml(resp):
    """Return a Python dict representing the XML response"""
    # Parse the response.
    return mbxml.XmlParser().parse(resp)

def mb_parser_json(resp):
    """Return a Python dict representing the JSON response"""
    # Parse the response.
    return mbjson.JsonParser().parse(resp)

# Defaults
parser_fun = mb_parser_xml
ws_format = "xml"

def set_parser(new_parser_fun=None):
    """Sets the function used to parse the response from the
    MusicBrainz web service.

    If no parser is given, the parser is reset to the default parser
    :func:`mb_parser_xml`.
    """
    global parser_fun
    if new_parser_fun is None:
        new_parser_fun = mb_parser_xml
    if not callable(new_parser_fun):
        raise ValueError("new_parser_fun must be callable")
    parser_fun = new_parser_fun

def set_format(fmt="xml"):
    """Sets the format that should be returned by the Web Service.
    The server currently supports `xml` and `json`.

    This method will set a default parser for the specified format,
    but you can modify it with :func:`set_parser`.

    .. warning:: The json format used by the server is different from
        the json format returned by the `musicbrainzngs` internal parser
        when using the `xml` format! This format may change at any time.
    """
    global ws_format
    if fmt == "xml":
        ws_format = fmt
        set_parser() # set to default
    elif fmt == "json":
        ws_format = fmt
        warn("The json format is non-official and may change at any time")
        set_parser(mb_parser_json)
    else:
        raise ValueError("invalid format: %s" % fmt)

# We need to remind _mb_request and makes a deviation via the ngs _mb_request
_ezmb_mb_request = ezmb._mb_request

def _mb_request(path, method='GET', auth_required=AUTH_NO,
                client_required=False, args=None, data=None, body=None):
    """Makes a request for the specified `path` (endpoint) on /ws/2 on
    the globally-specified hostname. Parses the responses and returns
    the resulting object.  `auth_required` and `client_required` control
    whether exceptions should be raised if the username/password and
    client are left unspecified, respectively.
    """
    global parser_fun

    request_user = None
    request_pw = None

    # Add credentials if required.
    add_auth = False
    if auth_required == AUTH_YES:
        ezmb._log.debug("Auth is required")
        if not user:
            raise UsageError("authorization required; "
                             "use auth(user, pass) first")
        add_auth = True

    if auth_required == AUTH_IFSET and user:
        ezmb._log.debug("Auth is required")
        add_auth = True

    if add_auth:
        request_user = user
        request_pw = password

    # Make request.
    resp = _ezmb_mb_request(path, method, auth_required,
                            client_required, args, data, body, api=ws_format,
                            user=request_user, password=request_pw)

    return parser_fun(resp)

_get_auth_type = ezmb._get_auth_type

def _mb_request_stub(path, method='GET', auth_required=AUTH_NO,
                     client_required=False, args=None, data=None, body=None, api="json",
                     user=None, password=None, client_id=None, access_token=None):
        return _mb_request(path, method, auth_required, client_required, args, data, body)

# The main interface!

# Single entity by ID
def get_area_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_area_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_artist_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_artist_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_instrument_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_instrument_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_label_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_label_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_place_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_place_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_event_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_event_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_recording_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_recording_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_release_by_id(id, includes=[], release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_release_by_id(id, includes, release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_release_group_by_id(id, includes=[],
                            release_status=[], release_type=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_release_group_by_id(id, includes,
                                   release_status, release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_series_by_id(id, includes=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_series_by_id(id, includes, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_work_by_id(id, includes=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_work_by_id(id, includes, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_url_by_id(id, includes=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_url_by_id(id, includes, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret

# Searching
def search_annotations(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('annotation', query, fields, limit, offset, strict, api="xml")
def search_areas(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('area', query, fields, limit, offset, strict, api="xml")
def search_artists(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('artist', query, fields, limit, offset, strict, api="xml")
def search_events(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('event', query, fields, limit, offset, strict, api="xml")
def search_instruments(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('instrument', query, fields, limit, offset, strict, api="xml")
def search_labels(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('label', query, fields, limit, offset, strict, api="xml")
def search_places(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('place', query, fields, limit, offset, strict, api="xml")
def search_recordings(query='', limit=None, offset=None,
                      strict=False, **fields):
    return ezmb._do_mb_search('recording', query, fields, limit, offset, strict, api="xml")
def search_releases(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('release', query, fields, limit, offset, strict, api="xml")
def search_release_groups(query='', limit=None, offset=None,
			  strict=False, **fields):
    return ezmb._do_mb_search('release-group', query, fields, limit, offset, strict, api="xml")
def search_series(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('series', query, fields, limit, offset, strict, api="xml")
def search_works(query='', limit=None, offset=None, strict=False, **fields):
    return ezmb._do_mb_search('work', query, fields, limit, offset, strict, api="xml")


# Lists of entities
def get_releases_by_discid(id, includes=[], toc=None, cdstubs=True, media_format=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_releases_by_discid(id, includes, toc,
                                       cdstubs, media_format, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_recordings_by_isrc(isrc, includes=[], release_status=[],
                           release_type=[], api="xml"):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_recordings_by_isrc(isrc, includes, release_status,
                           release_type, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_works_by_iswc(iswc, includes=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_works_by_iswc(iswc, includes, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret

# Browse methods
# Browse include are a subset of regular get includes, so we check them here
# and the test in _do_mb_query will pass anyway.
def browse_artists(recording=None, release=None, release_group=None,
                   work=None, includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_artists(recording, release, release_group,
                          work, includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_events(area=None, artist=None, place=None,
                  includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_events(area, artist, place,
                         includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_labels(release=None, includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_labels(release, includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_places(area=None, includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_places(area, includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_recordings(artist=None, release=None, includes=[],
                      limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_recordings(artist, release, includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_releases(artist=None, track_artist=None, label=None, recording=None,
                    release_group=None, release_status=[], release_type=[],
                    includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_releases(artist, track_artist, label, recording,
                           release_group, release_status, release_type,
                           includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_release_groups(artist=None, release=None, release_type=[],
                          includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_release_groups(artist, release, release_type,
                         includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_urls(resource=None, includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_urls(resource, includes, limit, offset, api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def browse_works(artist=None, includes=[], limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.browse_works(artist, includes, limit, offset, api="xml")

# Collections
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_collections():
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_collections(api="xml")
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_artists_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_artists_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_releases_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_releases_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_events_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_events_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_places_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_places_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_recordings_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_recordings_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret
def get_works_in_collection(collection, limit=None, offset=None):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.get_works_in_collection(collection, limit, offset)
    ezmb._mb_request = _ezmb_mb_request
    return ret

# Submission methods

def submit_barcodes(release_barcode):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.submit_barcodes(release_barcode)
    ezmb._mb_request = _ezmb_mb_request
    return ret

def submit_isrcs(recording_isrcs):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.submit_isrcs(recording_isrcs)
    ezmb._mb_request = _ezmb_mb_request
    return ret

def submit_tags(**kwargs):
   return ezmb.submit_tags(kwargs)

def submit_ratings(**kwargs):
   return ezmb.submit_ratings(kwargs)

def add_releases_to_collection(collection, releases=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.add_releases_to_collection(collection, releases)
    ezmb._mb_request = _ezmb_mb_request
    return ret

def remove_releases_from_collection(collection, releases=[]):
    ezmb._mb_request = _mb_request_stub
    ret = ezmb.remove_releases_from_collection(collection, releases)
    ezmb._mb_request = _ezmb_mb_request
    return ret
