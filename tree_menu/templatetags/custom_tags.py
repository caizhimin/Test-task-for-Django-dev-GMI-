# coding: utf8
from __future__ import unicode_literals
from django import template
from django.utils.safestring import mark_safe
__author__ = 'cai'

register = template.Library()


def custom_menu(value):

    def _helper(list_, tabs=1):
        indent = u'\t' * tabs
        output = []
        list_length = len(list_)
        i = 0
        while i < list_length:
            title = list_[i]
            sublist = ''
            sublist_item = None
            if isinstance(title, (list, tuple)):
                sublist_item = title
                title = ''
            elif i < list_length - 1:
                next_item = list_[i+1]
                if next_item and isinstance(next_item, (list, tuple)):
                    # The next item is a sub-list.
                    sublist_item = next_item
                    # We've processed the next item now too.
                    i += 1
            if sublist_item:
                sublist = _helper(sublist_item, tabs+1)
                sublist = '\n%s<ul>\n<a href="">%s</a>\n%s</ul>\n%s' % (indent, sublist,
                                                         indent, indent)
            output.append('%s<li><a href="%s">%s%s</a></li>' % (indent, title, title, sublist))
            i += 1
        return '\n'.join(output)
    return mark_safe(_helper(value))


register.filter('custom_menu', custom_menu)




