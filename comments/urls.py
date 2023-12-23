from django.urls import path
from . import views

urlpatterns = [
    # path("comments/<int:fk>/", views.comments_by_tip_id),
    path("all/", views.comments_list),
    path("<int:tip_id>/", views.comments_by_tip_id),
    path("newcomment/", views.post_comment),
    path('deletecomment/<int:pk>/', views.delete_comment)
]