
from django.urls import path

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<str:slug>/', ProductDetailSlugView.as_view()),
]