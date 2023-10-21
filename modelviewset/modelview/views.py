from . models import Student
from .serializer import Studenterializers
from rest_framework import viewsets

# Create your views here.

# =========================== ModelViewSet =================================


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studenterializers
    
    
    
# ========================  ReadOnlyModelViewSet ====================================    

# class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = Studenterializers