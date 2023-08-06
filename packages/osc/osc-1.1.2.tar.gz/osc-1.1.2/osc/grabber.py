# Copyright (C) 2018 SUSE Linux.  All rights reserved.
# This program is free software; it may be used, copied, modified
# and distributed under the terms of the GNU General Public Licence,
# either version 2, or (at your option) any later version.


import os
from urllib.request import HTTPError
from urllib.parse import urlparse
from urllib.parse import unquote
from urllib.error import URLError

import urllib3.exceptions

from .core import streamfile


class OscFileGrabber:
    def __init__(self, progress_obj=None):
        self.progress_obj = progress_obj

    def urlgrab(self, url, filename=None, text=None):
        if filename is None:
            parts = urlparse(url)
            filename = os.path.basename(unquote(parts[2]))
        with open(filename, 'wb') as f:
            for i in streamfile(url, progress_obj=self.progress_obj,
                                text=text):
                f.write(i)


class OscMirrorGroup:
    def __init__(self, grabber, mirrors):
        self._grabber = grabber
        self._mirrors = mirrors

    def urlgrab(self, url, filename=None, text=None):
        for mirror in self._mirrors:
            try:
                self._grabber.urlgrab(mirror, filename, text)
                return True
            except (HTTPError, URLError, urllib3.exceptions.URLSchemeUnknown) as e:
                # try next mirror
                pass

        return False
