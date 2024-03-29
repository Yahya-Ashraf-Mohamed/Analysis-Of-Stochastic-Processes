import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt
#from .colors import Colormap, Normalize
from collections.abc import Mapping
import pandas as pd


t = np.arange(0, 2.1, 0.1)  # Generate time with step 0.1

# X(t) from input file
def OpenFile(FileName):
    try:
        Process_X = np.loadtxt(open(FileName, "rb"), delimiter=",")
        return Process_X
    except:
        return False


# Y(t) = βsin(2πt), where 0 ≤ t ≤ 2, β∼N(0, 1)
def GenerateProcess_Y():
    Process_Y = np.zeros((101, 21))
    β = np.random.uniform(low=0, high=1, size=(100,))
    Process_Y[0] = t
    for i in range(1, 101):
        Process_Y[i] = β[i - 1] * np.sin(2 * np.pi * t)
    return Process_Y


# Z(t) = X(t) * Y(t)
def GenerateProcess_Z(Process_X, Process_Y):
    Process_Z = np.zeros((101, 21))
    Process_Z[0] = t
    Process_Z[1:] = np.multiply(Process_X[1:, 0:21], Process_Y[1: ])
    return Process_Z


# Save the process
def Save_Process(File_Location,Process_File_Name, Process_Data):
    CompletePath = File_Location + Process_File_Name+".csv"
    savetxt(CompletePath, Process_Data, delimiter=",")

# Plot the process
def Plot_Process(Process ,Graph_Title, Graph_xlable, Graph_ylable):
    plt.plot(Process[0], Process[1])
    plt.title(Graph_Title)
    plt.xlabel(Graph_xlable)
    plt.ylabel(Graph_ylable)
    plt.show()


# Generate Random Bits
def random_bits(n):
    bits = []
    for i in range(10):
        bits.append(np.random.choice([0, 1]))
    return bits



def Polar_NRZ_signal(Bits, Tb, Shift_Value, A):
    T = len(Bits) * Tb
    steps = 20
    N = steps * len(Bits)
    dt = T / N
    t = np.arange(0, T, dt)

    tamplet = np.zeros(len(t))
    shift = Shift_Value / dt

    # generate line code
    for i in range(len(Bits)):
        if Bits[i] == 1:
            tamplet[i * steps:int((i + 1) * steps)] = A
        elif Bits[i] == 0:
            tamplet[i * steps:int((i + 1) * steps)] = -A

    P = np.zeros(len(t))
    P[int(shift):] = tamplet[:len(tamplet) - int(shift)]
    return t, P

# P(t) is a 10-bits Polar NRZ process,
# with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
def GenerateProcess_P(BitsNum, A, Tb):
    Process_P = np.zeros((101, 200))
    α = np.random.uniform(low=0, high=Tb, size=(100,))

    for i in range(0, len(α)):
        bits = random_bits(BitsNum)
        time, P = Polar_NRZ_signal(bits, 2, α[i], A)
        Process_P[i + 1] = P
    Process_P[0] = time
    return Process_P




def manchester_signal(Bits, Tb, Shift_Value,A):
    T = len(Bits) * Tb
    steps = 20
    N = steps * len(Bits)
    dt = T / N
    t = np.arange(0, T, dt)
    template = np.zeros(len(t))
    my_shift = int(Shift_Value / dt)

    # generate line code
    for i in range(len(Bits)):
        if Bits[i] == 1:
            template[i * steps:int((i + 0.5) * steps)] = 5
            template[int((i + 0.5) * steps):(i + 1) * steps] = -5
        elif Bits[i] == 0:
            template[i * steps:int((i + 0.5) * steps)] = -5
            template[int((i + 0.5) * steps):(i + 1) * steps] = 5
    M = np.zeros(len(t))
    M[my_shift:] = template[:len(template) - my_shift]
    return t, M


# M(t) is a 10-bits Manchester code process,
# with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
def GenerateProcess_M(BitsNum, A, Tb):
    Process_M = np.zeros((101, 200))
    α = np.random.uniform(low=0, high=Tb, size=(100,))

    for i in range(0, len(α)):
        bits = random_bits(BitsNum)
        time, M = manchester_signal(bits, 2, α[i], A)
        Process_M[i + 1] = M

    Process_M[0] = time
    return Process_M


def Clear_Saved_Output_File(FileName):
    try:
        FileHandel = open(FileName, 'w')
        Text = ""
        FileHandel.write(Text)
        FileHandel.close()
        return True
    except:
        return False


def Save_Output_File(Otput_Name, Ensamble_Mean, FileName):
    try:
        FileHandel = open(FileName, 'r')
        Text = FileHandel.read()
        FileHandel.close()
        FileHandel = open(FileName, 'w')
        Text = Text + str(Otput_Name) + " \n" + \
               "===============" + " \n" + \
               str(Ensamble_Mean) + "\n\n"

        FileHandel.write(Text)
        FileHandel.close()
        return True
    except:
        return False

