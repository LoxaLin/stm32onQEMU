#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate .c file.
"""

__author__     = "Lluís Vilanova <vilanova@ac.upc.edu>"
__copyright__  = "Copyright 2012, Lluís Vilanova <vilanova@ac.upc.edu>"
__license__    = "GPL version 2 or (at your option) any later version"

__maintainer__ = "Stefan Hajnoczi"
__email__      = "stefanha@linux.vnet.ibm.com"


from tracetool import out


def begin(events):
    out('/* This file is autogenerated by tracetool, do not edit. */')
