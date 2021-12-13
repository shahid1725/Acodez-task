
from django.urls import path
from .views import StockAddView,StockUEditView,StockHome,StockDeleteView



urlpatterns=[
    path("list",StockHome.as_view(),name="stockhome"),
    path("stock/add",StockAddView.as_view(),name="addstock"),
    path("stock/edit/<int:id>",StockUEditView.as_view(),name="editstock"),
    path("stock/delete/<int:id>",StockDeleteView.as_view(),name="deletestock")
]
