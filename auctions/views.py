from email import message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from auctions.forms import ListingForm
from .models import *


@login_required
def new(request):

    # When you submit a new listing via POST
    if request.method == "POST":
        
        # Form data collected
        new = ListingForm(request.POST)

        # Check if form is valid
        if new.is_valid():   
            
            # Save new Listing with inputted form data
            new.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "auctions/new.html", {
            "form": ListingForm(initial={'owner': request.user})
        })


@login_required
def listings(request, listing_id):

    listing = Listing.objects.get(id=listing_id)
    user = request.user

    return render(request, "auctions/listings.html", {
        "listing": listing,
        "user": user,
            })

@login_required
def categories(request):

    # Takes the CATEGORY_CHOICES from the Model to display for user to choose which categories to look at
    return render(request, "auctions/categories.html", {
        "categories": CATEGORY_CHOICES
    })

@login_required
def category(request, category):

    # Finds all listings that match the category chosen from categories.html
    cat_listings = Listing.objects.all().filter(category=category)

    return render(request, "auctions/category.html", {
        "cat_listings": cat_listings
    })

@login_required
def index(request):

    listings = Listing.objects.all()

    return render(request, "auctions/index.html", {
        "listings": listings
    })

@login_required
def watchlist(request):

    # Watchlist of all items for user
    watchlist = Listing.objects.all().filter(watchlist=request.user)

    return render (request, "auctions/watchlist.html", {
        "watchlist": watchlist
    })

def add_watchlist(request, listing_id):

    if request.method == "POST":
        
        # Looks up title of Listing
        listing_id = int(request.POST["listing_id"])
        listing = Listing.objects.get(id=listing_id)

        # if already on watchlist will remove else add to watchlist
        if request.user in listing.watchlist.all():
            listing.watchlist.remove(request.user)
        else:
            listing.watchlist.add(request.user)
            listing.save()

        return HttpResponseRedirect(reverse('watchlist'))

@login_required
def bid(request):
    
    if request.method == "POST":

        # Get listing_id and the bid from user
        listing_id = request.POST["listing_id"]
        bid = float(request.POST["bid"])

        # Look up listing from listing_id
        listing = Listing.objects.get(id=listing_id)

        # Make sure bid is valid
        if bid <= listing.price:
            return render(request, "auctions/listings.html", {
                "listing": listing,
                "bid": bid,
                "message": "Invalid bid, must be larger than current price"                
            })
        else:
            new_bid = Bid(bid=bid, auction=listing, bidder=request.user)
            new_bid.save()

            listing.price = bid
            listing.winner = request.user
            listing.save()

        
        return HttpResponseRedirect(reverse('index'))

@login_required
def close(request):

    if request.method == "POST":

        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)

        if listing.owner == request.user:
            listing.active = False
            listing.save()

        return HttpResponseRedirect(reverse('index'))
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
