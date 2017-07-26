import sqlite3

def create_vote(conn, zid, candidage, ranking):
    with conn:
        conn.execute("REPLACE INTO votes (zid, candidate, ranking) VALUES (?, ?, ?)", (zid, candidate, ranking))

def vote(conn, zid, votes):
    for ranking, candidate in votes.items():
        create_vote(conn, zid, ranking, candidatg)

'''
def update(conn, zid, candidate, ranking):
    with conn:
        conn.execute("UPDATE votes SET ranking = ? WHERE (zid = ? AND candidate = ?)", (ranking, zid, candidate))

def exists_ranking(conn, zid, ranking):
    return conn.execute("SELECT EXISTS (SELECT * FROM votes WHERE (zid = ? AND ranking = ?) LIMIT 1 )", (zid, ranking))

def delete_candidate(conn, zid, candidate):
    with conn:
        conn.execute("DELETE FROM votes WHERE (zid = ? AND candidate = ?)", (zid, candidate))

def delete_ranking(conn, zid, ranking):
    with conn:
        conn.execute("DELETE FROM votes WHERE (zid = ? AND ranking = ?)", (zid, ranking))

def update_vote(conn, zid, candidate, ranking):
    with conn:
        if exists_ranking(conn, zid, ranking):
            delete_rankning(conn, zid, ranking)

        else:
            conn.execute("""UPDATE votes SET ranking = ? WHERE (zid = ? AND candidate = ?)""", (ranking, zid, candidate))

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def build_clause(i):
    return list(map(
        lambda s: s[0] + " {} ?".format(s[1]) if isinstance(s, tuple) else s + " = ?", i))

def fetchall(conn, table, where = {}, orderby = {}, limit = 0):
    conn.row_factory = dict_factory #sqlite3.Row
    query = "SELECT * FROM {}".format(table)
    if where:
        query += " WHERE {}".format(" AND ".join(build_clause(where.keys())))
    if orderby:
        query += " ORDER BY " + ", ".join(
                ["{} {}".format(key, value) for key, value in orderby.items()])
    if limit:
        query += " LIMIT {}".format(limit)
    return conn.execute(query, (*where.values(),)).fetchall()

def fetchone(conn, table, where = {}):
    conn.row_factory = dict_factory #sqlite3.Row
    query = "SELECT * FROM {}".format(table)
    if where:
        query += " WHERE {}".format(" AND ".join(build_clause(where.keys())))
    return conn.execute(query, (*where.values(),)).fetchone()

def exists(conn, table, where):
    return conn.execute(
        "SELECT EXISTS (SELECT * FROM {} WHERE ({}) LIMIT 1)".format(
            table,
            " AND ".join(build_clause(where.keys()))),
        (*where.values(),)).fetchone()[0]

def create(conn, table, values):
    with conn:
        conn.execute(
            "INSERT INTO {} ({}) VALUES ({})".format(
                table,
                ", ".join(values.keys()),
                ", ".join(["?"] * len(values))),
            (*values.values(),))

def update(conn, table, values, where = {}):
    with conn:
        query = "UPDATE {} SET {}".format(
                table,
                ", ".join(build_clause(values.keys())))
        if where:
            query += " WHERE {}".format(" AND ".join(build_clause(where.keys())))
            conn.execute(query, (*values.values(), *where.values(),))
        else:
            conn.execute(query, (*values.values(),))

def delete(conn, table, where):
    with conn:
        conn.execute(
            "DELETE FROM {} WHERE ({})".format(
                table,
                " AND ".join(build_clause(where.keys()))),
            (*where.values(),))
'''
