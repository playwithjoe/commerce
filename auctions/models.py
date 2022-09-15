from multiprocessing.dummy import current_process
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORY_CHOICES = [
        ("CLOTHING", "Clothing & Apparel"),
        ("ELECTRONICS", "Electronics"),
        ("HOME", "Home & Garden"),
        ("TOYS", "Toys")
    ]

class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    title = models.CharField(max_length=32)
    picture = models.CharField(max_length=128)
    description = models.CharField(max_length=256, default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner", default=1)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", default=1)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default="Home")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} that's listed for {self.price} by {self.owner}"

class Bid(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids", default="0")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bid} made by {self.bidder} on {self.auction.title}"

class Comments(models.Model):
    message = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, null=True, on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented: {self.message}"
