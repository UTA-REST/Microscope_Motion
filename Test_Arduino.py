import time
import serial


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


with serial.Serial('COM8',9800,timeout=1) as ser:
    Start_Arduino(0.3, 1)

    for i in range(5):
        print("NOW")
        Trigger(0.1, 0.5)
