from app import app, db
from flask import jsonify
from app.rdb.models import User


@app.route("/users/<union_id>")
def get_union_users(union_id: str):
    users = db.session.query(User)
    return jsonify([user.first_name for user in users])
