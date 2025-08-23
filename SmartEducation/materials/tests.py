from http.client import responses

from django.contrib.auth.models import Group
from django.http import response
from rest_framework.test import APITestCase
from users.models import Users
from materials.models import Course, Lesson, Subscription


class LessonTests(APITestCase):
    def setUp(self):
        """
        Подготовка данных для тестов уроков.
        Создаем пользователя, модератора, курс, урок и данные для создания урока.
        """
        self.user = Users.objects.create(
            username="testuser",
            email="testuser@example.com",
            is_active=True
        )
        self.moderator = Users.objects.create(
            username="moderator",
            email="moderator@example.com",
            is_staff=True,
            is_active=True
        )

        self.course = Course.objects.create(
            title="Тестовый курс",
            author=self.user
        )

        self.lesson = Lesson.objects.create(
            title="Тестовый урок",
            course=self.course,
            author=self.user
        )

        self.lesson_data = {
            "title": "Новый урок",
            "description": "Описание нового урока",
            "course": self.course.pk,
            "link_video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
        self.not_owner = Users.objects.create(username="not_owner",
            email="testuser@example.com",
            is_active=True
        )
        moderator_group, created = Group.objects.get_or_create(name='Модератор')
        self.moderator.groups.add(moderator_group)

    def test_moderator_not_create_lesson(self):
        """Проверка на то, что модератор не может создавать уроки."""
        self.client.force_authenticate(user=self.moderator)
        response = self.client.post('/lessons/', self.lesson_data, format='json')
        self.assertEqual(response.status_code, 403)

    def test_moderator_not_delete_lessons(self):
        """Проверка на то, что модератор не может удалять уроки."""
        self.client.force_authenticate(user=self.moderator)
        response = self.client.delete(f'/lessons/{self.lesson.pk}/')
        self.assertEqual(response.status_code, 403)

    def test_create_lesson(self):
        """Проверка обычный пользователь может создать урок."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/lessons/', self.lesson_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_list_lessons(self):
        """Проверка пользователь может просмотреть список уроков."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, 200)

    def test_update_lessons(self):
        """Проверка владелец урока может его обновить."""
        self.client.force_authenticate(user=self.user)
        update_data = {'title': 'Обновленный урок'}
        response = self.client.patch(f'/lessons/{self.lesson.pk}/', update_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_lesson_not_owner(self):
        """Проверка модератор не может удалить урок"""
        self.client.force_authenticate(user=self.moderator)
        response = self.client.delete(f'/lessons/{self.lesson.pk}/')
        self.assertEqual(response.status_code, 403)

    def test_update_lesson_by_moderator(self):
        """Проверка на то что модератор может обновить чужой урок."""
        self.client.force_authenticate(user=self.moderator)
        update_data = {'title': 'Обновленный урок модератором'}
        response = self.client.patch(f'/lessons/{self.lesson.pk}/', update_data, format='json')
        self.assertEqual(response.status_code, 200)


class SubScriptionTest(APITestCase):
    def setUp(self):
        """
        Создаем данные для теста
        """
        self.user = Users.objects.create(
            username="testuser",
            email="testuser@example.com",
            is_active=True
        )
        self.course = Course.objects.create(
            title="Тестовый курс",
            author=self.user
        )
        self.subscription_data = {'course_id': self.course.pk}

    def test_create_subscription(self):
        """Проверка возможности полписки"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/subscription/', self.subscription_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete_subscription(self):
        """Проверка отписки"""
        Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/subscription/', self.subscription_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())