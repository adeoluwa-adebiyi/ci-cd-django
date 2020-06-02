from django.urls import path

from .views import MultiplyView

urlpatterns = [
    path("multiply", MultiplyView().as_view(), name="multiply-view"),
]