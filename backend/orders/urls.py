from django.urls import path

from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path("", OrderListCreateView.as_view(), name="order_list_create"),
    path("<int:pk>/", OrderRetrieveUpdateDestroyView.as_view(), name="order_detail"),
]
