#Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.svm import SVC
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
svc =  SVC(kernel='rbf', C=2)
svc = SVC(probability = True)
svc.fit(X_train, y_train)
svc_predicted = svc.predict(X_test)
svc_conf_matrix = confusion_matrix(y_test, svc_predicted)
svc_acc_score = accuracy_score(y_test, svc_predicted)
print("confussion matrix")
print(svc_conf_matrix)
print("\n")
print("Accuracy of Support Vector Classifier:",svc_acc_score*100,'\n')
print(classification_report(y_test,svc_predicted))

# save the model to disk
pickle.dump(svc, open(conf['SVM_MODEL'], 'wb'))

# Save the model stats
joblib.dump(svc_conf_matrix, conf["SVM_CONF_MATRIX"])

# save the scaler to disk
joblib.dump(scaler, conf['SVM_SCALER']) 