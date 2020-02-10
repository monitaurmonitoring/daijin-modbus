#!/usr/bin/env python
#from serial import Serial
import serial
from ctypes import *

def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

def int_convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_int))
    return fp.contents.value         # dereference the pointer, get the float

global daijin_distance1
daijin_distance1 = 0
global daijin_distance2
daijin_distance2 = 0
global daijin_level1
daijin_level1 = 0
global daijin_level2
daijin_level2 = 0

ser = serial.Serial('/dev/ttyUSB0', 4800, timeout=1)
# print (ser.name)

def poll_level():
    packet = bytearray()
    packet.append(0x01)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x65)
    packet.append(0xcb)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw level return from the instrument is: ", s)
    data_extract = s[6:14]
    ser.close
    print ("The extracted level data is: ", data_extract)
    print ("The converted level float is: ", convert(data_extract))
    print ("The int converted level float is: ", int_convert(data_extract))
    global daijin_level1
    daijin_level1 = convert(data_extract)

def poll_level2():
    packet = bytearray()
    packet.append(0x01)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x34)
    packet.append(0x0b)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw level2 return from the instrument is: ", s)
    data_extract = s[6:14]
    global daijin_level2
    daijin_level2 = int_convert(data_extract)
    print ("The extracted level2 data is: ", data_extract)
    print ("The converted level2 float is: ", convert(data_extract))
    print ("The int converted level2 float is: ", int_convert(data_extract))
    ser.close

def poll_distance():
    packet = bytearray()
    packet.append(0x01)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0xC4)
    packet.append(0x0b)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw distance return from the instrument is: ", s)
    data_extract = s[6:14]
    global daijin_distance1
    daijin_distance1 = int_convert(data_extract)
    print ("The extracted distance data is: ", data_extract)
    print ("The converted distance float is: ", convert(data_extract))
    print ("The int converted distance float is: ", int_convert(data_extract))
    ser.close

def poll_distance2():
    packet = bytearray()
    packet.append(0x01)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x01)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x95)
    packet.append(0xcb)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    global daijin_distance2
    daijin_distance2 = int_convert(data_extract)
    print ("The raw distance2 return from the instrument is: ", s)
    data_extract = s[6:14]
    print ("The extracted distance2 data is: ", data_extract)
    print ("The converted distance2 float is: ", convert(data_extract))
    print ("The int converted distance2 float is: ", int_convert(data_extract))
    ser.close

try:
  poll_distance()
except:
  print ("Distance1 errored out")
  daijin_distance1 = -1
try:
  poll_distance2()
except:
  print ("Distance2 errored out")
  daijin_distance2 = -1
try:
  poll_level()
except:
  daijin_level1 = -1
  print ("Level1 errored out")
try:
  poll_level2()
except:
  daijin_level2 = -1
  print ("Level2 errored out")

data1 = {"distance1":daijin_distance1,"distance2":daijin_distance2,"level1":daijin_level1,"level2":daijin_level2}
print (data1)
