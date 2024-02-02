from django.urls import path
from .views import *

urlpatterns = [
    path('stock_index',StockAPI.as_view()),
]
