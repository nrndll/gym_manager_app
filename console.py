from models.member import Member
from models.activity import Activity
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

# member_repository.delete_all()
# member_repository.delete(1)

# activity_repository.delete_all()
# activity_repository.delete(1)

# booking_repository.delete_all()
# booking_repository.delete(1)

member_1 = Member("Nathan", "Rendall", True)
member_repository.add(member_1)
member_2 = Member("Dean", "Robertson", True)
member_repository.add(member_2)
member_3 = Member("Arnold", "Schwarzenegger", True)
member_repository.add(member_3)
member_4 = Member("Stephen", "Seagal", False)
member_repository.add(member_4)
member_5 = Member("Carl", "Weathers", False)
member_repository.add(member_5)

# print(member_repository.select_all())
# print(member_repository.select(1))

activity_1 = Activity("Axe Throwing", 12, True, "2021-07-31", "13:00")
activity_repository.add(activity_1)
activity_2 = Activity("Powerlifting", 10, False, "2021/07/21", "21:00")
activity_repository.add(activity_2)
activity_3 = Activity("Deadlifts", 4, True, "2021/08/01", "16:00")
activity_repository.add(activity_3)
activity_4 = Activity("Strength", 8, False, "2021/07/21", "09:00")
activity_repository.add(activity_4)

# print(activity_repository.select_all())
# print(activity_repository.select(1))

booking_1 = Booking(member_1, activity_3)
booking_repository.add(booking_1)
booking_2 = Booking(member_2, activity_3)
booking_repository.add(booking_2)
booking_3 = Booking(member_4, activity_3)
booking_repository.add(booking_3)
booking_4 = Booking(member_2, activity_4)
booking_repository.add(booking_4)

print(activity_repository.capacity(activity_3))
activity_repository.space_for_booking(activity_3)

