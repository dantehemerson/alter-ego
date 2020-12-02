# -*- coding: utf-8 -*-

'''Convert some ASCII characters to mapped special characters.

Synopsis: <trigger> <char | key>'''

from albertv0 import *

__iid__ = 'PythonInterface/v0.1'
__prettyname__ = 'Alter Ego'
__version__ = '0.1'
__trigger__ = 'c'
__author__ = 'Dante Calderon'

specialChars = {
 "a": "á",
 "e": "é",
 "o": "ó",
 "i": "í",
 "u": "ú",
 "A": "Á",
 "E": "É",
 "I": "Í",
 "O": "Ó",
 "U": "Ú",
 # I need add macros
 "`": "~",
 "q": "~",
}

def handleQuery(query):
    if not query.isTriggered:
        return

    item = Item(completion=query.rawString)
    stripped = query.string.strip()

    success = False
    if stripped:
        result = specialChars.get(stripped)
        if result is not None:
            item.text = result
            item.subtext = 'Result'
            success = True

    if not success:
        item.text = "Not Found"
        item.subtext = 'Type some character'
        success = False

    if success:
        item.addAction(ClipAction('Copy result to clipboard', result))

    return item