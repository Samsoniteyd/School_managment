from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from . import models


def index(request):
    close= models.course.objects.all()

    # pagination 
    # pagination
    pagination = Paginator(close, 2)
    page_number = request.GET.get('page')
    page_list= pagination.get_page(page_number) 


    context= {
        'close':close,
        'paginator': page_list
        
    }
    return render(request, 'school/index.html', context)