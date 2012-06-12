# -*- coding: utf-8 -*-
from tempfile import NamedTemporaryFile
from subprocess import Popen, PIPE

from zope.interface import implements

from Products.PortalTransforms.interfaces import itransform
from Products.PortalTransforms.libtransforms.utils import bodyfinder

try:
    from Products.PortalTransforms.interfaces import ITransform
    HAS_PLONE3 = False
except ImportError:
    from Products.PortalTransforms.z3.interfaces import ITransform
    HAS_PLONE3 = True


class ppt_to_html():
    """Transform which converts from powerpoint to xhtml"""

    if HAS_PLONE3:
        __implements__ = itransform
    else:
        implements(ITransform)

    __name__ = "ppt_to_html"
    inputs   = ("application/vnd.ms-powerpoint",)
    output   = "text/html"

    def convert(self, data, cache, **kwargs):
        tmp = NamedTemporaryFile()
        tmp.write(data)
        tmp.flush()
        cmd = ['ppthtml', tmp.name]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        body = bodyfinder(stdout)
        cache.setData(body)
        return cache

def register():
    return ppt_to_html()
