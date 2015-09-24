#License
#-------
#This code is published and shared by Numato Systems Pvt Ltd under GNU LGPL 
#license with the hope that it may be useful. Read complete license at 
#http://www.gnu.org/licenses/lgpl.html or write to Free Software Foundation,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

#Simplicity and understandability is the primary philosophy followed while
#writing this code. Sometimes at the expence of standard coding practices and
#best practices. It is your responsibility to independantly assess and implement
#coding practices that will satisfy safety and security necessary for your final
#application.

#This demo code demonstrates how to write to a GPIO

import sys
import serial

if (len(sys.argv) < 2):
	print "Usage: gpiowrite.py <PORT> <GPIONUM> <COMMAND> \nEg: gpiowrite.py COM1 0 set"
	sys.exit(0)
else:
	portName = sys.argv[1];
	gpioNum = sys.argv[2];
	command = sys.argv[3];

#Open port for communication	
serPort = serial.Serial(portName, 19200, timeout=1)

#Send "gpio write" command. GPIO number 10 and beyond are
#referenced in the command by using alphabets starting A. For example
#GPIO10 willbe A, GPIO11 will be B and so on. Please note that this is
#not intended to be hexadecimal notation so the the alphabets can go 
#beyond F.

if (int(gpioNum) < 10):
    gpioIndex = str(gpioNum)
else:
    gpioIndex = chr(55 + int(gpioNum))

serPort.write("gpio "+ command +" "+ gpioIndex  + "\r")

print "Command sent..."
	
#Close the port
serPort.close()