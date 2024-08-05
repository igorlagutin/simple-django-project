from django.urls import path

from api.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view()),
]