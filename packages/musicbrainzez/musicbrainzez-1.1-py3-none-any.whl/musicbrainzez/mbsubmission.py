# This file is part of the musicbrainzez library
# Copyright (C) Louis Rannou, Alastair Porter, Adrian Sampson, and others
# This file is distributed under a BSD-2-Clause type license.
# See the COPYING file for more information.

import xml.etree.ElementTree as ET
import logging

from . import util


def fixtag(tag, namespaces):
    # given a decorated tag (of the form {uri}tag), return prefixed
    # tag and namespace declaration, if any
    if isinstance(tag, ET.QName):
        tag = tag.text
    namespace_uri, tag = tag[1:].split("}", 1)
    prefix = namespaces.get(namespace_uri)
    if prefix is None:
        prefix = "ns%d" % len(namespaces)
        namespaces[namespace_uri] = prefix
        if prefix == "xml":
            xmlns = None
        else:
            xmlns = ("xmlns:%s" % prefix, namespace_uri)
    else:
        xmlns = None
    return "%s:%s" % (prefix, tag), xmlns


NS_MAP = {"http://musicbrainz.org/ns/mmd-2.0#": "ws2",
          "http://musicbrainz.org/ns/ext#-2.0": "ext"}
_log = logging.getLogger("musicbrainzez")

def make_artist_credit(artists):
    names = []
    for artist in artists:
        if isinstance(artist, dict):
            if "name" in artist:
                names.append(artist.get("name", ""))
            else:
                names.append(artist.get("artist", {}).get("name", ""))
        else:
                names.append(artist)
    return "".join(names)

###

def make_barcode_request(release2barcode):
    NS = "http://musicbrainz.org/ns/mmd-2.0#"
    root = ET.Element("{%s}metadata" % NS)
    rel_list = ET.SubElement(root, "{%s}release-list" % NS)
    for release, barcode in release2barcode.items():
        rel_xml = ET.SubElement(rel_list, "{%s}release" % NS)
        bar_xml = ET.SubElement(rel_xml, "{%s}barcode" % NS)
        rel_xml.set("{%s}id" % NS, release)
        bar_xml.text = barcode

    return ET.tostring(root, "utf-8")

def make_tag_request(**kwargs):
    NS = "http://musicbrainz.org/ns/mmd-2.0#"
    root = ET.Element("{%s}metadata" % NS)
    for entity_type in ['artist', 'label', 'place', 'recording', 'release', 'release_group', 'work']:
        entity_tags = kwargs.pop(entity_type + '_tags', None)
        if entity_tags is not None:
            e_list = ET.SubElement(root, "{%s}%s-list" % (NS, entity_type.replace('_', '-')))
            for e, tags in entity_tags.items():
                e_xml = ET.SubElement(e_list, "{%s}%s" % (NS, entity_type.replace('_', '-')))
                e_xml.set("{%s}id" % NS, e)
                taglist = ET.SubElement(e_xml, "{%s}user-tag-list" % NS)
                for tag in tags:
                    usertag_xml = ET.SubElement(taglist, "{%s}user-tag" % NS)
                    name_xml = ET.SubElement(usertag_xml, "{%s}name" % NS)
                    name_xml.text = tag
    if kwargs.keys():
        raise TypeError("make_tag_request() got an unexpected keyword argument '%s'" % kwargs.popitem()[0])

    return ET.tostring(root, "utf-8")

def make_rating_request(**kwargs):
    NS = "http://musicbrainz.org/ns/mmd-2.0#"
    root = ET.Element("{%s}metadata" % NS)
    for entity_type in ['artist', 'label', 'recording', 'release_group', 'work']:
        entity_ratings = kwargs.pop(entity_type + '_ratings', None)
        if entity_ratings is not None:
            e_list = ET.SubElement(root, "{%s}%s-list" % (NS, entity_type.replace('_', '-')))
            for e, rating in entity_ratings.items():
                e_xml = ET.SubElement(e_list, "{%s}%s" % (NS, entity_type.replace('_', '-')))
                e_xml.set("{%s}id" % NS, e)
                rating_xml = ET.SubElement(e_xml, "{%s}user-rating" % NS)
                rating_xml.text = str(rating)
    if kwargs.keys():
        raise TypeError("make_rating_request() got an unexpected keyword argument '%s'" % kwargs.popitem()[0])

    return ET.tostring(root, "utf-8")

def make_isrc_request(recording2isrcs):
    NS = "http://musicbrainz.org/ns/mmd-2.0#"
    root = ET.Element("{%s}metadata" % NS)
    rec_list = ET.SubElement(root, "{%s}recording-list" % NS)
    for rec, isrcs in recording2isrcs.items():
        if len(isrcs) > 0:
            rec_xml = ET.SubElement(rec_list, "{%s}recording" % NS)
            rec_xml.set("{%s}id" % NS, rec)
            isrc_list_xml = ET.SubElement(rec_xml, "{%s}isrc-list" % NS)
            isrc_list_xml.set("{%s}count" % NS, str(len(isrcs)))
            for isrc in isrcs:
                isrc_xml = ET.SubElement(isrc_list_xml, "{%s}isrc" % NS)
                isrc_xml.set("{%s}id" % NS, isrc)
    return ET.tostring(root, "utf-8")
