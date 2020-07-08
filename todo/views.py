from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404

#from todo.models import ToDoElements
from todo.serializers import ToDoSerializer
from todo.models import ToDoElements

class ToDoView(APIView):
    def get(self,request):
        todos = ToDoElements.objects.all()
        #return Response(todos)
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def put(self,request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ToDoDetailView(APIView):
    def get(self,request, pk):
        todo = get_object_or_404(ToDoElements, pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def delete(self,request, pk):
        todo = get_object_or_404(ToDoElements, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)