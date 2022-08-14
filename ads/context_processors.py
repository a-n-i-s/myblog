from .models import Ad
def ads(request):
  return {'ads':Ad.objects.all()}
