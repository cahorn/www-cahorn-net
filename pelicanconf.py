# Change to True if you want document-relative URLs when developing
RELATIVE_URLS = False

AUTHOR = "Ansel Horn"
SITENAME = "Ansel Horn"
SITEURL = "" if RELATIVE_URLS else "https://www.cahorn.net"

SITELOGO = SITEURL + "/images/profile.jpg"

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Use filename as title
FILENAME_METADATA = '(?P<title>.*)'

# Use filesystem timestamp as default date
DEFAULT_DATE = "fs"

# Use Flex theme
THEME = "themes/Flex"
