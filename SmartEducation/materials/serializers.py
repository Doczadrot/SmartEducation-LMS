from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import SerializerMetaclass

from .models import Lesson, Course

# Сериализатор для модели Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):

    count_lesson = SerializerMethodField() # добавляем поле количество уроков

    def get_count_lesson(self, instance): #описываем как будет работать count_lesson
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'

# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'