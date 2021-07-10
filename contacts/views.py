from django.shortcuts import render, redirect
from .models import Contacts
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)
        contact.save()

        # Send Mail
        print('Email : ', realtor_email)
        send_mail(
            subject='Property listing inquiry',
            message='There has been an inquiry for ' + listing + '. Sign into the admin panel for more',
            from_email='khutik6@gmail.com',
            recipient_list=[realtor_email, 'khoda.khunti22@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Query submitted successfuly, Realtor will get in touch with you')
        return redirect('/listings/' + listing_id)

        
