# Worklog: Learn Jekyll Templating - 2023-02-02

## Prerequisite

Running jekyll serve locally in docker via the Makefile included in this repo

## Showing ~Posts~ Site.Pages


### Jekyll Doc

<https://jekyllrb.com/docs/posts/#displaying-an-index-of-posts>

Tried following this, but there's a lot of overhead in arranging the posts _just so_, learning the templating system, etc, and as a result the initial experiment didn't work.

### Copypasta from minima

The default GH pages theme, minima, shows the posts by default, purely based on markdown files in directories, without requiring special naming conventions or metadata (`frontmatter`).

If set theme locally to `minima`, the page gets rendered with links to md pages in subdirs; names appear to be based off of the h1 headers.
```html
<body><header class="site-header" role="banner">
  <div class="wrapper"><a class="site-title" rel="author" href="/">yoinkbird.github.io</a><nav class="site-nav">
        <input type="checkbox" id="nav-trigger" class="nav-trigger" />
        <!-- ... -->
        <div class="trigger"><a class="page-link" href="/blog/cyclesafe/webenable.html">Goal</a><a class="page-link" href="/blog/datalearn/misc.html">perldb</a><a class="page-link" href="/blog/datalearn/studynotes_kubernetes_docker.html">https://github.com/PipelineAI/pipeline/tree/master/docs/quickstart/kubernetes</a><a class="page-link" href="/blog/datalearn/studynotes_spark.html">Apache Spark</a><a class="page-link" href="/blog/worklogs/learn_jekyll_templating.html">Learn Jekyll Templating</a><a class="page-link" href="/blog/worklogs/overhaul_gh_pages.html">Overhaul of the GitHub Pages Website</a><a class="page-link" href="/">YoinkBird</a></div>
      </nav></div>
</header>
```

Reading the `minima` docs <https://github.com/jekyll/minima#layouts> , it should be possible to just copy in the layout files locally to get more control, iterate, and determine how to transfer this templating over to the `slate` theme.


obtain locally:
```bash
mkdir _layouts && cd _layouts
curl -O https://raw.githubusercontent.com/jekyll/minima/master/_layouts/home.html
curl -O https://raw.githubusercontent.com/jekyll/minima/master/_layouts/default.html
curl -O https://raw.githubusercontent.com/jekyll/minima/master/_layouts/page.html
curl -O https://raw.githubusercontent.com/jekyll/minima/master/_layouts/post.html
```

Note: `page.html` is the most essential here

This takes effect:
```bash
      Regenerating: 1 file(s) changed at 2023-02-02 11:23:57
                    _layouts/home.html
                    
      Regenerating: 1 file(s) changed at 2023-02-02 11:23:57
                    _layouts/default.html
                    
      Regenerating: 1 file(s) changed at 2023-02-02 11:23:57
                    _layouts/page.html
                    
      Regenerating: 1 file(s) changed at 2023-02-02 11:23:57
                    _layouts/post.html
                    
      Regenerating: 1 file(s) changed at 2023-02-02 11:24:22
                    blog/worklogs/learn_jekyll_templating.md

```

Experiment: Change template layout, verify whether page is rendered differently

Observations:

* not posts; no `post-meata` class present
* in the header, upon closer inspection of rendered HTML and templates


Goal: get the header incldued in `_layouts/default.html`, see doc at <https://github.com/jekyll/minima#includes>

```bash
mkdir _includes && cd _includes
curl -O https://raw.githubusercontent.com/jekyll/minima/master/_includes/header.html
```

Split `_includes/header.html` into `_includes/header.html` with only the title and `_includes/site_pages.html` with the list of site pages.

Iterate on the html until formatting looks good.

Observation: Site pages now rendered, but on every page.

Conclusion: this works but needs modification to avoid rendering site pages on each page. To be fixed later.

Experiment: Simply change theme back to `slate` and see whether this persists

```bash
      Remote Theme: Using theme pages-themes/slate
  Liquid Exception: Could not locate the included file 'head.html' in any of ["/srv/jekyll/_includes", "/tmp/jekyll-remote-theme-20230202-1-sa3ud/_includes"]. Ensure it exists in one of those directories and is not a symlink as those are not allowed in safe mode. in /_layouts/default.html
```

update `_layouts/default.html`


Observation: Site pages rendered, but theme is off. 

Conclusion: This site pages strategy from minima will work for slate, but needs to be applied to the slate templates to work correctly.

Experiment: Apply site-pages templating to slate layout

Obtain slate layout, making sure to re-
```bash
mkdir -p _layouts && cd _layouts
curl -O https://raw.githubusercontent.com/pages-themes/slate/master/_layouts/default.html
```

Add:
```
{%- include site_pages.html -%}
```

Remove unrelated:
```bash
rm _includes/header.html
rm _layouts/home.html
rm_layouts/page.html
rm_layouts/post.html
```


Observation: Works, but site pages on every page.

Conclusion: Good progress, much more to learn about jekyll posts, pages, etc.


Experiment: use `index.md` as the "home" page, remove include from `default.html`

Observation: site pages no longer on every page. Need to iterate on formatting.

Experiment: remove `default.html`, rely on remote theme

Restart jekyll server to be sure

Observation: Works

Conclusion: Needed simply to have an `index.md` and add the `site pages` template to it.

Next steps: fix the formatting of the include
