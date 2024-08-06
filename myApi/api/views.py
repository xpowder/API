from django.shortcuts import get_object_or_404, render
from .models import Jop
from .serializers import JopSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

class JobView(APIView):  # Corrected the class name

    def get(self, request, *args, **kwargs):  # Corrected 'requset' to 'request'
        pk = kwargs.get('pk')
        queryset = Jop.objects.all()
        serializer = JopSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):  # Corrected 'requset' to 'request'
        serializer = JopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrected error handling
    
    def put(self, request, pk):  # Corrected 'requset' to 'request'
        job = get_object_or_404(Jop, pk=pk)  # Corrected model reference
        serializer = JopSerializer(job, data=request.data)  # Pass the instance to the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        job = get_object_or_404(Jop, pk=pk)  # Ensure the correct model is used
        job.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)
