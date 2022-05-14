from django.urls import path
from .endpoint import views, auth_views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),

    path('', auth_views.google_login),
    path('google/', auth_views.google_auth),
    path('spotify-login/', auth_views.spotify_login),
    path('spotify-callback/', auth_views.spotify_auth),
]
