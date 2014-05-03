##########################################
## Python module to read a Wii nunchuck ##
##                                      ##
## Written by Jason - @Boeeerb          ##
## v0.1 03/05/14 - jase@boeeerb.co.uk   ##
##########################################
##
## v0.1 03/05/14 - Initital release
##

from smbus import SMBus
import RPi.GPIO as rpi

bus = 0

class nunchuck:
  
  def __init__(self):
    if rpi.RPI_REVISION == 1:
      i2c_bus = 0
    elif rpi.RPI_REVISION == 2:
      i2c_bus = 1
    else:
      print "Unable to determine Raspberry Pi revision."
      exit
    self.bus = SMBus(i2c_bus)
    self.bus.write_byte_data(0x52, 0xF0, 0x55)
    
  def read(self):
    buf = self.bus.read_i2c_block_data(0x52, 0x00, 6)
    data = [0x00]*6

    for i in range(len(buf)):
      data[i] = buf[i]
    return data

  def raw(self):
    data = self.read()
    return data

  def joystick(self):
    data = self.read()
    return data[0],data[1]

  def accelerometer(self):
    data = self.read()
    return data[2],data[3],data[4]

  def button_c(self):
    data = self.read()
    butc = (data[5] & 0x02)
    if butc == 0:
      return True
    else:
      return False

  def button_z(self):
    data = self.read()
    butc = (data[5] & 0x01)
    if butc == 0:
      return True
    else:
      return False    


  def joystick_x(self):
    data = self.read()
    return data[0]

  def joystick_y(self):
    data = self.read()
    return data[1]

  def accelerometer_x(self):
    data = self.read()
    return data[2]

  def accelerometer_y(self):
    data = self.read()
    return data[3]
  
  def accelerometer_z(self):
    data = self.read()
    return data[4]

  
  def scale(self,value,_min,_max,_omin,_omax):
    return (value - _min) * (_omax - _omin) // (_max - _min) + _omin