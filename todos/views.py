from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo


class TodoListViews(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class  TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    template_name = 'todos/todo_confirm_delete.html'


class TodoCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.mark_has_complete()
        return redirect("todo_list")

