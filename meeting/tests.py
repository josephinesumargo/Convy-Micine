from django.test import TestCase
from django.contrib.auth.models import User
from group.models import Group
from .models import Meeting

# Create your tests here.
class Test_Create_Meeting(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        testuser1.save()

        test_group = Group.objects.create(
            category='PERS', title='Trial Test'
        )
        test_group.save()

        test_meeting = Meeting.objects.create(
            user_id=1, 
            group_id=1, 
            agenda='Trial', 
            meeting_date='2022-07-25 02:00:00+00:00',
            location='Zoom',
            meeting_link='https://zoomlink.com'
        )

    def test_meeting(self):
        meeting = Meeting.objects.get(id=1)
        user = f'{meeting.user}'
        group = f'{meeting.group}'
        agenda = f'{meeting.agenda}'
        meeting_date = f'{meeting.meeting_date}'
        location = f'{meeting.location}'
        meeting_link = f'{meeting.meeting_link}'
        self.assertEqual(user, 'test_user1')
        self.assertEqual(group, 'Trial Test - PERS')
        self.assertEqual(agenda, 'Trial')
        self.assertEqual(meeting_date, '2022-07-25 02:00:00+00:00')
        self.assertEqual(location, 'Zoom')
        self.assertEqual(meeting_link, 'https://zoomlink.com')
        self.assertEqual(str(meeting), "Trial")