from django.urls import path, re_path

from .views import (IndexAPIView)

urlpatterns = [
    path("", IndexAPIView.as_view(), name="index_page")
]
