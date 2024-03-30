# Import Libraries
import numpy as np
from omegaconf import OmegaConf
import pickle
import joblib

# Load config file
# While running notebooks
#conf = OmegaConf.load("../../config.yaml")
# While running app
conf = OmegaConf.load("../config.yaml")

class ModelPrediction:
    def __init__(self) -> None:
        # Load scalers
        self.lr_scaler = joblib.load(conf['LR_SCALER'])
        self.rf_scaler = joblib.load(conf['RF_SCALER'])
        self.knn_scaler = joblib.load(conf['KNN_SCALER'])
        self.dt_scaler = joblib.load(conf['DT_SCALER'])
        self.svm_scaler = joblib.load(conf['SVM_SCALER'])

        # Load models
        self.lr_model = pickle.load(open(conf['LR_MODEL'], 'rb'))
        self.rf_model = pickle.load(open(conf['RF_MODEL'], 'rb'))
        self.knn_model = pickle.load(open(conf['KNN_MODEL'], 'rb'))
        self.dt_model = pickle.load(open(conf['DT_MODEL'],'rb'))
        self.svm_model = pickle.load(open(conf['SVM_MODEL'],'rb'))

    def predict_for_all_models(self, features):
        # Predict using LR
        lr_output_class, lr_output_prob = self.predict_using_lr(features)
        # Predict using RF
        rf_output_class, rf_output_prob = self.predict_using_rf(features)
        # Predict using KNN
        knn_output_class,knn_output_prob = self.predict_using_knn(features)
        # Predict using DT
        dt_output_class,dt_output_prob = self.predict_using_dt(features)
        # Predict using SVM
        svm_output_class,svm_output_prob = self.predict_using_svm(features)
        return [lr_output_prob, rf_output_prob, knn_output_prob,dt_output_prob,svm_output_prob]

    
    def predict_using_lr(self, features):
        # Transform to 2D array
        features_values = np.array(features).reshape(1, -1)
        # Scaling
        scaled_features_values = self.lr_scaler.transform(features_values)
        # Model output predict
        model_output = self.lr_model.predict(scaled_features_values)
        # Model predict probability for each class
        model_proba_output = self.lr_model.predict_proba(scaled_features_values)
        # Predict probability for class 1
        predict_probability = model_proba_output[:,1]
        return model_output[0], round(100 * predict_probability[0],2)
    
    def predict_using_rf(self, features):
        # Transform to 2D array
        features_values = np.array(features).reshape(1, -1)
        # Scaling
        scaled_features_values = self.rf_scaler.transform(features_values)
        # Model output predict
        model_output = self.rf_model.predict(scaled_features_values)
        # Model predict probability for each class
        model_proba_output = self.rf_model.predict_proba(scaled_features_values)
        # Predict probability for class 1
        predict_probability = model_proba_output[:,1]
        return model_output[0], round(100 * predict_probability[0],2)
    
    def predict_using_knn(self, features):
        # Transform to 2D array
        features_values = np.array(features).reshape(1, -1)
        # Scaling
        scaled_features_values = self.knn_scaler.transform(features_values)
        # Model output predict
        model_output = self.knn_model.predict(scaled_features_values)
        # Model predict probability for each class
        model_proba_output = self.knn_model.predict_proba(scaled_features_values)
        # Predict probability for class 1
        predict_probability = model_proba_output[:,1]
        return model_output[0], round(100 * predict_probability[0],2)
    
    def predict_using_dt(self,features):
        # Transform to 2D array
        features_values = np.array(features).reshape(1, -1)
        # Scaling
        scaled_features_values = self.dt_scaler.transform(features_values)
        # Model output predict
        model_output = self.dt_model.predict(scaled_features_values)
        # Model predict probability for each class
        model_proba_output = self.dt_model.predict_proba(scaled_features_values)
        # Predict probability for class 1
        predict_probability = model_proba_output[:,1]
        return model_output[0], round(100 * predict_probability[0],2)
    
    def predict_using_svm(self,features):
        # Transform to 2D array
        features_values = np.array(features).reshape(1, -1)
        # Scaling
        scaled_features_values = self.svm_scaler.transform(features_values)
        # Model output predict
        model_output = self.svm_model.predict(scaled_features_values)
        # Model predict probability for each class
        model_proba_output = self.svm_model.predict_proba(scaled_features_values)
        # Predict probability for class 1
        predict_probability = model_proba_output[:,1]
        return model_output[0], round(100 * predict_probability[0],2)
    



        