import Functions

if __name__ == '__main__':

    # Generate Processes

    global FileName
    FileName = "D:\Self Development\Zewail collage material\Academic years\Year 3\Probability\Stochastic-Processes-Analyzer\Processes\Process_X.csv"
    Process_X = Functions.OpenFile(FileName)
    Functions.Plot_Process(Process_X, "X[t] Graph", "Time [t]", "X[t]")

    # Y(t) = βsin(2πt), where 0 ≤ t ≤ 2, β∼N(0, 1)
    Process_Y = Functions.GenerateProcess_Y()
    Functions.Plot_Process(Process_Y, "Y[t] Graph", "Time [t]", "Y[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_Y", Process_Y)

    # Z(t) = X(t) * Y(t)
    Process_Z = Functions.GenerateProcess_Z(Process_X, Process_Y)
    Functions.Plot_Process(Process_Z, "Z[t] Graph", "Time [t]", "Z[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_Z", Process_Z)

    # P(t) is a 10-bits Polar NRZ process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    Process_P = Functions.GenerateProcess_P(10, 5, 2)   # bits, A, Tb
    Functions.Plot_Process(Process_P, "P[t] Graph", "Time [t]", "P[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_P", Process_P)

    # M(t) is a 10-bits Manchester code process,
    # with A = 5 volts, Tb = 2 seconds, and initial time shift, α∼U(0, Tb)
    Process_M = Functions.GenerateProcess_M(10, 5, 2) # bits, A, Tb
    Functions.Plot_Process(Process_M, "M[t] Graph", "Time [t]", "M[t]")
    Functions.Save_Process(
        "D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Stochastic-Processes-Analyzer/Processes/",
        "Process_M", Process_M)


