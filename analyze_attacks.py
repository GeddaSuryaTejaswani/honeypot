import pandas as pd

data = pd.read_csv("dataset/attack_logs.csv")

print("\nTotal Interactions:",len(data))

print("\nAttack vs Normal:")
print(data["label"].value_counts())

print("\nTop Commands:")
print(data["command"].value_counts().head())

print("\nTop Attacker IPs:")
print(data["ip"].value_counts().head())