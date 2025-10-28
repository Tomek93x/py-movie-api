<<<<<<< HEAD
from django.urls import path
from .views import (
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
>>>>>>> 2b6308f2207193ba4916bdfbe9ecf71a54d126ed
]
