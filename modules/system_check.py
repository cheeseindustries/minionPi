import serial
from time import sleep

robot = serial.Serial('/dev/ttyUSB0', 9600)
connected = False

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
    connection.write('forward')
    sleep(2)
    print("Halting...")
    connection.write('halt')
    sleep(2)
    print("Trying reverse motion...")
    connection.write('back')
    sleep(2)
    print("Halting...")
    connection.write('halt')
    sleep(2)
    print("Trying left rotate...")
    connection.write('left')
    sleep(2)
    print("Halting...")
    connection.write('halt')
    sleep(2)
    print("Trying right rotate...")
    connection.write('right')
    sleep(2)
    print("Halting...")
    connection.write('halt')

check_commands(robot)

robot.close()
