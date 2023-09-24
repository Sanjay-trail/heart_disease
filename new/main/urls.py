from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path('explore/', views.explore, name='explore'),
    path('', views.homepage, name="homepage"),
    path('', views.prediction, name='prediction'),

]