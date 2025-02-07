# Change to True if you want document-relative URLs when developing
RELATIVE_URLS = False

AUTHOR = "Ansel Horn"
SITENAME = "Ansel Horn"
SITEURL = "" if RELATIVE_URLS else "https://www.cahorn.net"

COPYRIGHT_NAME = "Colby Ansel Horn"
COPYRIGHT_YEAR = 2025
FAVICON = SITEURL + "/images/favicon.ico"
SITETITLE = "Ansel Horn"
SITESUBTITLE = "Polymath Aspirant"
SITELOGO = SITEURL + "/images/profile.jpg"

MAIN_MENU = True
MENUITEMS = (
    ("Projects", SITEURL + "/category/projects.html"),
)

PATH = "content"
STATIC_PATHS = [
    "images",
    "static",
]

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (
    ("Resume", SITEURL + "/static/resume.pdf"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/cahorn"),
    ("linkedin", "https://www.linkedin.com/in/cahorn"),
)

DEFAULT_PAGINATION = 10

# Use filename as title
FILENAME_METADATA = '(?P<title>.*)'

# Use filesystem timestamp as default date
DEFAULT_DATE = "fs"

# Use Flex theme
THEME = "themes/Flex"
