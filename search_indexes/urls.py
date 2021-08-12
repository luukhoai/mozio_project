from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PolygonDocumentView

router = DefaultRouter()
books = router.register('polygon',
                        PolygonDocumentView,
                        basename='polygondocument')

urlpatterns = [
    path('', include(router.urls)),
]
