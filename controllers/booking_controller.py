from flask import Flask, Blueprint, render_template, redirect, request
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def view_all():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/<id>")
def view(id):
    booking = booking_repository.select(id)
    return render_template("bookings/view.html", booking=booking)

@bookings_blueprint.route("/bookings/add")
def add():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("/bookings/add.html", members=members, activities=activities)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create():
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity)
    booking_repository.add(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete(id):
    booking_repository.delete(id)
    return redirect("/bookings")
