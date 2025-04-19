---
title: Explore Jekyll Tags and Categories
categories:
- hi
tags:
- bye
---
# {{ page.title }}

# Summary:

Probably only works for `_posts`, which is not used here.

https://jekyllrb.com/docs/posts/#tags-and-categories

# Experiments:
* Categories:
    * {{ site.categories }}
* Tags:
    * {{ site.tags }}

List them Out:
<pre>
{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
</pre>
/Done listing
