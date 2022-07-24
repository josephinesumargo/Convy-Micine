from django.test import TestCase
from django.contrib.auth.models import User
from group.models import Group
from .models import TaskGroup, Task

# Create your tests here.
class Test_Create_TaskGroup(TestCase):

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

        test_taskgroup = TaskGroup.objects.create(
            user_id=1, 
            group_id=1, 
            title='Trial', 
            deadline='2022-07-25 02:00:00+00:00',
        )
        test_taskgroup.save()

    def test_taskgroup(self):
        taskgroup = TaskGroup.objects.get(id=1)
        user = f'{taskgroup.user}'
        group = f'{taskgroup.group}'
        title = f'{taskgroup.title}'
        deadline = f'{taskgroup.deadline}'
        self.assertEqual(user, 'test_user1')
        self.assertEqual(group, 'Trial Test - PERS')
        self.assertEqual(title, 'Trial')
        self.assertEqual(deadline, '2022-07-25 02:00:00+00:00')
        self.assertEqual(str(taskgroup), "Trial")

class Test_Create_Task(TestCase):

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

        test_taskgroup = TaskGroup.objects.create(
            user_id=1, 
            group_id=1, 
            title='Trial', 
            deadline='2022-07-25 02:00:00+00:00',
        )
        test_taskgroup.save()

        test_task = Task.objects.create(
            user_id=1, 
            taskgroup_id=1, 
            title='Trial', 
            complete='False',
        )
        test_task.save()

    def test_taskgroup(self):
        task = Task.objects.get(id=1)
        user = f'{task.user}'
        taskgroup = f'{task.taskgroup}'
        title = f'{task.title}'
        complete = f'{task.complete}'
        self.assertEqual(user, 'test_user1')
        self.assertEqual(taskgroup, 'Trial')
        self.assertEqual(title, 'Trial')
        self.assertEqual(complete, 'False')
        self.assertEqual(str(task), "Trial")