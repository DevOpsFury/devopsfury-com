BLOG_AUTHOR = "DevOps Fury"
BLOG_TITLE = "DevOps Fury"
BLOG_DESCRIPTION = "Practical ideas for building, shipping, and running better systems."
BLOG_EMAIL = "hello@devopsfury.com"
COMMENT_SYSTEM = None

SITE_URL = "https://devopsfury.com/"
DEFAULT_LANG = "en"
TIMEZONE = "UTC"

THEME = "devopsfury"
TEMPLATE_ENGINE = "mako"
THEME_COLOR = "#1A1B25"
EXTRA_HEAD_DATA = '<link rel="stylesheet" href="/assets/css/site.css">'

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/#books", "Books"),
        ("/blog/", "Blog"),
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
}
