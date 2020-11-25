#!/user/bin/env python3
# -*- coding: utf8 -*-
""" HTTP route definitions """

from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/user")
def get_all_user():
    out = scan()
    out["ok"] = True
    out["message"] = "Success"
    return out


@app.route("/user/<pid>")
def get_one_user(pid):
    out = read(int(pid))
    out["ok"] = True
    out["message"] = "Success"
    return out


@app.route("/user", methods=["POST"])
def create_user():
    product_data = request.json
    new_id = create(
        product_data.get("name"),
        product_data.get("hobby"),
        product_data.get("sex")
    )

    return {"ok": True, "message": "Success", "new_id": new_id}


@app.route("/user/<pid>", methods=["PUT"])
def update_user(pid):
    product_data = request.json
    out = update(int(pid), product_data)
    return {"ok": out, "message": "Updated"}
