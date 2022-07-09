from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.forms import ListingForm
from .models import CATEGORY_CHOICES, User, Listing, Auction


@login_required
def new(request):

    # When you submit a new listing via POST
    if request.method == "POST":
        
        # Form data collected
        new_form = ListingForm(request.POST)

        # Check if form is valid
        if new_form.is_valid():

            # Save new listing
            listing = new_form.save()

            Auction.objects.create(listing=listing, bid=listing.bid)

        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "auctions/new.html", {
            "form": ListingForm()
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
def categories(request, CATEGORY_CHOICES):
    
    

    return render(request, "auctions/categories.html", {
        "category": CATEGORY_CHOICES,

    })

@login_required
def index(request):

    # Find all Listings filtered by the owner 
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

def bid(request, listing):
    pass

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
