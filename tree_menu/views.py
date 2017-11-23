from django.shortcuts import render_to_response
from django.http import Http404
from models import Menu

# Create your views here.


def display(menus):
    """
    :param menus:
    :return:
    [u'Asia', [u'China', [u'Shanghai']], u'South America', [u'Chile', u'USA', [u'New York']], u'North America']
    """
    display_list = []
    for menu in menus:
        display_list.append(menu.title)
        children = menu.children.all()
        if len(children) > 0:
            display_list.append(display(children.all()))
    return display_list


def index(request):
    menus = Menu.objects.filter(parent=None)
    return render_to_response('index.html', {'menus': display(menus)})


def allow_menu(request, menu):
    if Menu.objects.filter(title=menu):
        menus = Menu.objects.filter(parent=None)
        return render_to_response('index.html', {'menus': display(menus)})
    else:
        raise Http404