import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def turnmotor(iDirection, iSeqPos=0):
    deg = 95
    aMotorPins = [32, 35, 31, 33]
    for pin in aMotorPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

    aSequence = [
        [1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]
    ]
            
    iNumSteps = len(aSequence)
    fWaitTime = 0.001
    
    iDeg = int(int(deg) * 11.377777777777)
    
    for step in range(0,iDeg):
        for iPin in range(0, 4):
            iRealPin = aMotorPins[iPin]
            if aSequence[iSeqPos][iPin] != 0:
                GPIO.output(iRealPin, True)
            else:
                GPIO.output(iRealPin, False)
     
        iSeqPos += iDirection
     
        if (iSeqPos >= iNumSteps):
            iSeqPos = 0
        if (iSeqPos < 0):
            iSeqPos = iNumSteps + iDirection
     
        # Time to wait between steps
        time.sleep(fWaitTime)

    for pin in aMotorPins:
        GPIO.output(pin, False)
    
    return iSeqPos #used motor is being turned to a position where it stops mid sequence