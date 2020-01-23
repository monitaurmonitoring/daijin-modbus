#!/usr/bin/env python
import serial
from ctypes import *

def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

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
    print ("The extracted level data is: ", data_extract)
    print ("The converted level float is: ", convert(data_extract))
    ser.close

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
    print ("The extracted level2 data is: ", data_extract)
    print ("The converted level2 float is: ", convert(data_extract))
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
    print ("The extracted distance data is: ", data_extract)
    print ("The converted distance float is: ", convert(data_extract))
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
    print ("The raw distance2 return from the instrument is: ", s)
    data_extract = s[6:14]
    print ("The extracted distance2 data is: ", data_extract)
    print ("The converted distance2 float is: ", convert(data_extract))
    ser.close

poll_distance()
poll_distance2()
poll_level()
poll_level2()
