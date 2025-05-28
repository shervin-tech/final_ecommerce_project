from django import forms
from users.models import Address

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 1})
    )

class CheckoutForm(forms.Form):
    shipping_address = forms.ModelChoiceField(
        queryset=None,
        empty_label="Select a shipping address",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipping_address'].queryset = Address.objects.filter(user=user) 