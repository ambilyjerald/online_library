import django_filters
from django.forms import forms
from django_filters import FilterSet, CharFilter

from myapp.models import Add_Book


class book_filter_form(FilterSet):
    brand=CharFilter(lookup_expr='icontains',widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'search by category'}))
    # seller_name= CharFilter(field_name='seller__name',lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'search by seller name'}))

    class Meta:
        model = Add_Book
        fields = ['brand',]
