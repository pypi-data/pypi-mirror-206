from datetime import datetime
from typing import List

import hao
from hao.pg import PG

from .domains import Permission

LOGGER = hao.logs.get_logger(__name__)


def get_permissions(username: str):
    with PG() as db:
        sql = 'select permissions from t_user_permissions where username = %s '
        values = (username, )
        db.cursor.execute(sql, values)
        items = db.cursor.fetchone()
        return items[0] if items else []


def add_permissions(username: str, permissions: List[Permission]):
    sql_select = 'select permissions from t_user_permissions where username = %s '
    sql_update = 'update t_user_permissions set permissions = %s, updated_at = %s where username = %s returning username'
    sql_insert = 'insert into t_user_permissions (username, permissions, updated_at) values (%s, %s, %s)'
    now = datetime.now()
    with PG() as db:
        values_select = (username, )
        db.cursor.execute(sql_select, values_select)
        items = db.cursor.fetchone()
        perms = items[0] if items else []

        perms_to_add = [p.value for p in permissions]
        perms = hao.jsons.dumps(hao.lists.uniquify(perms + perms_to_add))

        values_update = (perms, now, username)
        db.cursor.execute(sql_update, values_update)
        db.conn.commit()
        items = db.cursor.fetchall()
        if items:
            return perms

        values_insert = (username, perms, now)
        db.cursor.execute(sql_insert, values_insert)
        db.conn.commit()
        return perms


def remove_permissions(username: str, permissions: List[Permission]):
    sql_select = 'select permissions from t_user_permissions where username = %s '
    sql_update = 'update t_user_permissions set permissions = %s, updated_at = %s where username = %s returning username'
    now = datetime.now()
    with PG() as db:
        values_select = (username, )
        db.cursor.execute(sql_select, values_select)
        items = db.cursor.fetchone()
        if not items:
            return []
        perms, = items

        perms_to_remove = [p.value for p in permissions]
        perms = hao.jsons.dumps([p for p in perms if p not in perms_to_remove])

        values_update = (perms, now, username)
        db.cursor.execute(sql_update, values_update)
        db.conn.commit()
        return perms
