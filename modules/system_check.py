import serial
from time import sleep

robot = serial.Serial('/dev/ttyUSB0', 9600)

def checkSerialConnectionReady(func):
    def wrapper(*args, **kwargs):
        verified = False
        print("Verifying serial port...")
        while verified is False:
            if robot.in_waiting > 0:
                verified = True
            else:
                verified = False
        print("Serial port connected...")
        func(*args, **kwargs)
    return wrapper

@checkSerialConnectionReady        
def check_commands(connection):
    print("Trying forward motion...")
    connection.write(str.encode('forward'))
    sleep(2)
    print("Halting...")
    connection.write(str.encode('halt'))
    sleep(2)
    print("Trying reverse motion...")
    connection.write(str.encode('back'))
    sleep(2)
    print("Halting...")
    connection.write(str.encode('halt'))
    sleep(2)
    print("Trying left rotate...")
    connection.write(str.encode('left'))
    sleep(2)
    print("Halting...")
    connection.write(str.encode('halt'))
    sleep(2)
    print("Trying right rotate...")
    connection.write(str.encode('right'))
    sleep(2)
    print("Halting...")
    connection.write(str.encode('halt'))

check_commands(robot)

robot.close()
