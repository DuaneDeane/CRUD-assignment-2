#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """

from flask import g
import sqlite3

DATABASE = "user_db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["name"] = result[1]
        res_dict["hobby"] = result[2]
        res_dict["sex"] = result[3]
        out["body"].append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(users_id):
    query = """
        SELECT *
        FROM user
        WHERE id = ?
        """

    cursor = get_db().execute(query, (users_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(users_id, fields: dict):
    field_string = ", ".join(
        "%s=\"%s\"" % (key, val)
        for key, val
        in fields.items())
    query = """
            UPDATE user
            SET %s
            WHERE id = ?
            """ % field_string
    cursor = get_db()
    cursor.execute(query, (users_id,))
    cursor.commit()
    return True


def create(name, hobby, sex):
    value_tuple = (name, hobby, sex)
    query = """
                INSERT INTO user (
                        name,
                        hobby,
                        sex)
                VALUES (?, ?, ?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id


def delete(users_id):
    query = "DELETE FROM user WHERE id=%s" % users_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True

