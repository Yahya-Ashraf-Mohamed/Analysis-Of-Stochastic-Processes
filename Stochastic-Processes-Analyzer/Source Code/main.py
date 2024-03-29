import Functions
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os

OutPutName = os.getcwd() + "\OutPut File"
def Generate_Process():
    global FileName
    FileName = os.getcwd() + "\Processes\Process_X.csv"

    global Process_X
    Process_X = Functions.OpenFile(FileName)
    #Functions.Plot_Process(Process_X, "X[t] Graph", "Time [t]", "X[t]")

    # Y(t) = βsin(2πt), where 0 ≤ t ≤ 2, β∼N(0, 1)
    global Process_Y
    Process_Y = Functions.GenerateProcess_Y()
    #Functions.Plot_Process(Process_Y, "Y[t] Graph", "Time [t]", "Y[t]")
    Functions.Save_Process(os.getcwd()+ "\Processes","\Process_Y", Process_Y)

    # Z(t) = X(t) * Y(t)
    global Process_Z
    Process_Z = Functions.GenerateProcess_Z(Process_X, Process_Y)
    #Functions.Plot_Process(Process_Z, "Z[t] Graph", "Time [t]", "Z[t]")
    Functions.Save_Process(os.getcwd()+ "\Processes","\Process_Z", Process_Z)

    # P(t) is a 10-bits Polar NRZ process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    global Process_P
    Process_P = Functions.GenerateProcess_P(10, 5, 2)   # bits, A, Tb
    #Functions.Plot_Process(Process_P, "P[t] Graph", "Time [t]", "P[t]")
    Functions.Save_Process(os.getcwd()+ "\Processes","\Process_P", Process_P)

    # M(t) is a 10-bits Manchester code process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    global Process_M
    Process_M = Functions.GenerateProcess_M(10, 5, 2) # bits, A, Tb
    #Functions.Plot_Process(Process_M, "M[t] Graph", "Time [t]", "M[t]")
    Functions.Save_Process(os.getcwd()+ "\Processes","\Process_M", Process_M)

    global i
    global j
    global M
    global n
# Browse for input file then print its name in the text box
def GetInputFile():
    global FileName
    try:
        FileName = filedialog.askopenfilename(initialdir="Home", title="Open CSV File",
                                              filetypes=(("csv Files", "*.csv"),))

        Process_X = Functions.OpenFile(FileName)

        if Process_X.any():
            FileName_Label.delete(0, END)
            FileName_Label.insert(0,FileName)
        else:
            messagebox.showerror("ERROR", "Can't open file!\n")
    except:
        messagebox.showerror("ERROR", "An Error Occurred!\n")

def Get_Choosen_Process(Chosen_Processes):
    match Chosen_Processes:
        case "X(t)":
            return Process_X
        case "Y(t)":
            return Process_Y
        case "Z(t)":
            return Process_Z
        case "P(t)":
            return Process_P
        case "M(t)":
            return Process_M
        case default:
            return Process_X

def Calculate_Ensamble_Mean(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    Ensamble_Mean = Functions.Calculate_Ensamble_Mean(Processe)

    Calculation_TextBox.config(state=NORMAL)
    Calculation_TextBox.delete(0, END)
    Calculation_TextBox.insert(0, str(Ensamble_Mean))
    Calculation_TextBox.config(state=DISABLED)
    messagebox.showinfo("Mean", str(Ensamble_Mean))

    if(Functions.Save_Output_File("Ensemble Mean", Ensamble_Mean, OutPutName) == True):
        messagebox.showinfo("Save", "Ensemble Mean Saved Successfully in Output file")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)

def Calculate_Time_ACF(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    Time_ACF = Functions.Calculate_Time_ACF(Processe)

    Calculation_TextBox.config(state=NORMAL)
    Calculation_TextBox.delete(0, END)
    Calculation_TextBox.insert(0, str(Time_ACF))
    Calculation_TextBox.config(state=DISABLED)
    messagebox.showinfo("Time ACF", str(Time_ACF))

    if (Functions.Save_Output_File("Time ACF", Time_ACF, OutPutName) == True):
        messagebox.showinfo("Save", "Time ACF Saved Successfully in Output file")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)

def Click_Show_Plot_M_Ensemble_Button(key):
    # Open button
    Plot_M_Ensemble_Button.configure(state=ACTIVE)

def Click_Show_Plot_N_Time_ACF_Button(key):
    # Open button
    Plot_N_Time_ACF_Button.configure(state=ACTIVE)

