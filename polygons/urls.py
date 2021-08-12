from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.PolygonList.as_view()),
    path('<slug:slug>/', views.PolygonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
