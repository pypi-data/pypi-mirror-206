# This file is part of the musicbrainzez library. It is a deprecated interface
# that gives retrocompatibility to the musicbrainzngs library

# Copyright (C) Louis Rannou

from musicbrainzez import caa as ezcaa

def set_caa_hostname(new_hostname, use_https=False):
    return ezcaa.set_caa_hostname(new_hostname, use_https)

get_image_list = ezcaa.get_image_list
get_release_group_image_list = ezcaa.get_release_group_image_list
get_release_group_image_front = ezcaa.get_release_group_image_front
get_image_front = ezcaa.get_image_front
get_image_back = ezcaa.get_image_back
get_image = ezcaa.get_image
