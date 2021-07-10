from db.run_sql import run_sql
from models.booking import Booking


def add(booking):
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id]
    result = run_sql(sql, values)
    id = result[0]["id"]
    booking.id = id
    return booking


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        booking = Booking(row["member_id"], row["activity_id"], row["id"])
        bookings.append(booking)
    return bookings


def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    booking = Booking(result["member_id"], result["activity_id"], result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    value = [id]
    run_sql(sql, value)
