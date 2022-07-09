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
            'watchlist': forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
