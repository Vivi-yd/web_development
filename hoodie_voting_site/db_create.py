from db import db

with db:
    db.execute("""CREATE TABLE votes (
        zid,
        candidate,
        ranking INTEGER,
        CONSTRAINT unique_rank UNIQUE (zid, rank),
        CONSTRAINT unique_candidate UNIQUE (zid, candidate)
    )""")

