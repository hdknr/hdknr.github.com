{% for date in dates %}
- [{{ date|date }}]({{date}}.md){% endfor %}