def Click_Show_Plot_N_Time_Mean_Button(key):
    # Open button
    Plot_N_Time_Mean_Button.configure(state=ACTIVE)

def Click_Show_ACF_i_Button(key):
    # Open button
    if(int(ACF_j_TextBox.get())):
        Plot_ACF_Button.configure(state=ACTIVE)
        Calculate_ACF_Button.configure(state=ACTIVE)
        #i = int(ACF_i_TextBox.get(1.0, END))
        #messagebox.showerror("ERROR", "Enter number of i sample you want!\n")

def Click_Show_ACF_j_Button(key):
    # Open button
    if (int(ACF_i_TextBox.get())):
        Plot_ACF_Button.configure(state=ACTIVE)
        Calculate_ACF_Button.configure(state=ACTIVE)
#        j = int(ACF_j_TextBox.get(1.0, END))
#        messagebox.showerror("ERROR", "Enter number of j sample you want!\n")

def Plot_M_Ensable(Chosen_Processe):
    try:
        M = int(Ensemble_TextBox.get())
        Processe = Get_Choosen_Process(Chosen_Processe)
        Functions.plot_M_samples(Processe, M)
    except:
        messagebox.showerror("ERROR", "Enter an integer number!\n")


def Calc_TMean(Chosen_Processe):
    try:
        N = int(Time_Mean_TextBox.get())
        Processe = Get_Choosen_Process(Chosen_Processe)
        Time_Mean = Functions.Calculate_Time_Mean(Processe, N)
        TMean_TextBox.config(state=NORMAL)
        TMean_TextBox.delete(0, END)
        TMean_TextBox.insert(0, str(Time_Mean))
        TMean_TextBox.config(state=DISABLED)
        messagebox.showinfo("Time Mean", str(Time_Mean))

        if (Functions.Save_Output_File("Time Mean", Time_Mean, OutPutName) == True):
            messagebox.showinfo("Save", "Time Mean Saved Successfully in Output file")
        else:
            messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)
    except:
        messagebox.showerror("ERROR", "Enter an integer number!\n")


def Plot_Time_ACF (Chosen_Processe):
    try:
        N = int(Time_ACF_TextBox.get())
        Processe = Get_Choosen_Process(Chosen_Processe)
        Functions.Plot_Time_ACF(Processe, N)
    except:
        messagebox.showerror("ERROR", "Enter an integer number!\n")

def Calc_Total_Average_Power(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    TAP = Functions.Calculate_total_average_power(Processe)

    Calculation_TextBox.config(state=NORMAL)
    Calculation_TextBox.delete(0, END)
    Calculation_TextBox.insert(0, str(TAP))
    Calculation_TextBox.config(state=DISABLED)
    messagebox.showinfo("Total Average Power", str(TAP))

    if (Functions.Save_Output_File("Total Average Power", TAP, OutPutName) == True):
        messagebox.showinfo("Save", "Total Average Power Saved Successfully in Output file")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)

