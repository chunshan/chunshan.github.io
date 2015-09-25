#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings
AUTHOR = u'Chunshan'
AUTHOR_EMAIL = u"shan.c.young@gmail.com"
SITENAME = u'MindDemons'
TAGLINE = u'Free Mind'
SITEURL = 'http:/chunshan.github.io'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DEFAULT_METADATA = (
)

DELETE_OUTPUT_DIRECTORY = False

THEME = 'pelican-elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
