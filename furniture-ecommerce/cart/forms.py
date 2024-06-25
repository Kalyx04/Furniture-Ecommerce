from django import forms

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)  # Add city field
    zipcode = forms.CharField(max_length=10)  # Add zip code field
    state = forms.CharField(max_length=50)  # Add state field
    phone_number = forms.CharField(max_length=20)