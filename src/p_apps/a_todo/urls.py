from django.urls import include, path
from rest_framework import routers

from p_apps.a_todo import views

router = routers.DefaultRouter()
router.register(r'list-todos', views.ToDoViewSets, basename="todos")


urlpatterns = [
    path('', include(router.urls)),
]