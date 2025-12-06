from django.urls import path
from . import views

app_name = 'videos'   # <-- app_name should be defined before urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name='upload'),
]