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
