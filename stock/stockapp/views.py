





from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,TemplateView,DeleteView,ListView
from .models import Stock
from .forms import AddstockForm,DateFilterForm

# Create your views here.

class StockHome(ListView):
    template_name = "home_stock.html"
    context_object_name = "stocks"
    model=Stock


class StockAddView(CreateView):
    template_name = "Add_stock.html"
    model=Stock
    success_url = reverse_lazy("stockhome")
    form_class = AddstockForm

class StockUEditView(UpdateView):
    model = Stock
    form_class = AddstockForm
    success_url = reverse_lazy("stockhome")
    pk_url_kwarg = "id"
    template_name = "update_stock.html"

class StockDeleteView(DeleteView):

        model = Stock
        template_name = "delete_stock.html"
        success_url = reverse_lazy("stockhome")
        pk_url_kwarg = "id"


