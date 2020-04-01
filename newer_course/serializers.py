from rest_framework import serializers

from newer_course.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Course
        fields = ['id', 'name', 'description', 'rating']
