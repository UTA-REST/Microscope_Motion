# Microscope_Motion

This is the code to controll the 3 PI motors that drive the HP microscope. 
These require the pipython libs that are in the python folder of the PI software package. 

the files quickstart and simple move are slightly modified version of their scripts. 

The Test scripts are for testing the functional groups. if you are going to trigger the camera with the arduino you will need to load the Py_arduino.ino on the arduino. This coe just lets the arduino take a serial command and make it a logic pulse. 

The scripts Microscope_Scan are what was used for testing tand development. It connects to all 3 mnotors and the arduino. there are functions which locate all focal positions on the sample and do a poor calabration for the focus, since you need to map all 3D points on the sample. 

