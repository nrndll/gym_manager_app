import unittest
from models.booking import Booking
from models.activity import Activity
from models.member import Member


class TestBooking(unittest.TestCase):
    def setUp(self):
        member = Member("Nathan", "Rendall", True, 1)
        activity = Activity("Axe Throwing", 12, True, 2)
        self.booking = Booking(member, activity)

    def test__booking_user(self):
        self.assertEqual(1, self.booking.member.id)

    def test_booking_lesson(self):
        self.assertEqual(2, self.booking.activity.id)

    def test__booking_id(self):
        self.assertEqual(None, self.booking.id)