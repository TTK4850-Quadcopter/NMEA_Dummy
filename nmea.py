import socket
import serial
import time

serialdevice = "/dev/tty.usbserial-FTGYEXIC"

port =serial.Serial(port=serialdevice, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=5)

longitude = 0
latitude = 0

gga='$GPGGA,123519,4807.%03d,N,01131.%03d,E,1,08,0.9,545.4,M,46.9,M,,*47'% (latitude, longitude)

while 1:
    gga='$GPGGA,123519,4807.%03d,N,01131.%03d,E,1,08,0.9,545.4,M,46.9,M,,*47'% (latitude, longitude)
    print gga
    port.write(gga + '\r\n')
    latitude+=1
    longitude+=1
    time.sleep(1)

