import Functions
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

def Generate_Process():
    global FileName
    FileName = "D:\Self Development\Zewail collage material\Academic years\Year 3\Probability\Stochastic-Processes-Analyzer\Processes\Process_X.csv"

    global Process_X
    Process_X = Functions.OpenFile(FileName)
    #Functions.Plot_Process(Process_X, "X[t] Graph", "Time [t]", "X[t]")

    # Y(t) = βsin(2πt), where 0 ≤ t ≤ 2, β∼N(0, 1)
    global Process_Y
    Process_Y = Functions.GenerateProcess_Y()
    #Functions.Plot_Process(Process_Y, "Y[t] Graph", "Time [t]", "Y[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_Y", Process_Y)

    # Z(t) = X(t) * Y(t)
    global Process_Z
    Process_Z = Functions.GenerateProcess_Z(Process_X, Process_Y)
    #Functions.Plot_Process(Process_Z, "Z[t] Graph", "Time [t]", "Z[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_Z", Process_Z)

    # P(t) is a 10-bits Polar NRZ process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    global Process_P
    Process_P = Functions.GenerateProcess_P(10, 5, 2)   # bits, A, Tb
    #Functions.Plot_Process(Process_P, "P[t] Graph", "Time [t]", "P[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_P", Process_P)

    # M(t) is a 10-bits Manchester code process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    global Process_M
    Process_M = Functions.GenerateProcess_M(10, 5, 2) # bits, A, Tb
    #Functions.Plot_Process(Process_M, "M[t] Graph", "Time [t]", "M[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_M", Process_M)

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

def Click_Show_Plot_M_Ensemble_Button(key):
    # Open button
    try:
        M = int(ACF_i_TextBox.get())
        if(M):
            Plot_M_Ensemble_Button.configure(state=ACTIVE, bg="Green")
    except:
        messagebox.showerror("ERROR", "Enter number of i sample you want!\n")
def Click_Show_ACF_i_Button(key):
    # Open button
    try:
        i = int(ACF_i_TextBox.get())
        if(j):
            Plot_ACF_Button.configure(state=ACTIVE, bg="Green")
    except:
        messagebox.showerror("ERROR", "Enter number of i sample you want!\n")

def Click_Show_ACF_j_Button(key):
    # Open button
    try:
        j = int(ACF_j_TextBox.get())
        if (i):
            Plot_ACF_Button.configure(state=ACTIVE, bg="Green")
    except:
        messagebox.showerror("ERROR", "Enter number of j sample you want!\n")


if __name__ == '__main__':

    # Generate Processes
    Generate_Process()

    # Main App
    root = Tk()
    root.geometry("420x380")
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
# Frame 6
    Frame_6 = LabelFrame(root, padx=0, pady=0, text="Calculate")

    # Output TextBox
    Time_ACF_TextBox = Entry(Frame_6, width=65, borderwidth=5, bg="White", fg="Black", state=DISABLED)

    # Create Buttons
    Ensemble_Mean_Button = Button(Frame_6, text="Ensemble Mean", state=ACTIVE, padx=20, pady=2, fg="Black",
                                  command=lambda: GetInputFile())
    Time_ACF_Button = Button(Frame_6, text="Time_ACF", state=ACTIVE, padx=20, pady=2, fg="Black",
                             command=lambda: GetInputFile())
    Total_Average_Power_Button = Button(Frame_6, text="Total_Average_Power", state=ACTIVE, padx=20, pady=2, fg="Black",
                                        command=lambda: GetInputFile())

    # Shoving Frame 6 into the screen
    Frame_6.place(x=10, y=75)
    Time_ACF_TextBox.pack(side=TOP)
    Ensemble_Mean_Button.pack(side=LEFT)
    Time_ACF_Button.place(x=135, y=27)
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
                                command=lambda: GetInputFile())

# Shoving Frame 2 into the screen
    Frame_2.place(x=10, y=160)
    Ensemble_Label.pack(side="left")
    Ensemble_TextBox.pack(side="left")
    Plot_M_Ensemble_Button.pack(side="right")

