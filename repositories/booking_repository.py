from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def add(booking):
    if booking.member.premium:
        if activity_repository.space_for_booking(booking.activity):
            sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
            values = [booking.member.id, booking.activity.id]
            result = run_sql(sql, values)
            id = result[0]["id"]
            booking.id = id
            return booking
        else:
            return None
    elif booking.member.premium == False and booking.activity.premium == True:
            return None
    elif booking.member.premium == False and booking.activity.premium == False:
        if activity_repository.space_for_booking(booking.activity):
            sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
            values = [booking.member.id, booking.activity.id]
            result = run_sql(sql, values)
            id = result[0]["id"]
            booking.id = id
            return booking
        else:
            return None
    else:
        return None

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row["member_id"])
        activity = activity_repository.select(row["activity_id"])
        booking = Booking(member, activity, row["id"])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    member = member_repository.select(result["member_id"])
    activity = activity_repository.select(result["activity_id"])
    booking = Booking(member, activity, result["id"])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    value = [id]
    run_sql(sql, value)
