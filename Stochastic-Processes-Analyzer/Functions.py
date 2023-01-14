import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt
import os.path
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
