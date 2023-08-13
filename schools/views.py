from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from . import models


def index(request):
    close= models.course.objects.all()
    slid= models.slider.objects.all()
    testmo = models.testmonial.objects.all()

    # pagination 
    # pagination
    pagination = Paginator(close, 4)
    page_number = request.GET.get('page')
    page_list= pagination.get_page(page_number) 


    context= {
        'close':close,
        'paginator': page_list,
        'slid': slid,
        'testmo': testmo
        
    }
    return render(request, 'school/index.html', context)