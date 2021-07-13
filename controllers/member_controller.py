from flask import Flask, Blueprint, render_template, redirect, request
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def view_all():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def view(id):
    member = member_repository.select(id)
    activities = member_repository.activities(member)
    return render_template("members/view.html", member=member, activities=activities)

@members_blueprint.route("/members/add")
def add():
    return render_template("/members/add.html")

@members_blueprint.route("/members", methods=["POST"])
def create():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    member = Member(first_name, last_name, premium)
    if member_repository.add(member) != None:
        return redirect("/members")
    else:
        return render_template("/members/error.html")

@members_blueprint.route("/members/<id>/edit")
def edit(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    member = Member(first_name, last_name, premium, id)
    member_repository.edit(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete(id):
    member_repository.delete(id)
    return redirect("/members")