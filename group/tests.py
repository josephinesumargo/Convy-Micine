from django.test import TestCase
from django.contrib.auth.models import User
from .models import Group, Announcement

# Create your tests here.
class Test_Create_Group(TestCase):

    @classmethod
    def setUpTestData(cls):
        def members(self):
            group = Group.objects.create(category='PERS', title='Trial Test')
            member1 = User.objects.create_user(username='test_user1', password='123456789')
            member2 = User.objects.create_user(username='test_user2', password='123456789')
            group.members.set([member1.pk, member2.pk])
            self.assertEqual(group.members.count(), 2)
            category = f'{group.category}'
            title = f'{group.title}'
            self.assertEqual(category, 'PERS')
            self.assertEqual(title, 'Trial Test')
            self.assertEqual(str(group), "Trial Test - PERS")

class Test_Create_Announcement(TestCase):

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

        test_announcement = Announcement.objects.create(
            user_id=1, 
            group_id=1, 
            title='Trial', 
            body='This is a trial',
            published='2022-07-24 02:00:00+00:00',
        )

    def test_announcement(self):
        announcement = Announcement.objects.get(id=1)
        user = f'{announcement.user}'
        group = f'{announcement.group}'
        title = f'{announcement.title}'
        body = f'{announcement.body}'
        published = f'{announcement.published}'
        self.assertEqual(user, 'test_user1')
        self.assertEqual(group, 'Trial Test - PERS')
        self.assertEqual(title, 'Trial')
        self.assertEqual(body, 'This is a trial')
        self.assertEqual(published, '2022-07-24 02:00:00+00:00')
        self.assertEqual(str(announcement), "Trial")

