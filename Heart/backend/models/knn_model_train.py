# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.neighbors import KNeighborsClassifier
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
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
knn_predicted = knn.predict(X_test)
knn_conf_matrix = confusion_matrix(y_test, knn_predicted)
knn_acc_score = accuracy_score(y_test, knn_predicted)
print("confussion matrix")
print(knn_conf_matrix)
print("\n")
print("Accuracy of K-NeighborsClassifier:",knn_acc_score*100,'\n')
print(classification_report(y_test,knn_predicted))

# save the model to disk
pickle.dump(knn, open(conf['KNN_MODEL'], 'wb'))

# Save the model stats
joblib.dump(knn_conf_matrix, conf["KNN_CONF_MATRIX"])

# save the scaler to disk
joblib.dump(scaler, conf['KNN_SCALER']) 