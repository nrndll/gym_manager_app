from flask import Flask, Blueprint, render_template, redirect, request
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)
