from django.contrib import admin
from django.urls import path
from todos.views import TodoListViews, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView
from todos.api import TodoView, TodoDetailView, TodoCompleteAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoListViews.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    # API urls
    path('api/todos/', TodoView.as_view()),
    path('api/todos/<int:pk>', TodoDetailView.as_view()),
    path('api/todos/complete/<int:pk>', TodoCompleteAPI.as_view()),
]
