from django.shortcuts import render, render,get_object_or_404, redirect
from django.utils import timezone
from .forms import DetailsForm
from .models import Details,Country, City
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def details_new(request):
    details = Details.objects.all()
    cities = City.objects.all()
    country = Country.objects.all()
    form = DetailsForm(request.POST, request.FILES)

    if request.method == "POST" and request.POST:
        details = Details.objects.get_or_create(name=request.POST.get('name'),
                                        email=request.POST.get('email'),
                                        address=request.POST.get('address'),
                                        country_id=request.POST.get('country'),
                                        city_id=request.POST.get('city'),
                                        zipcode=request.POST.get('zipcode'),
                                        phone_number=request.POST.get('phone_number'),
                                        image=request.FILES.get('image')
            )
    else:
        form = DetailsForm()
    return render(request, 'task/details_form.html',{'form':form,'cities':cities,'country':country} )
 
