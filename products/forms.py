from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    url = forms.CharField(
        widget= forms.TextInput(
            attrs={
            'placeholder': 'enter url ',
            'class': 'w-full p-2 border border-gray-300 rounded-lg'
            # 'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;'
            }
            )
    ),
    name = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
            'placeholder': 'enter name ',
            'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;'
            }
            )),
    old_price = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
            'placeholder': 'enter price ',
            'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;'
            }
            )
    )
    class Meta: 
        model = Product
        fields = ['url','name','old_price']