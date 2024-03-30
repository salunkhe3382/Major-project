import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")

appWidth,appHeight = 1440,900

self = ctk.CTk()

def medicine(self):
    

        self.title("Prescription")
        self.geometry(f"{appWidth}x{appHeight}")

        self.wm_state('zoomed')


        heading_label = ctk.CTkLabel(self,text="PRESCRIPTION",font=('Arial',32,'bold'))
        heading_label.grid(row=0,column=4,columnspan=4,pady=20,sticky="ew")

        #medicine

        self.med_label = ctk.CTkLabel(self,text="Medicine")
        self.med_label.grid(row=2,column=0,padx=20,pady=20,sticky="ew")

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
        self.medOption.grid(row=2,column=1,padx=20,pady=20,columnspan=8,sticky="ew")

        #Tablet
        self.tablet_label = ctk.CTkLabel(self,text="Tablet")
        self.tablet_label.grid(row=3,column=0,padx=20,pady=20,sticky="ew")

        #Tablet Combo Box
        self.tabletOption = ctk.CTkOptionMenu(self,values=["5mg","20mg",
                                                           "50mg","40mg","75mg"])
        self.tabletOption.grid(row=3,column=1,padx=20,pady=20,columnspan=8,sticky="ew")

        #Taking Time
        self.time_label = ctk.CTkLabel(self,text="Taking Time")
        self.time_label.grid(row=4,column=0,padx=20,pady=20,sticky="ew")

        #Choice Check Box Taking Time
        self.checkboxVar = tk.StringVar(value="Choice 1")

        self.choice1 = ctk.CTkCheckBox(self,text="Once a day",
                                       variable=self.checkboxVar,
                                       onvalue="choice1",
                                       offvalue="c1")
        self.choice1.grid(row=4,column=1,padx=20,pady=20,sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self,text="Twice a day",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")
        self.choice2.grid(row=4,column=2,padx=20,pady=20,sticky="ew")

        #Reason
        self.reason_label = ctk.CTkLabel(self,text="Reason")
        self.reason_label.grid(row=5,column=0,padx=20,pady=20,sticky="ew")

        self.reasonEntry = ctk.CTkEntry(self,placeholder_text="Reason for medication")
        self.reasonEntry.grid(row=5,column=1,columnspan=8,padx=20,pady=20,sticky="ew")

        #Generate Button
        self.generateResultButton = ctk.CTkButton(self,text="Prescribe")
        self.generateResultButton.grid(row = 6,column=3,padx=20,pady=20,sticky="ew")









if __name__ == "__main__":
    app = medicine()

    app.mainloop()