def Plot_Ensemble_Mean(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    Functions.Plot_Ensemble_Mean(Processe)

def Plot_Power_Spectral_Density(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    Functions.plot_PSD(Processe)

def Calc_Power_Spectral_Density(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    PSD, freq= Functions.Calc_PSD(Processe)

    Calculation_TextBox.config(state=NORMAL)
    Calculation_TextBox.delete(0, END)
    Calculation_TextBox.insert(0, str(PSD))
    Calculation_TextBox.config(state=DISABLED)
    messagebox.showinfo("Power Spectral Density", str(PSD))

    if (Functions.Save_Output_File("Power Spectral Density", PSD, OutPutName) == True):
        messagebox.showinfo("Save", "Power Spectral Density Saved Successfully in Output file")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)

def Calc_ACF(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    i = int(ACF_i_TextBox.get())
    j = int(ACF_j_TextBox.get())
    ACF = Functions.Calculate_ACF(Processe, i, j)

    ACF_TextBox.config(state=NORMAL)
    ACF_TextBox.delete(0, END)
    ACF_TextBox.insert(0, str(ACF))
    ACF_TextBox.config(state=DISABLED)
    messagebox.showinfo("Auto Correlation Function", str(ACF))

    if (Functions.Save_Output_File("Auto Correlation Function", ACF, OutPutName) == True):
        messagebox.showinfo("Save", "Auto Correlation Function Saved Successfully in Output file")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + OutPutName)


def Plot_3D_ACF(Chosen_Processe):
    Processe = Get_Choosen_Process(Chosen_Processe)
    i = int(ACF_i_TextBox.get())
    j = int(ACF_j_TextBox.get())
    try:
        Functions.plot_3D_ACF(Processe, i, j)
    except:
        messagebox.showerror("ERROR", "An Error Occurred")
        

if __name__ == '__main__':

    Functions.Clear_Saved_Output_File(OutPutName)
    # Generate Processes
    Generate_Process()
    global Process
    Process = Process_X

    # Main App
    root = Tk()
    root.geometry("420x415")
    root.title("Statistical Analysis Of Text Files")

# ==================================================================================================================== #
# Frame 1
    Frame_1 = LabelFrame(root, padx=0, pady=0)

    # Create a labelbox widget
    FileName_Label = Entry(Frame_1, width=55, borderwidth=5, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    FileName_Label.insert(0, "Default Process X generated.")
    # Create Buttons
    button_Choose_File = Button(Frame_1, text="Browse File", state=ACTIVE, padx=22, pady=2, fg="blue",
                                command=lambda: GetInputFile())


# Shoving Frame 1 into the screen
    Frame_1.place(x=10,y=10)
    FileName_Label.pack()
    button_Choose_File.pack()

# ==================================================================================================================== #
    # Frame 8
    Frame_8 = LabelFrame(root, padx=0, pady=0)

    # Create Radio buttons
    Processes = [
        ("X(t)", "X(t)"),
        ("Y(t)", "Y(t)"),
        ("Z(t)", "Z(t)"),
        ("P(t)", "P(t)"),
        ("M(t)", "M(t)"),
    ]

    global Chosen_Processes
    Chosen_Processes = StringVar()
    Chosen_Processes.set("X(t)")

    column = 0
    for text, mode in Processes:
        Radiobutton(Frame_8, text=text, variable=Chosen_Processes, value=mode).grid(row=0, column=column)
        column = column + 1

    # Shoving Frame 8 into the screen
    Frame_8.place(x=10, y=75)

# ==================================================================================================================== #
# Frame 6
    Frame_6 = LabelFrame(root, padx=0, pady=0, text="Calculate")

    # Output TextBox
    Calculation_TextBox = Entry(Frame_6, width=65, borderwidth=5, bg="White", fg="Black", state=DISABLED)

    # Create Buttons
    Ensemble_Mean_Button = Button(Frame_6, text="Ensemble Mean", state=ACTIVE, padx=10, pady=2, fg="Black",
                                  command=lambda: Calculate_Ensamble_Mean(Chosen_Processes.get()))
    Power_Spectral_Density_Button = Button(Frame_6, text="Power Spectral Density", state=ACTIVE, padx=5, pady=2, fg="Black",
                             command=lambda: Calc_Power_Spectral_Density(Chosen_Processes.get()))
    Total_Average_Power_Button = Button(Frame_6, text="Total_Average_Power", state=ACTIVE, padx=5, pady=2, fg="Black",
                                        command=lambda: Calc_Total_Average_Power(Chosen_Processes.get()))

    # Shoving Frame 6 into the screen
    Frame_6.place(x=10, y=110)
    Calculation_TextBox.pack(side=TOP)
    Ensemble_Mean_Button.pack(side=LEFT)
    Power_Spectral_Density_Button.place(x=122, y=27)
    Total_Average_Power_Button.pack(side=RIGHT)

# ==================================================================================================================== #
# Frame 2
    Frame_2 = LabelFrame(root, padx=0, pady=0, text="Plot Show M Ensembles of process")
    # Ensemble Label
    Ensemble_Label = Label(Frame_2, text='Ensembles: ', width=10, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    # Text box for M samples
    Ensemble_TextBox = Entry(Frame_2, width=10, borderwidth=5, bg="White", fg="Black")
    Ensemble_TextBox.bind("<Key>", Click_Show_Plot_M_Ensemble_Button)

    # Create Buttons
    Plot_M_Ensemble_Button = Button(Frame_2, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                command=lambda: Plot_M_Ensable(Chosen_Processes.get()))

# Shoving Frame 2 into the screen
    Frame_2.place(x=10, y=195)
    Ensemble_Label.pack(side="left")
    Ensemble_TextBox.pack(side="left")
    Plot_M_Ensemble_Button.pack(side="right")

# ==================================================================================================================== #
# Frame 3
    Frame_3 = LabelFrame(root, padx=1, pady=1, text="Plot ACF")
    # ACF Label
    ACF_TextBox = Entry(Frame_3, width=10, borderwidth=5, bg="White", fg="Black", state=DISABLED)

    ACF_i_Label = Label(Frame_3, text='i:', width=2, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    ACF_j_Label = Label(Frame_3, text='j:', width=2, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")

    # Text box for ACF
    ACF_i_TextBox = Entry(Frame_3, width=10, borderwidth=5, bg="White", fg="Black")
    ACF_i_TextBox.bind("<Key>", Click_Show_ACF_i_Button)
    ACF_j_TextBox = Entry(Frame_3, width=10, borderwidth=5, bg="White", fg="Black")
    ACF_j_TextBox.bind("<Key>", Click_Show_ACF_j_Button)

    # Create Button
    Plot_ACF_Button = Button(Frame_3, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                    command=lambda: Plot_3D_ACF(Chosen_Processes.get()))
    Calculate_ACF_Button = Button(Frame_3, text="Calc", state=DISABLED, padx=15, pady=2, fg="Black",
                             command=lambda: Calc_ACF(Chosen_Processes.get()), font=('Helvetica', 10))

# Shoving Frame 3 into the screen
    Frame_3.place(x=260, y=195)
    ACF_TextBox.grid(row=2, column=1)

    ACF_i_Label.grid(row=0, column=0)
    ACF_i_TextBox.grid(row=0, column=1)

    ACF_j_Label.grid(row=1, column=0)
    ACF_j_TextBox.grid(row=1, column=1)

    Calculate_ACF_Button.grid(row=2, column=0)
    Plot_ACF_Button.grid(row=3, column=1)


# ==================================================================================================================== #
# Frame 4
    Frame_4 = LabelFrame(root, padx=0, pady=0, text="Plot Time Mean of N samples")
    # Ensemble Label
    Time_Mean_Label = Label(Frame_4, text='N Samples: ', width=12, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    # Text box for M samples
    Time_Mean_TextBox = Entry(Frame_4, width=20, borderwidth=5, bg="White", fg="Black")
    Time_Mean_TextBox.bind("<Key>", Click_Show_Plot_N_Time_Mean_Button)

    TMean_TextBox = Entry(Frame_4, width=20, borderwidth=5, bg="White", fg="Black", state=DISABLED)

    # Create Buttons
    Plot_N_Time_Mean_Button = Button(Frame_4, text="Plot", state=DISABLED, padx=27, pady=2, fg="Black",
                                command=lambda: Calc_TMean(Chosen_Processes.get()))

# Shoving Frame 4 into the screen
    Frame_4.place(x=10, y=260)
    Time_Mean_Label.grid(row=0, column=0)
    Time_Mean_TextBox.grid(row=0, column=1)
    Plot_N_Time_Mean_Button.grid(row=1, column=0)
    TMean_TextBox.grid(row=1, column=1)

# ==================================================================================================================== #
# Frame 5
    Frame_5 = LabelFrame(root, padx=0, pady=0, text="Plot Time ACF of N samples")
    # Ensemble Label
    Time_ACF_Label = Label(Frame_5, text='N Samples: ', width=10, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    # Text box for M samples
    Time_ACF_TextBox = Entry(Frame_5, width=10, borderwidth=5, bg="White", fg="Black")
    Time_ACF_TextBox.bind("<Key>", Click_Show_Plot_N_Time_ACF_Button)

    # Create Buttons
    Plot_N_Time_ACF_Button = Button(Frame_5, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                    command=lambda: Plot_Time_ACF(Chosen_Processes.get()))

# Shoving Frame 5 into the screen
    Frame_5.place(x=10, y=351)
    Time_ACF_Label.pack(side="left")
    Time_ACF_TextBox.pack(side="left")
    Plot_N_Time_ACF_Button.pack(side="right")

# ==================================================================================================================== #
# Frame 7
    Frame_7 = LabelFrame(root, padx=0, pady=0, text="Plot")

    # Create Buttons
    Plot_Ensemble_Mean_Button = Button(Frame_7, text="Ensemble Mean", state=ACTIVE, padx=22, pady=2, fg="Black",
                                  command=lambda: Plot_Ensemble_Mean(Chosen_Processes.get()))
    Plot_Power_Spectral_Density_Button = Button(Frame_7, text="Power Spectral Density", state=ACTIVE, padx=5, pady=2, fg="Black",
                             command=lambda: Plot_Power_Spectral_Density(Chosen_Processes.get()))

    # Shoving Frame 7 into the screen
    Frame_7.place(x=260, y=325)
    Plot_Ensemble_Mean_Button.pack(side=TOP)
    Plot_Power_Spectral_Density_Button.pack(side=BOTTOM)

# ==================================================================================================================== #
# Generate main loop
    root.mainloop()