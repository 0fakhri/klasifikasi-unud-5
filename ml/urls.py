from django.urls import path
from ml import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predictnab',views.predictnab,name="predictnab"),
]
