import unittest
from models.booking import Booking
from models.lesson import Lesson
from models.member import Member


class TestBooking(unittest.TestCase):
    def setUp(self):
        member = Member("Nathan", "Rendall", True, 1)
        lesson = Lesson("Axe Throwing", 12, True, 2)
        self.booking = Booking(member, lesson)

    def test__booking_user(self):
        self.assertEqual(1, self.booking.member.id)

    def test_booking_lesson(self):
        self.assertEqual(2, self.booking.lesson.id)

    def test__booking_id(self):
        self.assertEqual(None, self.booking.id)