# ==================================================================================================================== #
# Frame 3
    Frame_3 = LabelFrame(root, padx=10, pady=10, text="Plot ACF")
    # ACF Label
    ACF_i_Label = Label(Frame_3, text='i:', width=5, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    ACF_j_Label = Label(Frame_3, text='j:', width=5, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")

    # Text box for ACF
    ACF_i_TextBox = Entry(Frame_3, width=10, borderwidth=5, bg="White", fg="Black")
    ACF_i_TextBox.bind("<Key>", Click_Show_ACF_i_Button)
    ACF_j_TextBox = Entry(Frame_3, width=10, borderwidth=5, bg="White", fg="Black")
    ACF_j_TextBox.bind("<Key>", Click_Show_ACF_j_Button)

    # Create Button
    Plot_ACF_Button = Button(Frame_3, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                    command=lambda: GetInputFile())

# Shoving Frame 3 into the screen
    Frame_3.place(x=260, y=160)
    ACF_i_Label.grid(row=0, column=0)
    ACF_i_TextBox.grid(row=0, column=1)

    ACF_j_Label.grid(row=1, column=0)
    ACF_j_TextBox.grid(row=1, column=1)

    Plot_ACF_Button.grid(row=2, column=1)

# ==================================================================================================================== #
# Frame 4
    Frame_4 = LabelFrame(root, padx=0, pady=0, text="Plot Time Mean of N samples")
    # Ensemble Label
    Time_Mean_Label = Label(Frame_4, text='N Samples: ', width=10, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    # Text box for M samples
    Time_Mean_TextBox = Entry(Frame_4, width=10, borderwidth=5, bg="White", fg="Black")
    Time_Mean_TextBox.bind("<Key>", Click_Show_Plot_M_Ensemble_Button)

    # Create Buttons
    Plot_N_Time_Mean_Button = Button(Frame_4, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                command=lambda: GetInputFile())

# Shoving Frame 4 into the screen
    Frame_4.place(x=10, y=238)
    Time_Mean_Label.pack(side="left")
    Time_Mean_TextBox.pack(side="left")
    Plot_N_Time_Mean_Button.pack(side="right")

# ==================================================================================================================== #
# Frame 5
    Frame_5 = LabelFrame(root, padx=0, pady=0, text="Plot Time ACF of N samples")
    # Ensemble Label
    Time_ACF_Label = Label(Frame_5, text='N Samples: ', width=10, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    # Text box for M samples
    Time_ACF_TextBox = Entry(Frame_5, width=10, borderwidth=5, bg="White", fg="Black")
    Time_ACF_TextBox.bind("<Key>", Click_Show_Plot_M_Ensemble_Button)

    # Create Buttons
    Plot_N_Time_ACF_Button = Button(Frame_5, text="Plot", state=DISABLED, padx=22, pady=2, fg="Black",
                                    command=lambda: GetInputFile())

# Shoving Frame 5 into the screen
    Frame_5.place(x=10, y=316)
    Time_ACF_Label.pack(side="left")
    Time_ACF_TextBox.pack(side="left")
    Plot_N_Time_ACF_Button.pack(side="right")

# ==================================================================================================================== #
# Frame 6
    Frame_7 = LabelFrame(root, padx=0, pady=0, text="Plot")

    # Create Buttons
    Ensemble_Mean_Button = Button(Frame_7, text="Ensemble Mean", state=ACTIVE, padx=20, pady=2, fg="Black",
                                  command=lambda: GetInputFile())
    Time_ACF_Button = Button(Frame_7, text="Time_ACF", state=ACTIVE, padx=35, pady=2, fg="Black",
                             command=lambda: GetInputFile())

    # Shoving Frame 6 into the screen
    Frame_7.place(x=260, y=290)
    Ensemble_Mean_Button.pack(side=TOP)
    Time_ACF_Button.pack(side=BOTTOM)

# ==================================================================================================================== #
# Generate main loop
    root.mainloop()