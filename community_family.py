# -*- coding: utf-8 -*-
"""
Family file for official and sanctioned Fandom Community Centrals

It has few additional options to keep in mind:
- categories will be kept at the bottom of the page, below interwiki (it won't reorder if no changes in that area are needed)
- en interwiki will always be at the top of the list
"""
from pywikibot import family
from pywikibot.tools import deprecated

class Family(family.Family):
    name = 'community'
    langs = {
        'en': 'community.fandom.com',
        'de': 'de.community.fandom.com',
        'es': 'comunidad.fandom.com',
        'fi': 'yhteiso.fandom.com',
        'fr': 'communaute.fandom.com',
        'it': 'it.community.fandom.com',
        'ja': 'ja.community.fandom.com',
        'ko': 'ko.community.fandom.com',
        'nl': 'nl.community.fandom.com',
        'pl': 'spolecznosc.fandom.com',
        'pt': 'comunidade.fandom.com',
        'ru': 'ru.community.fandom.com',
        'vi': 'congdong.fandom.com',
        'zh': 'zh.community.fandom.com'
    }
    languages_by_size = ['en','ru','es','de','pl','fr','pt','zh','it','ja','ko','vi','nl','fi']
    
    @property
    def categories_last(self):
        return self.langs.keys()
    
    @property
    def interwiki_putfirst(self):
        return {k:['en'] for k in self.langs.keys()}
    
    def scriptpath(self, code):
        return ''
    
    @deprecated('APISite.version()')
    def version(self, code):
        return u'1.19.24'

    def protocol(self, code):
        return 'https'