from flask import Flask, Blueprint, render_template, redirect, request
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def actvities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)
