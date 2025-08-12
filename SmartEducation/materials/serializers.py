from rest_framework import serializers
from .models import Lesson, Course

# Сериализатор для модели Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'