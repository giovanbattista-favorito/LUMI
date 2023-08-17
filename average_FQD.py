import numpy as np
import time
import serial

#Select port
port = '/dev/cu.usbmodem101'
usb = serial.Serial(port)

t0 = time.time()
deltat = 0.
y_tot = 0.
x_tot = 0.
deltat_MAX = input("Time over which you want to average? ")
deltat_MAX = float(deltat_MAX)

counter = 0
while(deltat < deltat_MAX):
    counter += 1
    
    #Read data from Serial Monitor
    arduino = usb.readline().rstrip()
    line = arduino.decode()
    
    # Split the line into two values (assuming they are space-separated)
    x, y, SUM = line.split()

    # Convert the values to floats
    y = float(y)
    x = float(x)
    
    y_tot += y
    x_tot += x

    deltat = time.time() - t0

    #Wait e-6 seconds before doing it again
    #plt.pause(0.000001)
    
y_tot = y_tot/counter
x_tot = x_tot/counter
print("Y average over {} s: {}".format(deltat_MAX, y_tot))
print("X average over {} s: {}".format(deltat_MAX, x_tot))