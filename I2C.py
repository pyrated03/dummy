# sudo apt install i2ctools  , which contains i2cdetect
# sudo apt install smbus

import smbus
import time
import RPi.GPIO as GPIO

BUS = smbus.SMBus(1)    #I2C port number in Raspberry Pi is 1

AirMotorsAddress =                                #Random address(Address for air motor) 
AirMotorsRegisterAddress =                        #Random address)Register Address for air motor) 
LandMotorsAddress =                               #Address for land motor
LandMotorsRegisterAddress =                       #Register Address for land motor
#Read the data and get it in the variable "data"

l = len(data)
if data == 's':
    Stop()
elif l == 2:
    SendWordData(data)
elif l == 4:
    SendBlockData(data)
    
    
def SendWordData(data):
    BUS.write_word_data(LandMotorsAddress, LandMotorsRegisterAddress, data)

def SendWordData(data):
    BUS.write_block_data(AirMotorsAddress, AirMotorsRegisterAddress, data)
   
def Stop:    
    GPIO.cleanup()
