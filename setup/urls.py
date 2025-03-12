from django.contrib import admin
from django.urls import path, include
from todos.views import TodoListViews, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView
from todos.api import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoListViews.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    # API urls
    path('api', include(router.urls)),
]
