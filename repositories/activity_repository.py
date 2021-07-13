from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def add(activity):
    sql = "INSERT INTO activities (description, capacity, premium, date, time) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [activity.description, activity.capacity, activity.premium, activity.date, activity.time]
    result = run_sql(sql, values)
    id = result[0]["id"]
    activity.id = id
    return activity

def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    for row in results:
        activity = Activity(row["description"], row["capacity"], row["premium"], row["date"], row["time"], row["id"])
        activities.append(activity)
    return activities

def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    activity = Activity(result["description"], result["capacity"], result["premium"], result["date"], result["time"], result["id"])
    return activity

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def edit(activity):
    sql = "UPDATE activities SET (description, capacity, premium, date, time) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [activity.description, activity.capacity, activity.premium, activity.date, activity.time, activity.id]
    run_sql(sql, values)

def members(activity):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
    value = [activity.id]
    results = run_sql(sql, value)
    for row in results:
        member = Member(row["first_name"], row["last_name"], row["premium"], row["id"])
        members.append(member)
    return members

# def total_bookings(activity):
#     sql = "SELECT COUNT(*) FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
#     value = [activity.id]
#     result = run_sql(sql, value)
#     return result[0][0]

def places_available(activity):
    sql = "SELECT COUNT(*) FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
    value = [activity.id]
    result = run_sql(sql, value)
    return activity.capacity - result[0][0]

def space_for_booking(activity):
    if places_available(activity) > 0:
        return True
    else:
        return False

# def non_premium_activities():
#     activities = []
#     sql = "SELECT * FROM activities WHERE premium = %s"
#     value = [False]
#     results = run_sql(sql, value)
#     for row in results:
#         activity = Activity(row["description"], row["capacity"], row["premium"], row["date"], row["time"], row["id"])
#         activities.append(activity)
#     return activities
