from django import template
from etude.models import Contact, StaticData

register = template.Library()


@register.inclusion_tag('etude/main_contact.html')
def show_main_contact():
    main_contact = Contact.objects.get(main_contact=True)
    return {'main_contact': main_contact}


@register.simple_tag()
def get_main_contact():
    return Contact.objects.get(main_contact=True)


@register.simple_tag()
def get_static_data():
    return StaticData.objects.get(main=True)
