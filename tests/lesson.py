import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):
    def setUp(self):
        self.lesson = Lesson("Axe Throwing", 12, True)

    def test_lesson_description(self):
        self.assertEqual("Axe Throwing", self.lesson.description)

    def test_lesson_capacity(self):
        self.assertEqual(12, self.lesson.capacity)

    def test_lesson_premium(self):
        self.assertEqual(True, self.lesson.premium)

    def test__lesson_id(self):
        self.assertEqual(None, self.lesson.id)
