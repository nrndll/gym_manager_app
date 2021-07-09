import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Nathan", "Rendall", True)

    def test_member_first_name(self):
        self.assertEqual("Nathan", self.member.first_name)

    def test_member_last_name(self):
        self.assertEqual("Rendall", self.member.last_name)

    def test_member_premium(self):
        self.assertEqual(True, self.member.premium)

    def test__member_id(self):
        self.assertEqual(None, self.member.id)
