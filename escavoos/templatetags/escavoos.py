from django.template import Library
from django.contrib.admin.templatetags.admin_list import result_list


register = Library()


@register.inclusion_tag("admin/escavoos/change_list_results.html")
def voos_list(cl):
    context = result_list(cl)
    context['results'] = zip(cl.result_list, context['results'])
    return context

