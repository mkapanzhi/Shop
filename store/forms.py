from django import forms

from .models import Store, ColorProduct, Product
from .validators import no_numbers_validator


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=1000, validators=[no_numbers_validator])
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    store = forms.ModelChoiceField(queryset=Store.objects.all())
    description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
    image = forms.ImageField(initial='/defpic.png')
    colors = forms.ModelMultipleChoiceField(queryset=ColorProduct.objects.all())



