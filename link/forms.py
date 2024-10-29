from django import forms
from .models import links_model
#list we need to pass to our temlate
#1 qurey set
#number of item we need to track 
# number of items are discounted
#from to save the objects and if we have error we need to dispaly

class link_forms(forms.ModelForm):
    class Meta:
        model = links_model  # Use 'model' instead of 'models'
        fields = ['url',]  # Ensure this field exists in your model
