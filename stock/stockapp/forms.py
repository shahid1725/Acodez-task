from django import forms
from django.forms import ModelForm
from .models import Stock


class AddstockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ["productid", "productname", "quantity", "status"]

        widgets = {
            "productid": forms.TextInput(attrs={"class": "form-control"}),
            "productname": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

        labels = {
            'productid': 'Product ID',
            'productname': 'Product Name',
            "quantity": "Quantity",
            "stock_date": "Stock Date",
            "status":"Status"

        }

class DateFilterForm(forms.Form):
    from_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    to_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

