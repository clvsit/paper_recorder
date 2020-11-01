from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('view', views.view, name="view"),
    path('label/get', views.get_label),
    path('label/add', views.add_label),
    path('label/add', views.delete_label),
    path('label/add', views.modify_label),
]
