from django.urls import path, include
from .views import HomePageView, SignUpView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView, BulletinView 


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("bulletin/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("bulletin/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("bulletin/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("bulletin/new/", PostCreateView.as_view(), name="post_new"),
    path("bulletin/", BulletinView.as_view(), name="bulletin"),
]