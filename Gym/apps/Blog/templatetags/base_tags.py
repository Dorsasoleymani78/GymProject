from unicodedata import category
from django import template
from ..models import settings,Category
 
register=template.Library()

@register.simple_tag
def title( ):
   tag= [ tag.title for tag in settings.objects.all()]
   return "".join(tag)

@register.inclusion_tag("Blog/partials/navbar.html")
def  category_navbar():
    return{
        "category":Category.objects.filter(status=True)
    }