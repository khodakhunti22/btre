from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    all_realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'mvp_realtor': mvp_realtor,
        'realtors': all_realtors
    }
    return render(request, 'pages/about.html', context)

