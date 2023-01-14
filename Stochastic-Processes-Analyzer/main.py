import Functions
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

def Generate_Process():
    global FileName
    FileName = "D:\Self Development\Zewail collage material\Academic years\Year 3\Probability\Stochastic-Processes-Analyzer\Processes\Process_X.csv"
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
    FileName = filedialog.askopenfilename(initialdir="Home", title="Open CSV File",
                                          filetypes=(("csv Files", "*.csv"),))
    Process_X = Functions.OpenFile(FileName)
    if Process_X.any():
        FileName_Label.configure(text=FileName)
    else:
        messagebox.showerror("ERROR", "Can't open file!\n")


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
    root.geometry("735x550")
    root.title("Statistical Analysis Of Text Files")


# Frame 1
    Frame_1 = LabelFrame(root, padx=10, pady=22)

    # Create a labelbox widget
    FileName_Label = Label(Frame_1, text='', width=88, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")

    # Create Buttons
    button_Choose_File = Button(Frame_1, text="Browse File", state=ACTIVE, padx=22, pady=2, fg="blue",
                                command=lambda: GetInputFile())


# Shoving Frame 1 into the screen
    Frame_1.grid(row=0, column=0)
    FileName_Label.grid(row=0, column=1)
    button_Choose_File.grid(row=1, column=1)


# Frame 2
    Frame_2 = LabelFrame(root, padx=0, pady=0, text="Show M Ensembles of process")
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
    Frame_2.grid(row=1, column=0)
    Ensemble_Label.grid(row=0, column=0)
    Ensemble_TextBox.grid(row=0, column=1)
    Plot_M_Ensemble_Button.grid(row=0, column=2)

# Frame 3
    Frame_3 = LabelFrame(root, padx=0, pady=0, text="ACF")
    # ACF Label
    ACF_i_Label = Label(Frame_3, text='i:', width=10, height=1, borderwidth=3, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left")
    ACF_j_Label = Label(Frame_3, text='j:', width=10, height=1, borderwidth=3, bg="White", fg="Black",
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
    Frame_3.grid(row=1, column=1)
    ACF_i_Label.grid(row=0, column=0)
    ACF_i_TextBox.grid(row=0, column=1)
    ACF_j_Label.grid(row=0, column=3)
    ACF_j_TextBox.grid(row=0, column=4)
    Plot_ACF_Button.grid(row=1, column=2)

    # Generate main loop
    root.mainloop()