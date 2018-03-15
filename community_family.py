# -*- coding: utf-8 -*-
"""
Family file for official and sanctioned FANDOM Community Centrals

It has few additional options to keep in mind:
- categories will be kept at the bottom of the page, below interwiki (it won't reorder if no changes in that area are needed)
- en interwiki will always be at the top of the list
"""
from pywikibot import family
from pywikibot.tools import deprecated

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'community'
        self.langs = {
            'en': 'community.wikia.com',
            'de': 'de.community.wikia.com',
            'es': 'comunidad.wikia.com',
            'fi': 'yhteiso.wikia.com',
            'fr': 'communaute.wikia.com',
            'it': 'it.community.wikia.com',
            'ja': 'ja.community.wikia.com',
            'ko': 'ko.community.wikia.com',
            'nl': 'nl.community.wikia.com',
            'pl': 'spolecznosc.wikia.com',
            'pt': 'comunidade.wikia.com',
            'ru': 'ru.community.wikia.com',
            'vi': 'congdong.wikia.com',
            'zh': 'zh.community.wikia.com'
        }
        self.languages_by_size = ['en','ru','es','de','pl','fr','pt','zh','it','ja','ko','vi','nl','fi']
        self.categories_last = self.langs.keys()
        
        self.interwiki_putfirst = {k:['en'] for k in self.langs.keys()}

    def scriptpath(self, code):
        return ''

    @deprecated('APISite.version()')
    def version(self, code):
        return u'1.19.24'
