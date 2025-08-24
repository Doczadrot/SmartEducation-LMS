from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import SerializerMetaclass

from .models import Lesson, Course, Subscription
from users.models import Pays

from .validators import LinkValidator


# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):

    link_video = serializers.URLField(validators=[LinkValidator(field='link_video')], required=False)

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)#поле со списком урока
    count_lesson = SerializerMethodField() # добавляем поле количество уроков
    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, instance):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, course=instance).exists()


    def get_count_lesson(self, instance): #описываем как будет работать count_lesson
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'count_lesson', 'is_subscribed')


class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'