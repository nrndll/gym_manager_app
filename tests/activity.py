import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):
    def setUp(self):
        self.activity = Activity("Axe Throwing", 12, True)

    def test_activity_description(self):
        self.assertEqual("Axe Throwing", self.activity.description)

    def test_activity_capacity(self):
        self.assertEqual(12, self.activity.capacity)

    def test_activity_premium(self):
        self.assertEqual(True, self.activity.premium)

    def test__activity_id(self):
        self.assertEqual(None, self.activity.id)
