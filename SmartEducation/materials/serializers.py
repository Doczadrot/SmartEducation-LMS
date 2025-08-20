from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import SerializerMetaclass

from .models import Lesson, Course
from users.models import Pays


# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)#поле со списком урока
    count_lesson = SerializerMethodField() # добавляем поле количество уроков

    def get_count_lesson(self, instance): #описываем как будет работать count_lesson
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'count_lesson')


class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'