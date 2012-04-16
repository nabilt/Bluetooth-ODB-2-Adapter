# You need pyserial to work for this import http://pyserial.sourceforge.net/
# easy_install pyserial
import serial

# Open bluetooth serial port
# Make sure you pair to the device first using the passcode 1234
# and change "/dev/cu.linvor-DevB" to your serial port
ser = serial.Serial("/dev/cu.linvor-DevB", baudrate=38400, timeout=1, bytesize=8, parity='N', stopbits=1)

# Request the RPM
# See http://en.wikipedia.org/wiki/OBD-II_PIDs and ELM327DS.pdf in the doc directory
ser.write('01 0C\r') 

# Read 18 bytes because the STN1110 appears to echo the command we sent
d = ser.read(18)     
print "raw data returned: ",
print list(d)

# Find the response code (41) and our RPM code (0C)
# The RPM value appears after the response code as 2 hex values
rpm = d.split("41 0C")[1].strip()
rpm = rpm.replace(" ", "")

# Divide the RPM by 4 because the car returns 4*rpm
print "RPM: ", int(rpm, 16)/4

ser.close()

