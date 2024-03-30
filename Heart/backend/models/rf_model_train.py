# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib
from omegaconf import OmegaConf 

# Load config file
conf = OmegaConf.load("../../config.yaml")

# Load dataset
data = pd.read_csv(conf["DATASET"])

# Select dataset
y = data["target"]
X = data.drop(columns=['patientid','target'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
rf = RandomForestClassifier(n_estimators=20, random_state=12,max_depth=5)
rf.fit(X_train,y_train)
rf_predicted = rf.predict(X_test)
rf_conf_matrix = confusion_matrix(y_test, rf_predicted)
rf_acc_score = accuracy_score(y_test, rf_predicted)
print("confussion matrix")
print(rf_conf_matrix)
print("\n")
print("Accuracy of Random Forest:",rf_acc_score*100,'\n')
print(classification_report(y_test,rf_predicted))

# save the model to disk
pickle.dump(rf, open(conf['RF_MODEL'], 'wb'))

# Save the model stats
joblib.dump(rf_conf_matrix, conf["RF_CONF_MATRIX"])

# save the scaler to disk
joblib.dump(scaler, conf['RF_SCALER']) 