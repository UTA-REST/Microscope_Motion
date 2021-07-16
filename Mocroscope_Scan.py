
import time
import serial
from random import uniform
import numpy as np

from pipython import GCSDevice
from pipython import pitools

T_start = time.time()
def Make_Position(START, END, STEP):
    Vals = []
    OUT  = True
    N=0
    while OUT:
        curr = START + STEP*N 
        N += 1
        Vals.append(round(curr,9))
        if curr > END:
            OUT=False
    return Vals

def Start_Arduino(High_Time, Low_Time):
    ser.write(b"H")
    time.sleep(High_Time)
    ser.write(b"L")
    time.sleep(Low_Time)

def Trigger(High_Time, Low_Time):
    ser.write(b"H")
    time.sleep(High_Time)
    ser.write(b"L")
    time.sleep(Low_Time)


X_vals = Make_Position(-4, 1.7, 0.4)
Y_vals = Make_Position(-1.6, 3, 0.4)

All_Positions = np.array(np.meshgrid(X_vals,Y_vals)).T.reshape(-1,2)




xstart = 1
ystart = 1
Zstart = 3.404

dist = 1
dx = 0.000
dy = 0.01
step = 0.05

XX = np.arange(xstart,xstart+dist+0.01,step=step)
YY = np.arange(ystart,ystart+dist+0.01,step=step)

All_Positions = []
for Y in range(0,len(YY)):
    Yval = round(YY[Y],9)
    XX = np.flip(XX, axis=0)
    for X in range(0,len(XX)):
        Xval = round(XX[X],9)
        
        Zval = Zstart + (Xval-xstart)*dx + (Yval-ystart)*dy
        Zval = round(Zval,9)
        
        All_Positions.append([Xval,Yval,Zval])
All_Positions = np.array(All_Positions)


Arduino_Port = "COM8"
Baud = 9600



Controller = 'E-873'
with GCSDevice(Controller) as X_Axis, GCSDevice(Controller) as Y_Axis, GCSDevice(Controller) as Z_Axis, serial.Serial(Arduino_Port,Baud,timeout=1) as ser:

    print("Starting to initilize the system.")
    Start_Arduino(0.3, 1)
    print("Connected to the Arduino!")
    print("___________________________________ \n")

    print("Loading the X axis")
    X_Axis.ConnectUSB(serialnum='120002968')
    #pitools.startup(X_Axis, stages='X_Q-545.140', refmode="FNL")
    pitools.startup(X_Axis, stages='X_Q-545.140', refmode="FNL")
    X_Axis.MOV(X_Axis.axes, 0.0)
    print("X axis loaded and on target!")
    print("___________________________________ \n")

    print("Loading the Y axis")
    Y_Axis.ConnectUSB(serialnum='120003784')
    pitools.startup(Y_Axis, stages='Y_Q-545.140', refmode="FNL")
    Y_Axis.MOV(Y_Axis.axes, 0.0)
    print("Y axis loaded and on target!")
    print("___________________________________ \n")

    print("Loading the Z axis")
    Z_Axis.ConnectUSB(serialnum='120002962')
    pitools.startup(Z_Axis, stages='Z_Q-545.140', refmode="FNL")
    #Z_Axis.MOV(Z_Axis.axes, -5.0)
    print("Z axis loaded and on target!")
    print("___________________________________ \n")

    print("Starting the scan.")

    Z_Axis.MOV(Z_Axis.axes, 3.0)
    pitools.waitontarget(Z_Axis)
    for i in range(0,len(All_Positions)):
        X_Pos = All_Positions[i][0]
        Y_Pos = All_Positions[i][1]
        Z_Pos = All_Positions[i][2]

        #Z_Axis.MOV(Z_Axis.axes, uniform(-6,6))
        #Y_Axis.MOV(Y_Axis.axes, uniform(-6,6))
        #X_Axis.MOV(X_Axis.axes, uniform(-6,6))

        Y_Axis.MOV(Y_Axis.axes, Y_Pos)
        X_Axis.MOV(X_Axis.axes, X_Pos)
        Z_Axis.MOV(Z_Axis.axes, Z_Pos)

        pitools.waitontarget(X_Axis)
        pitools.waitontarget(Y_Axis)
        pitools.waitontarget(Z_Axis)
        
        time.sleep(0.5) # setteling time

        Trigger(0.1, 0.5)

    

    print("Program loop has finished, moving morors to origin.")
    time.sleep(0.5)
    Z_Axis.MOV(Z_Axis.axes, -5.0)
    pitools.waitontarget(Z_Axis)
    Y_Axis.MOV(Y_Axis.axes, 0.0)
    X_Axis.MOV(X_Axis.axes, 0.0)
    pitools.waitontarget(X_Axis)
    pitools.waitontarget(Y_Axis)
    print("Motors reset.")

    print("Closing connnection.")

T_end = time.time()
print("The scan took "+str(T_end-T_start))

