from django import template
from django.template.defaultfilters import urlencode

from ..models import Blog, Categories
register = template.Library()


@register.simple_tag
def blog_post():
    return Blog.objects.all().order_by('-id')[:3]


@register.simple_tag
def blog_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)