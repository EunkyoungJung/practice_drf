#from django.http import Http404

#from rest_framework          import status
from rest_framework.response import Response
#from rest_framework.views    import APIView
from rest_framework         import generics, mixins

from newer_course.models      import Course
from newer_course.serializers import CourseSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
