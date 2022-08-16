from multiprocessing.dummy import current_process
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
    title = models.CharField(max_length=32, default="title")
    picture = models.CharField(max_length=128, default="picture")
    description = models.CharField(max_length=256, default="No description")
    bid = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner", default=1)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default="Home")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return f"{self.title} that's listed for {self.bid} by {self.owner}"

class Auction(models.Model):
    active = models.BooleanField(default=True)
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator", default=1)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", default=1)

    def __str__(self):
        return f"{self.winner} is currently winning {self.listing}"

class Comments(models.Model):
    message = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
        
    def __str__(self):
        return f"{self.user}: {self.message}"
