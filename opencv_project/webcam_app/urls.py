from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home" ),
    path('hand_tracking_camera/', views.hand_tracking_camera, name='hand_tracking_camera'),

]