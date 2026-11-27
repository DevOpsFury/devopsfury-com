BLOG_AUTHOR = {"en": "Grzegorz S. Adamowicz", "pl": "Grzegorz S. Adamowicz"}
BLOG_TITLE = {"en": "DevOps Fury", "pl": "DevOps Fury"}
BLOG_DESCRIPTION = {
    "en": "Practical ideas for building, shipping, and running better systems.",
    "pl": "Praktyczne pomysły na budowanie, wdrażanie i utrzymywanie lepszych systemów.",
}
BLOG_EMAIL = "hello@devopsfury.com"
COMMENT_SYSTEM = None

SITE_URL = "https://devopsfury.com/"
DEFAULT_LANG = "en"
TRANSLATIONS = {
    "en": "",
    "pl": "/pl",
}
TIMEZONE = "UTC"
DATE_FORMAT = {
    "en": "MMMM d, yyyy",
    "pl": "d MMMM yyyy",
}

THEME = "devopsfury"
TEMPLATE_ENGINE = "mako"
THEME_COLOR = "#1A1B25"
EXTRA_HEAD_DATA = '<link rel="stylesheet" href="/assets/css/site.css">'

NAVIGATION_LINKS = {
    "en": (
        ("/#books", "Books"),
        ("/blog/", "Blog"),
    ),
    "pl": (
        ("/pl/#ksiazki", "Książki"),
        ("/pl/blog/", "Blog"),
    ),
}

POSTS = (("posts/*.md", "blog", "post.tmpl"),)
PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
)

INDEX_PATH = "blog"
PRETTY_URLS = True
STRIP_INDEXES = True

FILES_FOLDERS = {
    "files": "",
    "pl-files": "pl",
}
