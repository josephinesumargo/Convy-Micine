from django.test import TestCase
from django.contrib.auth.models import User
from convy_calendar.models import Event

# Create your tests here.
class Event_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        testuser1.save()

        test_event = Event.objects.create(
            user_id=1, title='DIY', description='This is a DIY', start_time='2022-07-25 03:58:00+00:00', end_time='2022-07-25 04:58:00+00:00'
        )
        test_event.save()

    def test_event(self):
        event = Event.objects.get(id=1)
        user = f'{event.user}'
        title = f'{event.title}'
        description = f'{event.description}'
        start_time = f'{event.start_time}'
        end_time = f'{event.end_time}'
        self.assertEqual(user, 'test_user1')
        self.assertEqual(title, 'DIY')
        self.assertEqual(description, 'This is a DIY')
        self.assertEqual(start_time, '2022-07-25 03:58:00+00:00')
        self.assertEqual(end_time, '2022-07-25 04:58:00+00:00')
        self.assertEqual(str(event), "DIY")