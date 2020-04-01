#from django.http import Http404

#from rest_framework          import status
from rest_framework.response import Response
#from rest_framework.views    import APIView
from rest_framework         import generics, mixins

from new_course.models      import Course
from new_course.serializers import CourseSerializer

class CourseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
        print(queryset)

    def post(self, request):
        return self.create(request)

class CourseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


