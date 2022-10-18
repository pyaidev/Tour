from django.template import Library
from apps.services.models import Services
from django.utils.http import urlencode

register = Library()


@register.simple_tag
def post_services():
    return Services.objects.all()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

