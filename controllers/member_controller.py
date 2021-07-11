from flask import Flask, Blueprint, render_template, redirect, request
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def member(id):
    member = member_repository.select(id)
    return render_template("members/view.html", member=member)

@members_blueprint.route("/members/add")
def add_member():
    return render_template("/members/add.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    member = Member(first_name, last_name, premium)
    member_repository.add(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    member = Member(first_name, last_name, premium, id)
    member_repository.edit(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")