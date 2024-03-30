#Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.tree import DecisionTreeClassifier
import pickle
import joblib
from omegaconf import OmegaConf 

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

#Train Model
dt = DecisionTreeClassifier(criterion = 'entropy',random_state=0,max_depth = 6)
dt.fit(X_train, y_train)
dt_predicted = dt.predict(X_test)
dt_conf_matrix = confusion_matrix(y_test, dt_predicted)
dt_acc_score = accuracy_score(y_test, dt_predicted)

print("confussion matrix")
print(dt_conf_matrix)
print("\n")
print("Accuracy of DecisionTreeClassifier:",dt_acc_score*100,'\n')
print(classification_report(y_test,dt_predicted))

# save the model to disk
pickle.dump(dt, open(conf['DT_MODEL'], 'wb'))

# Save the model stats
joblib.dump(dt_conf_matrix, conf["DT_CONF_MATRIX"])

# save the scaler to disk
joblib.dump(scaler, conf['DT_SCALER']) 

