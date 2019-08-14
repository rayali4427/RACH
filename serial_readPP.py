import time
import pigpio

pi=pigpio.pi()
ser = pi.serial_open("/dev/ttyAMA0",19200,0)

while 1:
    (b, x) = pi.serial_read(ser,3)
    if b >0:
        print(int.from_bytes(x, byteorder='big'))
                    
    
