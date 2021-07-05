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

def SendBlockData(data):
    BUS.write_block_data(AirMotorsAddress, AirMotorsRegisterAddress, data)
   
def Stop:    
    BUS.write_byte_data(AirMotorsAddress, AirMotorsRegisterAddress, data)    
    BUS.write_byte_data(LandMotorsAddress, LandMotorsRegisterAddress, data)    










###################################################################################################################################################
BUS = 1  # I2C1 bus/channel which are GPIO pins 2 & 3

DEV_ADRS = 0x08      # device address
DEV_REG_ADRS = 0x02  # device register address

bus = smbus.SMBus(BUS)

# truncate to 8 bits
val = val & 0xff
# write 8 bits to slave
bus.write_byte_data(DEV_ADRS, DEV_REG_ADRS, val)

# reads 8 bits from slave
val_rec = bus.read_byte_data(DEV_ADRS, DEV_REG_ADRS, val)
###################################################################################################################################################
