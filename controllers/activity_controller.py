from flask import Flask, Blueprint, render_template, redirect, request
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def view_all():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)


@activities_blueprint.route("/activities/<id>")
def view(id):
    activity = activity_repository.select(id)
    members = activity_repository.members(activity)
    return render_template("activities/view.html", activity=activity, members=members)


@activities_blueprint.route("/activities/add")
def add():
    return render_template("/activities/add.html")


@activities_blueprint.route("/activities", methods=["POST"])
def create():
    description = request.form["description"]
    capacity = request.form["capacity"]
    premium = request.form["premium"]
    activity = Activity(description, capacity, premium)
    activity_repository.add(activity)
    return redirect("/activities")


@activities_blueprint.route("/activities/<id>/edit")
def edit(id):
    activity = activity_repository.select(id)
    return render_template("/activities/edit.html", activity=activity)


@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update(id):
    description = request.form["description"]
    capacity = request.form["capacity"]
    premium = request.form["premium"]
    activity = Activity(description, capacity, premium, id)
    activity_repository.edit(activity)
    return redirect("/activities")


@activities_blueprint.route("/activities/<id>/delete", methods=["POST"])
def delete(id):
    activity_repository.delete(id)
    return redirect("/activities")
