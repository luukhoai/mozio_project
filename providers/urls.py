from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ProviderList.as_view()),
    path('<slug:slug>/', views.ProviderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
