import serial
from flask import Flask, request

robot = serial.Serial('/dev/ttyUSB0', 9600)

def checkSerialConnection():
    verified = False
    print('waiting for serial port')
    while verified is False:
        if robot.in_waiting > 0:
            print('serial port connected')
            return True
        else:
            print('error')
            return False


app = Flask(__name__)

@app.route('/', methods=['GET'])
def tallyho():
    #Check that the API is running...
    return 'tallyho'

@app.route('/checkserial', methods=['GET'])
def checkserial():
    #Verify that we can talk to the robot...
    if checkSerialConnection():
        return 'connected'
    else:
        return 'error'

@app.route('/move', methods=['POST'])
def move():
    #Move robot in direction `dir`...
    direction = request.args.get('direction')
    valid = ('forward', 'back')

    if checkSerialConnection():
        if request.method == 'POST':
            if direction in valid:
                robot.write(str.encode(direction))
                return 'moving {0}'.format(direction)
            else:
                return 'invalid direction argument, expected {0} got {1}'.format(valid, direction)
        else:
            return 'invalid request method, expected "POST" got {0}'.format(request.method)
    else:
        return 'serial connection error'


@app.route('/pivot', methods=['POST'])
def pivot():
    #Turn robot in direction `dir`...
    direction = request.args.get('direction')
    valid = ('left', 'right')

    if checkSerialConnection():
        if request.method == 'POST':
            if direction in valid:
                robot.write(str.encode(direction))
                return 'pivoting {0}'.format(direction)
            else:
                return 'invalid direction argument, expected {0} got {1}'.format(valid, direction)
        else:
            return 'invalid request method, expected "POST" got {0}'.format(request.method)
    else:
        return 'serial connection error'

@app.route('/halt', methods=['POST'])
def halt():
    #Halt the robot...
    if checkSerialConnection():
        if request.method == 'POST':
            robot.write(str.encode('halt'))
            return 'halting'
        else:
            return 'invalid request method, expected "POST" got {0}'.format(request.method)
    else: return 'serial connection error'

