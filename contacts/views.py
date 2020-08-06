from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from contacts.models import Contact
from listings.models import Listing
from django.core.mail import send_mail


def makeContact(request):
    if request.method == "POST":
        listing = Listing.objects.get(pk=request.POST['listing_id'])
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            user = request.user
            hasContacted = Contact.objects.all().filter(listing_id=listing.id, listing__contact__user_id=user.id)
            if hasContacted:
                messages.error(request, "you have already make an inqueri for this listing")
                return redirect('/listings/' + str(listing.id))

        else:
            user = None

        contact = Contact(listing=listing, name=name, email=email, phone=phone, message=message, user=user)
        contact.save()
        # send_mail
        send_mail(
            'property listing inquery',
            'there has been an inquery for' + str(listing) + ". Sign in to admin panel for more info",
            'karimzadarsalan@gmail.com',
            [listing.realtor.email, "arsalankarimzadeh1@gmail.com","rsharifnasab@gmail.com"],
            fail_silently=False
        )

        messages.success(request, "Your request has been submitted a realtor will call you soon")

        return redirect('/listings/' + str(listing.id))
    pass
