# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.linear_model import LogisticRegression
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
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_predict = lr.predict(X_test)
lr_conf_matrix = confusion_matrix(y_test, lr_predict)
lr_acc_score = accuracy_score(y_test, lr_predict)

print("confussion matrix")
print(lr_conf_matrix)
print("\n")
print("Accuracy of Logistic Regression:",lr_acc_score*100,'\n')
print(classification_report(y_test,lr_predict))

# save the model to disk
pickle.dump(lr, open(conf['LR_MODEL'], 'wb'))

# Save the model stats
joblib.dump(lr_conf_matrix, conf["LR_CONF_MATRIX"])

# save the scaler to disk
joblib.dump(scaler, conf['LR_SCALER']) 