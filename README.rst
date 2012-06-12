Introduction
============

Powerpoint and Excel to HTML transformation

It uses ppthtml and xlhtml which can be installed with e.g:
::
    apt-get install ppthtml xlhtml

or you can obtain the sourcecode from
http://sourceforge.net/projects/chicago/

Installation
============

Add ``collective.transform.ppt_xl`` to the list of eggs to install, e.g.:
::
    [buildout]
    ...
    eggs =
        ...
        collective.transform.ppt_xl


Re-run buildout, e.g. with:
::
    $ ./bin/buildout
