from django.urls import path

from . import views

from .models import CATEGORY_CHOICES

urlpatterns = [
    path("", views.index, name="index"),
    path("listings/<int:listing_id>", views.listings, name="listings"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watchlist", views.add_watchlist, {"listing_id": "listing_id"}, name="add_watchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("bid", views.bid, name="bid"),
    path("close", views.close, name="close"),
    path("comment", views.add_comment, name="comment"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new")  
] 
