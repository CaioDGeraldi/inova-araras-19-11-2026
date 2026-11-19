import segno
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def qr(context, path):
    url = context["request"].build_absolute_uri(path)
    return mark_safe(segno.make(url).svg_inline(scale=5, border=2))
