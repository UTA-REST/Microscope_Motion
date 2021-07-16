from pipython import GCSDevice

from random import uniform

from pipython import pitools

"""Connect to a PIPython device."""
CONTROLLERNAME = 'E-873'
STAGES = ('Q-545.140',)  # connect stages to axes
REFMODE = ('None',)  # reference the connected stages
# We recommend to use GCSDevice as context manager with "with".
with GCSDevice() as pidevice:
    #pidevice.InterfaceSetupDlg(key='E-873') # this searches and lets you pick the motor
    pidevice.ConnectUSB(serialnum='120002962') # this just connects with that motor

    # Each PI controller supports the qIDN() command which returns an
    # identification string with a trailing line feed character which
    # we "strip" away.

    print('connected: {}'.format(pidevice.qIDN().strip()))

    # Show the version info which is helpful for PI support when there
    # are any issues.

    if pidevice.HasqVER():
        print('version info: {}'.format(pidevice.qVER().strip()))

    print('done - you may now continue with the simplemove.py example...')


    print('initialize connected stages...')
    pitools.startup(pidevice, stages=STAGES, refmode=None)

    # Now we query the allowed motion range of all connected stages.
    # GCS commands often return an (ordered) dictionary with axes/channels
    # as "keys" and the according values as "values".

    rangemin = list(pidevice.qTMN().values())
    rangemax = list(pidevice.qTMX().values())
    ranges = zip(rangemin, rangemax)

    print("Austin was here")
    print(rangemin)

    print("********************************")

    print(pidevice.getparam('0x94'))

    if pidevice.HasqSPA():
        #print('SPA info: {}'.format(pidevice.qSPA()))
        print(pidevice.qSPA(1,'0x94')[1]['0x94'])
    else:
        print("FUCK ME!!!")

    print("********************************")
    print("********************************")
    pidevice.SPA({1:{'0x94':900}})
    print(pidevice.qSPA(1,'0x94')[1]['0x94'])

    pidevice.SPA({1:{'0x95':0.4}})
    print(pidevice.qSPA(1,'0x95')[1]['0x95'])



    #print(pidevice.qSPA(items="notchfilter").values())
    #for a in pidevice.qSGP():
    #    print(a.values())
    #print(pidevice.qSPA("notchfilter"))


