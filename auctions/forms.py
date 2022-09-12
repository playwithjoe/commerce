from sre_parse import CATEGORIES
from django import forms
from django.forms import HiddenInput, ModelForm
from .models import Listing, User

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'winner': forms.HiddenInput(),
            'watchlist': forms.HiddenInput(),
            "active": forms.HiddenInput(),
            "picture": forms.TextInput(attrs={"placeholder": "Copy link to picture of listing eg. (https://www.website.com/my_picture.jpeggit"})
        }
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
        
