# Worklog - 2023-02-03: Jekyll+Liquid: Categorize Pages by Directory

# Goal: Automatically group pages by directory

In [Learn Jekyll Templating](/learn_jekyll_templating.md), the basic site pages template provided by minima was hacked into the slate theme in order to list all markdown pages within the site.

The result is a simple list of all markdown pages.

However, the pages were originally created within parent directories in order to group them.

Timebox an investigation into whether these parent directories can be used as a category.


## Result

This was possible, and the results can be seen in the `_includes/site_pages.html` of the GH Pages repo.

The include itself serves as good-enough documentation of this experiment, but does not capture the resources used during the learning process.

**time** ~1h for experiment, ~15min for writeup

## Resources

* comments: <https://stackoverflow.com/questions/27007323/how-do-you-comment-out-in-liquid>
* valid URL chars: <https://stackoverflow.com/questions/1547899/which-characters-make-a-url-invalid?noredirect=1&lq=1>
  * note: this may have to be revisited
* advanced arrays
  * <https://stackoverflow.com/questions/27198467/parse-a-string-into-tokens-in-shopify-liquid>
  * <https://kermode.co/2014/advanced-arrays-in-shopify-s-liquid/>
  * liquid templating: <https://shopify.github.io/liquid/>
    * capture: <https://shopify.github.io/liquid/tags/variable/#capture>
      * for string concatenation
    * split: <https://shopify.github.io/liquid/filters/split/>
      * for creating arrays (from said concatenated strings)
    * concat: <https://shopify.github.io/liquid/filters/concat/>
      * for array concatenation
    * uniq: <https://shopify.github.io/liquid/filters/downcase/>
      * for removing duplicates from concatenated array
* understanding site.pages
  * pages: <https://jekyllrb.com/docs/pages/>
  * jekyll variables: <https://jekyllrb.com/docs/variables/>
  * data types: <https://stackoverflow.com/a/58919169>
    * possibly outdated; `site.pages` includes markdown files which have no frontmatter
