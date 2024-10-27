from django import forms
from .models import links_model
class link_forms(forms.ModelForm):
     class Meta:
        models=links_model,
        fields=('url')