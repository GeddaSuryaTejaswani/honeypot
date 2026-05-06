import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, IsolationForest

data = pd.read_csv("dataset/attack_logs.csv")

X = data[["command_length","failed_attempts","session_time"]]

y = data["label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train,y_train)

# Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,y_train)

# Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train,y_train)

# Isolation Forest
iso_model = IsolationForest()
iso_model.fit(X)

print("Logistic Regression Accuracy:",log_model.score(X_test,y_test))
print("Decision Tree Accuracy:",dt_model.score(X_test,y_test))
print("Random Forest Accuracy:",rf_model.score(X_test,y_test))

pickle.dump(log_model,open("ml_models/logistic_model.pkl","wb"))
pickle.dump(dt_model,open("ml_models/decision_tree.pkl","wb"))
pickle.dump(rf_model,open("ml_models/random_forest.pkl","wb"))
pickle.dump(iso_model,open("ml_models/isolation_forest.pkl","wb"))