

from rest_framework.response import Response
from . models import Student
from .serializer import Studenterializers
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

# ===========================  Viewsets ================================================================
# =======================================================================================================

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = Studenterializers(stu , many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None,format=None):
            
            try:
                stu = Student.objects.get(id = pk)
                serializer = Studenterializers(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=404)
        
    def create(self,request,formate=None):
        serializer = Studenterializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'  }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk = id)
        serializer = Studenterializers(stu, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def partial_update(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk = id)
        serializer = Studenterializers(stu, request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk =id)
        stu.delete()
        return Response({'msg':'data Deleted'})
    
    
    
            
    
        
        
        
            