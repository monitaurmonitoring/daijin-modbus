#!/usr/bin/env python
#from serial import Serial
import serial
import codecs
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

# Open serial connection
serial_connected = 1
try:
  ser_device = '/dev/ttyUSB0'
  ser = serial.Serial(ser_device, 9600, timeout=1)
except:
  serial_connected = 0
  print ('/dev/ttyUSB0 did not work, trying /dev/ttyUSB1')
if serial_connected == 0:
  try:
    ser_device = '/dev/ttyUSB1'
    ser = serial.Serial(ser_device, 9600, timeout=1)
  except:
    print ('serial did not work')
    raise

def poll_distance():
    packet = bytearray()
    packet.append(0x02)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0xC4)
    packet.append(0x38)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw distance return from the instrument is: ", s)
    print ("The extracted return from the instrument is: ", s[16:34])
    #data_extract = s[6:12]
    data_extract = s[22:30]
    b1_data_extract = s[22:26]
    b2_data_extract = s[26:30]
    bi_data_extract = s[26:30] + s[22:26]
    global daijin_distance1
    daijin_distance1 = int_convert(data_extract)
    print ("The extracted distance data is: ", data_extract)
    print ("The converted distance float is: ", convert(data_extract))
    print ("The int converted distance data is: ", int_convert(data_extract))
    print ("The extracted level bi_data is: ", bi_data_extract)
    print ("The bigendian converted level data is: ", convert(bi_data_extract))
    print ("The int converted level bi_data is: ", int_convert(bi_data_extract))
    print ("The data byte1 is: ", b1_data_extract)
    print ("The int converted level data byte1 is: ", int_convert(b1_data_extract))
    print ("The data byte2 is: ", b2_data_extract)
    print ("The int converted level data byte2 is: ", int_convert(b2_data_extract))
    ser.close

def poll_distance2():
    packet = bytearray()
    packet.append(0x02)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x01)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x95)
    packet.append(0xf8)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    global daijin_distance2
    #data_extract = s[6:12]
    data_extract = s[22:30]
    b1_data_extract = s[22:26]
    b2_data_extract = s[26:30]
    bi_data_extract = s[26:30] + s[22:26]
    daijin_distance2 = int_convert(data_extract)
    print ("The raw distance2 return from the instrument is: ", s)
    print ("The extracted return from the instrument is: ", s[16:34])
    print ("The extracted distance2 data is: ", data_extract)
    print ("The converted distance2 float is: ", convert(data_extract))
    print ("The int converted distance2 data is: ", int_convert(data_extract))
    print ("The extracted level bi_data is: ", bi_data_extract)
    print ("The bigendian converted level data is: ", convert(bi_data_extract))
    print ("The int converted level bi_data is: ", int_convert(bi_data_extract))
    print ("The data byte1 is: ", b1_data_extract)
    print ("The int converted level data byte1 is: ", int_convert(b1_data_extract))
    print ("The data byte2 is: ", b2_data_extract)
    print ("The int converted level data byte2 is: ", int_convert(b2_data_extract))
    ser.close

def poll_level():
    packet = bytearray()
    packet.append(0x02)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x65)
    packet.append(0xf8)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw level return from the instrument is: ", s)
    print ("The extracted return from the instrument is: ", s[16:34])
    data_extract = s[22:30]
    b1_data_extract = s[22:26]
    b2_data_extract = s[26:30]
    bi_data_extract = s[26:30] + s[22:26]
    ser.close
    print ("The extracted level data is: ", data_extract)
    print ("The converted level data is: ", convert(data_extract))
    print ("The int converted level data is: ", int_convert(data_extract))
    print ("The extracted level bi_data is: ", bi_data_extract)
    print ("The bigendian converted level data is: ", convert(bi_data_extract))
    print ("The int converted level bi_data is: ", int_convert(bi_data_extract))
    print ("The data byte1 is: ", b1_data_extract)
    print ("The int converted level data byte1 is: ", int_convert(b1_data_extract))
    print ("The data byte2 is: ", b2_data_extract)
    print ("The int converted level data byte2 is: ", int_convert(b2_data_extract))
    global daijin_level1
    daijin_level1 = convert(data_extract)

def poll_level2():
    packet = bytearray()
    packet.append(0x02)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x02)
    packet.append(0x34)
    packet.append(0x38)
    print ("Sending packet: ", packet.hex())
    ser.write(packet)
    s = ser.read(100).hex()
    print ("The raw level2 return from the instrument is: ", s)
    print ("The extracted return from the instrument is: ", s[16:34])
    #data_extract = s[6:12]
    data_extract = s[22:30]
    b1_data_extract = s[22:26]
    b2_data_extract = s[26:30]
    bi_data_extract = s[26:30] + s[22:26]
    ser.close
    global daijin_level2
    daijin_level2 = int_convert(data_extract)
    print ("The extracted level2 data is: ", data_extract)
    print ("The converted level2 float is: ", convert(data_extract))
    print ("The int converted level2 data is: ", int_convert(data_extract))
    print ("The extracted level bi_data is: ", bi_data_extract)
    print ("The bigendian converted level data is: ", convert(bi_data_extract))
    print ("The int converted level bi_data is: ", int_convert(bi_data_extract))
    print ("The data byte1 is: ", b1_data_extract)
    print ("The int converted level data byte1 is: ", int_convert(b1_data_extract))
    print ("The data byte2 is: ", b2_data_extract)
    print ("The int converted level data byte2 is: ", int_convert(b2_data_extract))

print ('--------------------------------------------------')
try:
  poll_distance()
except:
  print ("Distance1 errored out")
  daijin_distance1 = -1
print ('--------------------------------------------------')
try:
  poll_distance2()
except:
  print ("Distance2 errored out")
  daijin_distance2 = -1
print ('--------------------------------------------------')
try:
  poll_level()
except:
  daijin_level1 = -1
  print ("Level1 errored out")
print ('--------------------------------------------------')
try:
  poll_level2()
except:
  daijin_level2 = -1
  print ("Level2 errored out")

data1 = {"distance1":daijin_distance1,"distance2":daijin_distance2,"level1":daijin_level1,"level2":daijin_level2}
print (data1)
