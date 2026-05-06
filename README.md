 🛡️ Honeypot ML Project – Attack Detection System

 📌 Overview

This project implements a **Low-Interaction Honeypot System integrated with Machine Learning** to detect and analyze cyber-attacks. It simulates a **fake Windows environment** to attract attackers, logs their activities, and classifies them as **normal or malicious** using ML algorithms.



 🚀 Features

* 🖥 Fake Windows command-line environment
* 🛡 Low-interaction honeypot (safe simulation)
* 🤖 Machine Learning-based attack detection
* 🔍 Hybrid detection (ML + rule-based)
* 📊 Dashboard for attack visualization
* 📝 Logging of attacker commands and IPs



🧠 Algorithms Used

* Low-Interaction Emulation Algorithm
* Random Forest
* Decision Tree
* Logistic Regression
* Isolation Forest
* Rule-Based Keyword Detection



 📁 Project Structure


honeypot_ml_project/
│
├── app.py
├── train_model.py
├── analyze_attacks.py
├── low_interaction.py
├── dataset/
├── ml_models/
├── logs/
├── templates/
├── static/
└── README.md




 ⚙️ Installation

 1. Clone Repository

bash
git clone https://github.com/GeddaSuryaTejaswani/honeypot.git
cd honeypot_ml_project


 2. Install Dependencies

bash
pip install -r requirements.txt



 ▶️ How to Run

Step 1: Train Model

bash
python train_model.py


Step 2: Run Application

bash
python app.py


Step 3: Open in Browser

http://127.0.0.1:5000


Dashboard

http://127.0.0.1:5000/dashboard



🧪 Example Commands

 Normal

dir
whoami
cd Documents
type notes.txt

 Attack Simulation

powershell exploit
nmap scan
hydra attack
net user admin /add
sql injection



 📊 Output

* Displays command output in fake terminal
* Detects attack or normal activity
* Logs data in CSV and log files
* Visualizes results in dashboard



 🎯 Objectives

* Simulate attacker interaction safely
* Detect cyber-attacks using ML
* Analyze attack patterns
* Provide visualization dashboard


 ⚠️ Limitations

* Low-interaction honeypot (limited realism)
* Small dataset affects ML accuracy
* Not suitable for production security systems


🚀 Future Enhancements

* Real-time dashboard updates
* Attack severity levels
* Geolocation tracking of attackers
* Full GUI-based fake Windows system



👩‍💻 Author

Mini Project – Cybersecurity & Machine Learning


📜 License

This project is for educational purposes only.

