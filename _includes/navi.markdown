<nav>
{% for entry in site.data.navi %}
<!-- {{ entry.url }} == {{ fullurl }}-->
{% if entry.url == page.url %}
  <a href="{{ entry.url }}" class="btn active">{{ entry.title }}</a>
{% else %}
  <a href="{{ entry.url }}" class="btn">{{ entry.title }}</a>
{% endif %}
{% endfor %}
</nav>