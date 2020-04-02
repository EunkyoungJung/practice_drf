from rest_framework import viewsets

from newest_course.models      import Course
from newest_course.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


