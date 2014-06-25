from django import template
import markdown

register = template.Library()

@register.filter(is_safe=True)
def md(value):
	return markdown.markdown(value)