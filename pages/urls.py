from django.urls import path
from .views import homePageView

#url patterns here



urlpatterns = [
    path('', homePageView, name='home'),
]