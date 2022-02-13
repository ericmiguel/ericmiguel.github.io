AUTHOR = 'Eric M. Ribeiro'
SITESUBTITLE = "Environmental data science"
SITENAME = 'Eric M. Ribeiro'
SITEURL = ''

LOCALE = 'C'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#')
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/ericmiguel'),
    ('Linkedin', '#')
)

DEFAULT_PAGINATION = 12

PLUGIN_PATHS = ['plugins']
PLUGINS = ['simple_footnotes']

# RELATIVE_URLS = True

THEME = 'theme'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'codehilite',
            'linenums': False,
            'use_pygments': True
        }
    }
}
