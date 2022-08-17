from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>', views.show_post_by_number),
    path('<str:blog>', views.show_my_posts),
    path('', views.index),
    path('test_1/', views.test_1),
    path('test_2/', views.get_guinness_world_records),
]
