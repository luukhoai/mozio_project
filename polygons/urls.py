from django.urls import path
from . import views

urlpatterns = [
    path('', views.PolygonList.as_view()),
    path('<slug:slug>/', views.PolygonDetail.as_view()),
]
