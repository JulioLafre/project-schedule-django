from django.shortcuts import render
from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect


def create(request):
    context = {

    }

    
    return render(
        request,
        'contact/create.html',
        context 
    )