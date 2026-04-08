from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def w209():
    file = "about9.jpg"
    return render_template("w209.html", file=file)

@app.route("/api")
def api():
    return jsonify({"X": 2})

@app.route("/players/count")
def players_count():
    db_path = "players_20.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
        LIMIT 1
    """)
    row = cur.fetchone()
    if row is None:
        con.close()
        return jsonify({"count": 0})

    table = row[0]
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur.fetchone()[0]

    con.close()
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run()
