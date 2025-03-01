from django import template
from django.shortcuts import render, redirect
from clientapp.models import Case

register = template.Library()

@register.inclusion_tag('clientapp/sidebar.html', takes_context=True)
def case_list_view(context):
    request = context['request']
    client_session = request.session.get("client_session", {})
    client_name = client_session.get("client_id") 
    c = Case.objects.filter(client=client_name)
    return {"cases": c}
