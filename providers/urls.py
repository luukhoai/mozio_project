from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProviderList.as_view()),
    path('<slug:slug>/', views.ProviderDetail.as_view()),
]
