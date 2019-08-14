import time
import struct
import pigpio

pi=pigpio.pi()
ser = pi.serial_open("/dev/ttyAMA0",19200,0)
counterA=0
counterB=1

while 1:
    counterC=counterA + counterB
    if counterC >= 256*256:
        counterA=0
        counterB=1
        counterC = counterA + counterB

    lobyte = counterC & 0xFF
    hibyte = (counterC >>8) & 0xFF
    #hihibyte = (counterC & 0x00FF) >>16
    #pi.serial_write(ser,struct.pack("B",hihibyte))
    pi.serial_write(ser,struct.pack("B",hibyte))
    pi.serial_write(ser,struct.pack("B",lobyte))
    counterA=counterB
    counterB=counterC
    print(counterC)
    time.sleep(1)
                    
    
