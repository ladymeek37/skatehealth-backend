from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.tips_list),
    path("", views.user_tip),
    path("<int:pk>/", views.tip_detail),
    path("favorite/<int:pk>/", views.add_to_fav_count),
    path("by_category", views.tips_by_category),
    path("by_id/<int:tip_id>/", views.get_tip_by_id),
]