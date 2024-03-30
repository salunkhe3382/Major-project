import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
from io import BytesIO
#from result import final
from functools import partial
from backend.models.model_predict import ModelPrediction
from functools import partial
#from med import medicine

model_pred_obj = ModelPrediction()

ctk.set_appearance_mode("white")

ctk.set_default_color_theme("blue")

appWidth,appHeight = 1440,900

self = ctk.CTk()

class MainApp(ctk.CTk):

    #photos_refs= []
    def __init__(self):
        super().__init__()

        self.open_App()

    def open_App(self):
        
        self.title("Heart Disease Prediction Model")
        self.geometry(f"{appWidth}x{appHeight}")

        self.wm_state('zoomed')

        """image_path = os.path.join(os.path.dirname(__file__),'Images/doctor.jpg')
        image = ctk.CTkImage(light_image=Image.open(image_path),size=(1600, 1200))
        image_label = ctk.CTkLabel(self,image=image,text='')
        image_label.place(x = 10,y = 20)"""

        
        heading_label=ctk.CTkLabel(self,text="HEART DISEASE DETECTION MODEL",font=('Arial',38,'bold'))
        heading_label.grid(row=0,column=4,columnspan=4,pady=20,sticky="ew")

        
        #Name
        self.nameLabel = ctk.CTkLabel(self,text="Name")
        self.nameLabel.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

        self.nameEntry = ctk.CTkEntry(self,placeholder_text="Enter Name")
        self.nameEntry.grid(row=1,column=1,columnspan=5,padx=20,pady=20,sticky="ew")
       
        #Age 
        self.ageLabel = ctk.CTkLabel(self,text="Age")
        self.ageLabel.grid(row=2,column=0,padx=20,pady=20,sticky="ew")

        self.ageEntry = ctk.CTkEntry(self,placeholder_text="Enter Age")
        self.ageEntry.grid(row=2,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Gender

        self.genderLabel = ctk.CTkLabel(self,text="Sex")
        self.genderLabel.grid(row=3,column=0,padx=20,pady=20,sticky="ew")
        
        #Gender radio buttons
        self.genderVar = tk.StringVar(value="Choose Gender")

        self.maleRadioButton = ctk.CTkRadioButton(self,text="Male",variable=self.genderVar)
        self.maleRadioButton.grid(row=3,column=1,padx=20,pady=20,sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self,text="Female",variable=self.genderVar)
        self.femaleRadioButton.grid(row=3,column=2,padx=20,pady=20,sticky="ew")

        #Chest Pain
        self.chestpainLabel = ctk.CTkLabel(self,text="Chest Pain(0 - 4)")
        self.chestpainLabel.grid(row=4,column=0,padx=20,pady=20,sticky="ew")

        self.chestpainEntry = ctk.CTkEntry(self,placeholder_text="Enter the value of chest pain range")
        self.chestpainEntry.grid(row=4,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Resting Blood Pressure
        self.rbpLabel = ctk.CTkLabel(self,text="Resting Blood Pressure(94 - 200)")
        self.rbpLabel.grid(row=5,column=0,padx=20,pady=20,sticky="ew")

        self.rbpEntry = ctk.CTkEntry(self,placeholder_text="Enter the value of Resting Blood Pressure")
        self.rbpEntry.grid(row=5,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Cholestrol
        self.cholLabel = ctk.CTkLabel(self,text="Cholestrol")
        self.cholLabel.grid(row=6,column=0,padx=20,pady=20,sticky="ew")

        self.cholEntry = ctk.CTkEntry(self,placeholder_text="Enter the Cholestrol Level")
        self.cholEntry.grid(row=6,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Fasting Blood Pressure
        self.fastingLabel = ctk.CTkLabel(self,text="Fasting Blood Pressure(0 - 4)")
        self.fastingLabel.grid(row=7,column=0,padx=20,pady=20,sticky="ew")

        self.fastingEntry = ctk.CTkEntry(self,placeholder_text="Enter the value of Fasting Blood Pressure")
        self.fastingEntry.grid(row=7,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Electrocardiogram
        self.ecgLabel = ctk.CTkLabel(self,text="Electrocardiogram(0 , 1 ,2)")
        self.ecgLabel.grid(row=1,column=7,padx=20,pady=20,sticky="ew")

        self.ecgEntry = ctk.CTkEntry(self,placeholder_text="Enter level of ECG")
        self.ecgEntry.grid(row=1,column=8,columnspan=5,padx=20,pady=20,sticky="ew")

        #Thalach
        self.thalachLabel = ctk.CTkLabel(self,text="Thalach(71 - 201)")
        self.thalachLabel.grid(row=2,column=7,padx=20,pady=20,sticky="ew")

        self.thalachEntry = ctk.CTkEntry(self,placeholder_text="Enter the value of Thalach")
        self.thalachEntry.grid(row=2,column=8,columnspan=5,padx=20,pady=20,sticky="ew")

        #exAngina
        self.anginaLabel = ctk.CTkLabel(self,text="Angina")
        self.anginaLabel.grid(row=3,column=7,padx=20,pady=20,sticky="ew")

        #Angina Radio Buttons
        self.anginaVar = tk.StringVar(value="Choose")

        self.anginaYes = ctk.CTkRadioButton(self,text = "1",variable=self.anginaVar)
        self.anginaYes.grid(row=3,column=9,padx=20,pady=20,sticky="ew")


        self.anginaNo = ctk.CTkRadioButton(self,text = "0",variable=self.anginaVar)
        self.anginaNo.grid(row=3,column=10,padx=20,pady=20,sticky="ew")

        #Old Peak
        self.oldpeakLabel = ctk.CTkLabel(self,text="Old Peak(0 - 6.2)")
        self.oldpeakLabel.grid(row=4,column=7,padx=20,pady=20,sticky="ew")

        self.oldpeakEntry = ctk.CTkEntry(self,placeholder_text="Enter value of Old Peak")
        self.oldpeakEntry.grid(row=4,column=8,columnspan=5,padx=20,pady=20,sticky="ew")

         #Slope
        self.slopeLabel = ctk.CTkLabel(self,text="Slope(0 - 2)")
        self.slopeLabel.grid(row=6,column=7,padx=20,pady=20,sticky="ew")

        self.slopeEntry = ctk.CTkEntry(self,placeholder_text="Enter the value of Slope")
        self.slopeEntry.grid(row=6,column=8,columnspan=5,padx=20,pady=20,sticky="ew")


        #Coronary Artery
        self.caLabel = ctk.CTkLabel(self,text="Coronary Artery(0 - 3)")
        self.caLabel.grid(row=5,column=7,padx=20,pady=20,sticky="ew")

        self.caEntry = ctk.CTkEntry(self,placeholder_text="Enter value of C.A")
        self.caEntry.grid(row=5,column=8,columnspan=5,padx=20,pady=20,sticky="ew")

        #Thalassemia
        self.thalLabel = ctk.CTkLabel(self,text="Thalassemia")
        self.thalLabel.grid(row=7,column=7,padx=20,pady=20,sticky="ew")

        #Thalassemia Radio Buttons
        self.thalassemiaVar = tk.StringVar(value="Choose")

        self.thalassemiaYes = ctk.CTkRadioButton(self,text = "1",variable=self.thalassemiaVar)
        self.thalassemiaYes.grid(row=7,column=9,padx=20,pady=20,sticky="ew")


        self.thalassemiaNo = ctk.CTkRadioButton(self,text = "0",variable=self.thalassemiaVar)
        self.thalassemiaNo.grid(row=7,column=10,padx=20,pady=20,sticky="ew")

        #Generate button
        self.generateResultButton = ctk.CTkButton(self,text="Analyse")
        self.generateResultButton.grid(row = 16,column=6,padx=20,pady=20,sticky="ew")
        self.generateResultButton.configure(command=self.predict)
        
        #Information
        #self.infoLabel = ctk.CTkLabel(self,text="More Information on Heart Disease Prediction")
        #self.infoLabel.grid(row)

        #CopyRight

        #self.copyRightlabel  = ctk.CTkLabel(self,text="© Heart Disease Prediction Model, 2024")
        #self.copyRightlabel.grid(row=27,column=6,padx=20,pady=20,sticky="ew")
    
    def predict(self):
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
        #age = 58
        #gender = 1
        #chestpain = 0
        #rbp = 100
        #chol = 248
        #fasting = 0
        #ecg = 1
        #thalach = 122
        #angina = 0
        #oldpeak = 1
        #slope = 1
        #ca = 0


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

        #model_output_class = 1

        if model_output_class == 1:
            #messagebox.showinfo("Prediction", "High risk")
            heading_label=ctk.CTkLabel(self,text="High risk",font=('Arial',38,'bold'))    
        else:
            heading_label=ctk.CTkLabel(self,text="Low risk",font=('Arial',38,'bold'))
        
        heading_label.grid(row=25,column=4,columnspan=4,pady=20,sticky="ew")
        self.generateGraph = ctk.CTkButton(self,text="Graph")
        self.generateGraph.grid(row = 25,column=5,padx=20,pady=20,sticky="ew")
        self.generateGraph.configure(command=partial(self.generate_graph, model_output_class))

        self.generateMed = ctk.CTkButton(self,text="Precription",command=self.medicine)
        self.generateMed.grid(row = 26,column=5,padx=20,pady=20,sticky="ew")

        #self.generate_graph()
    
    def generate_graph(self,out_probs):
        self.wm_state('zoomed')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self = ctk.CTkToplevel(self)
        self.title("Graphs")
        self.geometry(f"{appWidth}x{appHeight}")

        df = pd.DataFrame(
            {
                "Model": ['Logistic Regression', 'Random Forest', 'k-NN', 'Decision Tree', 'SVM'],
                "Probability": out_probs
            }
        )
        fig = px.bar(df, x='Model', y='Probability',color='Model', text='Probability', height=400, template='plotly_white')
        # fig.show()
        pio.write_image(fig,"output_probs.png", format="png")
        
        #image = Image.open("output_probs.png")

        #grp_img = ctk.CTkImage(dark_image=image,size=(100,100))
        #grp_img_tk = ImageTk.PhotoImage(grp_img)

        grp_img = ctk.CTkImage(Image.open("output_probs.png"), size=(400, 400))


        #Save a reference
        #self.photos_refs.append(photo)

        lab = ctk.CTkLabel(self, image=grp_img)
        lab.grid(row=0,column=0, padx=10, pady=10, sticky="ew")


        #image = Image.open("output_probs.png")
        #self.photo = ctk.CTkImage(image=image)

        #label = ctk.CTkLabel(self,image=self.photo)
        #label.photo = self.photo
        #label.grid(row=0,column=0)
        
        #substituteWindow = tk.Tk()
        #text1 = tk.Text(new_window)
        #photo = tk.PhotoImage(file='output_probs.png')
        #text1.insert(tk.END, '\n')
        #text1.image_create(tk.END, image=photo)
        #text1.grid(row=12, rowspan=12, column=12)
        #substituteWindow.mainloop()
            
        # lbl = Label(mGui, image = tkimage)
        # lbl.place(x=0, y=0)

    #def __del__(self):

        #for photo in self.photos_refs:
            #photo.destroy()

    def medicine(self):

        self.title("Prescription")
        self.geometry(f"{appWidth}x{appHeight}")
        self = tk.Toplevel(self)
        self.wm_state('zoomed')


        heading_label = ctk.CTkLabel(self,text="PRESCRIPTION",font=('Arial',32,'bold'))
        heading_label.grid(row=0,column=4,columnspan=4,pady=20,sticky="ew")

        #Name
        self.nameLabel = ctk.CTkLabel(self,text="Name")
        self.nameLabel.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

        self.nameEntry = ctk.CTkEntry(self,placeholder_text="Enter Name")
        self.nameEntry.grid(row=1,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #Email
        self.emailLabel = ctk.CTkLabel(self,text="Email")
        self.emailLabel.grid(row=2,column=0,padx=20,pady=20,sticky="ew")

        self.emailEntry = ctk.CTkEntry(self,placeholder_text="abc@gmail.com")
        self.emailEntry.grid(row=2,column=1,columnspan=5,padx=20,pady=20,sticky="ew")

        #medicine

        self.med_label = ctk.CTkLabel(self,text="Medicine")
        self.med_label.grid(row=3,column=0,padx=20,pady=20,sticky="ew")

        #Medicine Combo Box
        self.medOption = ctk.CTkOptionMenu(self,values=["Aspirin",
                                                       "Atrovastatin",
                                                       "Metroprolol",
                                                       "Clopidogrel",
                                                       "Ramipril",
                                                       "Warfarin",
                                                       "Furosemide",
                                                       "Spironolactone",
                                                       "Isosorbide Mononitrate",
                                                       "Carvedilol"])
        self.medOption.grid(row=3,column=1,padx=20,pady=20,columnspan=8,sticky="ew")

        #Tablet
        self.tablet_label = ctk.CTkLabel(self,text="Tablet")
        self.tablet_label.grid(row=4,column=0,padx=20,pady=20,sticky="ew")

        #Tablet Combo Box
        self.tabletOption = ctk.CTkOptionMenu(self,values=["5mg","20mg",
                                                           "50mg","40mg","75mg"])
        self.tabletOption.grid(row=4,column=1,padx=20,pady=20,columnspan=8,sticky="ew")

        #Taking Time
        self.time_label = ctk.CTkLabel(self,text="Taking Time")
        self.time_label.grid(row=5,column=0,padx=20,pady=20,sticky="ew")

        #Choice Check Box Taking Time
        self.checkboxVar = tk.StringVar(value="Choice 1")

        self.choice1 = ctk.CTkCheckBox(self,text="Once a day",
                                       variable=self.checkboxVar,
                                       onvalue="choice1",
                                       offvalue="c1")
        self.choice1.grid(row=5,column=1,padx=20,pady=20,sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self,text="Twice a day",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")
        self.choice2.grid(row=5,column=2,padx=20,pady=20,sticky="ew")

        #Reason
        self.reason_label = ctk.CTkLabel(self,text="Reason")
        self.reason_label.grid(row=6,column=0,padx=20,pady=20,sticky="ew")

        self.reasonEntry = ctk.CTkEntry(self,placeholder_text="Reason for medication")
        self.reasonEntry.grid(row=6,column=1,columnspan=8,padx=20,pady=20,sticky="ew")

        #Generate Button
        self.generatePrescribe = ctk.CTkButton(self,text="Prescribe",command=self.generateText)
        self.generatePrescribe.grid(row = 7,column=1,padx=20,pady=20,sticky="ew")

        #Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200,height=100)
        self.displayBox.grid(row = 8,column=0,columnspan = 4,padx = 20,pady=20,sticky="ew")

    def generateText(self):
        self.displayBox.delete("0.0","200.0")
        text = self.createText()
        self.displayBox.insert("0.0",text)

    def createText(self):
        checkboxValue = ""

        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxValue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxValue += self.choice2.get()
        else:
            checkboxValue = "none of the available options"

        text = f"{self.nameEntry.get()} : \n{self.emailEntry.get()} :\n{self.medOption} :\n{self.tabletOption} :\n{checkboxValue} :\n{self.reasonEntry.get()}"
        
        return text

        

if __name__ == "__main__":
    app_instance = MainApp()

    app_instance.mainloop()



