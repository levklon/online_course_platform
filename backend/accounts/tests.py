from django.test import TestCase
from .models import Course, Video

class CourseModelTest(TestCase):
    def setUp(self):
        Course.objects.create(title="Django Testing", description="Testing in Django")

    def test_course_title(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.title}'
        self.assertEqual(expected_object_name, 'Django Testing')

class VideoModelTest(TestCase):
    def setUp(self):
        course = Course.objects.create(title="Django Testing", description="Testing in Django")
        Video.objects.create(course=course, title="Test Video", url="http://example.com")

    def test_video_title(self):
        video = Video.objects.get(id=1)
        expected_object_name = f'{video.title}'
        self.assertEqual(expected_object_name, 'Test Video')
