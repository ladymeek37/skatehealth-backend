from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_favorited_tips),
    path("addfavorite/",views.add_to_favorites)
]
