import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from backend.models.model_predict import ModelPrediction

model_pred_obj = ModelPrediction()


ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")

appWidth,appHeight = 1440,900

self = ctk.CTk()
self.title("Result")
self.geometry(f"{appWidth}x{appHeight}")

self.wm_state('zoomed')

def final():
    age = float(self.ageEntry.get())
    gender = int(self.genderVar.get())
    chestpain = int(self.chestpainEntry.get())
    rbp = float(self.rbpEntry.get())
    chol = float(self.cholEntry.get())
    fasting = int(self.fastingEntry.get())
    ecg = int(self.ecgEntry.get())
    thalach = float(self.thalachEntry.get())
    angina = int(self.anginaVar.get())
    oldpeak = float(self.oldpeakEntry.get())
    slope = int(self.slopeEntry.get())
    ca = int(self.caEntry.get())

    sequence_of_features = [
        "age", "gender", "chestpain", "restingBP", "serumcholestrol", 
        "fastingbloodsugar", "restingrelectro", "maxheartrate", 
        "exerciseangia", "oldpeak", "slope", "noofmajorvessels"
    ]

    values = {
        'age': age,
        'gender': gender,
        'chestpain': chestpain,
        'restingBP': rbp,
        'serumcholestrol': chol,
        'fastingbloodsugar': fasting,
        'restingrelectro': ecg,
        'maxheartrate': thalach,
        'exerciseangia': angina,
        'oldpeak': oldpeak,
        'slope': slope,
        'noofmajorvessels': ca,
    }

    model_input = [values[i] for i in sequence_of_features]

    model_output_class, _ = model_pred_obj.predict_using_lr(model_input)
        
    if model_output_class == 1:
        messagebox.showinfo("Prediction", "High risk")
        

    else:
        messagebox.showinfo("Prediction", "Low Risk")
 

if __name__ == "__main__":
    app = final()

    app.mainloop()



