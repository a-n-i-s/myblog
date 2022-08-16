from atexit import register
from django import template
register=template.Library()
@register.filter()
def star(id,user):
  if user.favourites.posts.filter(id=id).exists():
    return '⭐'
  return '✰'
