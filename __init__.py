# -*- coding: utf-8 -*-

'''Convert English vocals to spanish with accent mark.

Synopsis: sc <char | key>'''

from albert import *

__title__ = 'Spanish Characters'
__version__ = '0.4.1'
__triggers__ = 'la '
__authors__ = 'dantehemerson'

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
 "N": "Ñ",
 "n": "ñ",
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
        item.text = "Alternative Character Not Found"
        item.subtext = 'Type some character'
        success = False

    if success:
        item.addAction(ClipAction('Copy result to clipboard', result))

    return item

