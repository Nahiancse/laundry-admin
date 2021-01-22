from django import forms
from .models import Item, SubItem


class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'


class SubItemForm(forms.ModelForm):
    class Meta:
        model=SubItem
        fields='__all__'