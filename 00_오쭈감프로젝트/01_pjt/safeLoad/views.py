from django.shortcuts import render
from .models import CCTV, Streetlamp

# Create your views here.
def index(request):
    cctv = CCTV.objects.all()
    strlmp = Streetlamp.objects.all()
    context = {
        'cctv' : cctv,
        'strlmp' : strlmp,
    }
    return render(request, 'safeLoad/index.html', context)