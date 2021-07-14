from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity

def add(member):
    capitalise_names(member)
    if already_member(member) == False:
        sql = "INSERT INTO members (first_name, last_name, premium) VALUES (%s, %s, %s) RETURNING id"
        values = [member.first_name, member.last_name, member.premium]
        result = run_sql(sql, values)
        id = result[0]["id"]
        member.id = id
        return member
    else:
        return None

def select_all():
    members=[]
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["first_name"], row["last_name"], row["premium"], row["id"])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["premium"], result["id"])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def edit(member):
    sql = "UPDATE members SET (first_name, last_name, premium) = (%s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.premium, member.id]
    run_sql(sql, values)

def activities(member):
    activities = []
    sql = "SELECT activities.* FROM activities INNER JOIN bookings ON bookings.activity_id = activities.id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        activity = Activity(row["description"], row["capacity"], row["premium"], row["date"], row["time"], row["id"])
        activities.append(activity)
    return activities

# def already_member(member):
#     results = select_all()
#     is_member = False
#     for result in results:
#         if result.first_name == member.first_name and result.last_name == member.last_name:
#             is_member = True
#     return is_member

def already_member(member):
    sql = "SELECT COUNT(*) FROM members WHERE (first_name, last_name) = (%s, %s)"
    values = [member.first_name, member.last_name]
    result = run_sql(sql, values)
    if result[0][0] > 0:
        return True
    else:
        return False

def capitalise_names(member):
    member.first_name = member.first_name.capitalize()
    member.last_name = member.last_name.capitalize()