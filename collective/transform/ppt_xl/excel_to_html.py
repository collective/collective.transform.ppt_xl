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


class excel_to_html():
    """Transform which converts from excel to xhtml"""

    if HAS_PLONE3:
        __implements__ = itransform
    else:
        implements(ITransform)

    __name__ = "excel_to_html"
    inputs   = ("application/vnd.ms-excel",)
    output   = "text/html"

    def __init__(self,name=None):
        if name:
            self.__name__=name

    def name(self):
        return self.__name__

    def convert(self, data, cache, **kwargs):
        tmp = NamedTemporaryFile()
        tmp.write(data)
        tmp.flush()
        cmd = ['xlhtml', tmp.name]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        body = bodyfinder(stdout)
        cache.setData(body)
        return cache

def register():
    return excel_to_html()
