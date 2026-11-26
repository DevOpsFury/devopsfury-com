# DevOps Fury

The DevOps Fury website is built with [Nikola](https://getnikola.com/). The
landing page is in `files/index.html`; blog entries belong in `posts/` and are
published under `/blog/`.

## Build locally

```sh
python -m pip install -r requirements.txt
nikola build
nikola serve
```

Nikola writes the generated website to `output/`.

The four Linux DevOps Handbook shop links emit a GA4 `book_shop_click` event
with the retailer and outbound URL. Mark `book_shop_click` as a key event in
Google Analytics if you want it counted as a conversion.