# =================================================================================================================== #

def Calculate_Ensamble_Mean(Processe):
    samples = Processe[1:]
    return Processe.sum(axis=0) / len(Processe)

def Calculate_ACF(Processe, i, j):
    samples = Processe[1:]
    ACF = samples[:, i] * samples[:, j].sum() / (len(samples))
    return ACF

# TODO Not working!
def Calculate_3D_ACF(Processe, i, j):
    Time_Vector = Processe[0]
    Total_ACF = np.zeros((len(Time_Vector), len(Time_Vector)))
    for x in range(i):
        for y in range(j):
            ACF = np.array(Calculate_ACF(Processe, x, y))
            Total_ACF[x,y] = ACF        # ERROR!
    return Total_ACF

def Calculate_Time_Mean(Processe, N):
    Time_Vector = Processe[0]
    sample = Processe[1:]

    signal = sample[N]
    dt = Time_Vector[1] - Time_Vector[0]
    time_mean = np.sum(signal) * dt / (Time_Vector[-1] - Time_Vector[0])
    return time_mean

def plot_M_samples(Processe, M):
    Time_Vector = Processe[0]
    samples = Processe[np.random.randint(Processe.shape[1], size=M)]
    fig, axs = plt.subplots(M)
    fig.set_figheight(7)
    fig.set_figwidth(8)
    fig.suptitle(f"Graph of {M} Samples of the signal")
    for i in range(M):
        axs[i].plot(Time_Vector, samples[i])
        axs[i].set_title(f"Realization {i + 1}")

    plt.show()

def Plot_Ensemble_Mean(Processe):
    Time_Vector = Processe[0]
    samples = Calculate_Ensamble_Mean(Processe)
    plt.plot(Time_Vector, samples)
    plt.title("Ensemble Mean Graph")
    plt.xlabel("Time (t)")
    plt.ylabel("Ensemble Mean")
    plt.grid()
    plt.show()

def plot_3D_ACF(Processe, i, j):
    Time_Vector = Processe[0]
    Total_ACF = Calculate_3D_ACF(Processe, i, j)
    X, Y = np.meshgrid(Time_Vector, Time_Vector)

    fig, ax = plt.subplots(subplot_kw={"3D"})
    surf = ax.plot_surface(X, Y, Total_ACF)

    ax.set_title(f"Auto Correlation Function Graph")
    ax.set_xlabel("i")
    ax.set_ylabel("j")
    ax.set_zlabel("Rx")
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.view_init(45, 45)
    plt.show()

def Plot_Time_ACF(Processe, N):
    Time_Vector = Processe[0]
    signal = Processe[N]
    samples_difference = np.arange(0, len(Time_Vector), 1)
    τs = Time_Vector
    time_ACF = np.zeros(len(τs))
    for delta in samples_difference:
        t1 = 0
        t2 = int(delta)
        dt = Time_Vector[1] - Time_Vector[0]

        while t2 < len(Time_Vector):
            time_ACF[int(delta)] += signal[int(t1)] * signal[int(t2)] * dt / len(Time_Vector)
            t1 += dt
            t2 += dt

    plt.plot(τs, time_ACF)
    plt.xlabel("τ")
    plt.ylabel("Time ACF")
    plt.title("Time ACF vs τ Graph")
    plt.grid()
    plt.show()


def plot_PSD(Processe):
    PSD, freqs= Calc_PSD(Processe)
    plt.xlabel("Frequency (rad/sec)")
    plt.ylabel("PSD")
    plt.plot(freqs, PSD)
    plt.show()

    return PSD

def Calc_PSD(Processe):
    Time_Vector = Processe[0]
    sample = Processe[1:]
    n = len(Time_Vector)
    fs = int(n/(Time_Vector[-1]-Time_Vector[0]))
    freqs = np.arange(-n/2,n/2,1)*(fs/n)
    PSD = np.zeros(len(freqs))
    T = Time_Vector[-1] - Time_Vector[0]
    for i in range(len(sample)):
        FT = np.fft.fft(sample[i])
        FT = np.fft.fftshift(FT)
        PSD = PSD + (abs(FT)**2)/(T*n)

    PSD = PSD/(len(sample))

    return PSD, freqs

def Calculate_total_average_power(Processe):
    Time_Vector = Processe[0]
    sample = Processe[1:]
    x2 = np.zeros(len(sample))
    dt = Time_Vector[1] - Time_Vector[0]

    for i in range(len(sample)):
        x2[i] = ((sample[i]) ** 2).sum() * dt

    T = Time_Vector[-1] - Time_Vector[0]

    TAVP = np.round(x2.sum() / (len(x2) * T), 3)
    return TAVP


