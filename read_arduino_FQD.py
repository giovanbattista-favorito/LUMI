import numpy as np
import matplotlib.pyplot as plt
import time
import serial

#Select port
port = '/dev/cu.usbmodem101'
usb = serial.Serial(port)

#Name of the file for intensity (insert from terminal)
#print("Name of the file containing the intensity values of the beam: ")
#file_name_intensity = input()

while(True):
    #Read data from Serial Monitor
    arduino = usb.readline().rstrip()
    line = arduino.decode()
    
    # Split the line into two values (assuming they are space-separated)
    x, y, SUM = line.split()

    # Convert the values to floats
    x = float(x)
    y = float(y)
    SUM = float(SUM)
    
    #Print intensity (SUM) on separate file
    #with open(file_name_intensity, "a") as intensity_file:
    #    intensity_file.write("{}\n".format(SUM))
    
    #Live plot of the values
    plt.title("Position Sensing Detector")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(-1., 1.)
    plt.ylim(-1., 1.)
    plt.grid()
    
    plt.plot(x, y, 'o', label = 'X = {} \n Y = {}'.format(x, y))
    plt.draw()
    plt.legend()

    #Wait e-6 seconds before doing it again
    plt.pause(0.000001)
    #Clear image
    plt.clf()