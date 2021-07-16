from pipython import GCSDevice
from pipython import pitools
from random import uniform

Controller = 'E-873'

with GCSDevice(Controller) as X_Axis, GCSDevice(Controller) as Y_Axis, GCSDevice(Controller) as Z_Axis:

    Z_Axis.ConnectUSB(serialnum='120002962')
    pitools.startup(Z_Axis, stages='Z_Q-545.140', refmode="FNL")

    Y_Axis.ConnectUSB(serialnum='120003784')
    pitools.startup(Y_Axis, stages='Y_Q-545.140', refmode="FNL")

    X_Axis.ConnectUSB(serialnum='120002968')
    pitools.startup(X_Axis, stages='X_Q-545.140', refmode="FNL")

    for x in range(5):


        Z_Axis.MOV(Z_Axis.axes, uniform(-6,6))
        Y_Axis.MOV(Y_Axis.axes, uniform(-6,6))
        X_Axis.MOV(X_Axis.axes, uniform(-6,6))

        pitools.waitontarget(X_Axis)
        pitools.waitontarget(Y_Axis)
        pitools.waitontarget(Z_Axis)


