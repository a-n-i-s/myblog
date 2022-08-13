from .models import Catagory
def catagories(request):
  return {'catagories':Catagory.objects.filter(parent=None)}