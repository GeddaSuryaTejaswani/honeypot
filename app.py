from flask import Flask, render_template, request
import pandas as pd
import pickle
import random
import datetime
import csv

from low_interaction import emulate_windows_command

app = Flask(__name__)

# Load ML model
rf_model = pickle.load(open("ml_models/random_forest.pkl", "rb"))

# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# COMMAND HANDLER
# -------------------------------
@app.route("/command", methods=["POST"])
def command():

    cmd = request.form["command"]
    ip = request.remote_addr

    cmd_len = len(cmd)
    failed = random.randint(0, 5)
    session = random.randint(1, 40)
    timestamp = datetime.datetime.now()

    # -------------------------------
    # HYBRID DETECTION
    # -------------------------------
    attack_keywords = [
        "powershell", "net user", "sql",
        "nmap", "hydra", "john",
        "exploit", "hack", "attack"
    ]

    if any(word in cmd.lower() for word in attack_keywords):
        label = 1
    else:
        prediction = rf_model.predict([[cmd_len, failed, session]])
        label = prediction[0]

    # -------------------------------
    # FAKE SYSTEM RESPONSE
    # -------------------------------
    output = emulate_windows_command(cmd)

    # -------------------------------
    # SAFE CSV STORAGE (FIXED)
    # -------------------------------
    with open("dataset/attack_logs.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        writer.writerow([
            ip,
            cmd,
            cmd_len,
            failed,
            session,
            timestamp,
            label
        ])

    # -------------------------------
    # LOG FILE
    # -------------------------------
    with open("logs/honeypot_logs.txt", "a") as f:
        f.write(f"{timestamp} | {ip} | {cmd} | Label: {label}\n")

    # -------------------------------
    # RESULT MESSAGE
    # -------------------------------
    if label == 1:
        result = "⚠ Possible Attack Detected"
    else:
        result = "Normal Activity"

    return render_template(
        "index.html",
        command=cmd,
        output=output,
        prediction=result
    )


# -------------------------------
# DASHBOARD (FIXED)
# -------------------------------
@app.route("/dashboard")
def dashboard():

    data = pd.read_csv("dataset/attack_logs.csv", on_bad_lines='skip')

    total = len(data)

    attacks = len(data[data["label"] == 1])

    normal = len(data[data["label"] == 0])

    commands = data["command"].value_counts().head(5)

    ips = data["ip"].value_counts().head(5)

    return render_template(
        "dashboard.html",
        total=total,
        attacks=attacks,
        normal=normal,
        commands=commands,
        ips=ips
    )


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)