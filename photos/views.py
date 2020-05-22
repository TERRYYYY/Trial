from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Location,Category,Image
import datetime as dt

# Create your views here.
def index(request):
    date = dt.date.today()
    images = Image.get_images()
    location = Location.get_location()
    locations = Location.get_location()

    return render(request, 'index.html', {"date": date, "images": images, "location": location, "locations": locations})


def image(request):
    return render(request,'all-photos/gallery.html')

def get_image(request, id):
  locations = Location.get_location()
  try:
    image = Image.objects.get(pk=id)
    print(image)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request, "all-photos/gallery.html", {"image": image, "locations": locations})


