from typing import List
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from . models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)   
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page) 

    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listings = Listing.objects.all().filter(is_published=True)
    listing = get_object_or_404(listings, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    # Keywords
    queryset = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(destription__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)
    
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)
    
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

