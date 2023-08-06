#! /usr/bin/env python
# -*- coding: utf-8 -*-

r"""
************************************
Module for capturing terminal output
************************************
"""

import sys
import io

class PrintLog:

    r'''

    Logs the console output that is normally printed to the screen when enabled

    '''

    def __init__(self):
        self._output = io.StringIO()
        self._original = sys.stdout
        self._enabled = False
    def enable(self):
        if self._enabled == False:
            self._enabled = True
            sys.stdout = self._output

    def disable(self):
        if self._enabled == True:
            self._enabled = False
            sys.stdout = self._original

    def get(self):
        return self._output.getvalue()

    def save(self, filename):
        with open(filename, "w") as text:
            text.write(self._output.getvalue())
