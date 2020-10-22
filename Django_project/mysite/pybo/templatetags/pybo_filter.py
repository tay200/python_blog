# ---------------------------------------- [edit] ---------------------------------------- #
from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg
    #-기존 값 - 입력받은 값-#
# ---------------------------------------------------------------------------------------- #