from django import forms

from store.models import Store


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=1000)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    store = forms.ModelChoiceField(queryset=Store.objects.all())