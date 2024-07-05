from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        Course.objects.create(title="Django Testing", description="Testing in Django")

    def test_course_title(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.title}'
        self.assertEqual(expected_object_name, 'Django Testing')
