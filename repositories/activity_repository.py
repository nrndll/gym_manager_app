from db.run_sql import run_sql
from models.activity import Activity

def add(activity):
    sql = "INSERT INTO activities (description, capacity, premium) VALUES (%s, %s, %s) RETURNING id"
    values = [activity.description, activity.capacity, activity.premium]
    result = run_sql(sql, values)
    id = result[0]["id"]
    activity.id = id
    return activity

def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    for row in results:
        activity = Activity(row["description"], row["capacity"], row["premium"], row["id"])
        activities.append(activity)
    return activities

def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    activity = Activity(result["description"], result["capacity"], result["premium"], result["id"])
    return activity

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    value = [id]
    run_sql(sql, value)