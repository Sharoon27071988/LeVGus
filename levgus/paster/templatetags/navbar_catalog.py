from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag('paster/navbar_catalog.html', takes_context=True)
def navbar_catalog(context):
    context['categories'] = Category.objects.all()
    return context


@register.inclusion_tag('paster/paster_list.html')
def paster_list(paster, page_obj):
    return {'paster': paster, 'page_obj': page_obj}
