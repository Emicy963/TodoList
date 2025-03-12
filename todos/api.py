from django.http import Http404
from .models import Todo
from .serializers import TodoSerializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView

class TodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    lookup_field = 'pk'

class TodoCompleteAPI(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        todo = self.get_object(pk)
        todo.mark_has_complete()
        serializer = TodoSerializers(todo)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
