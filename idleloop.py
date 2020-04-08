import time
from keypad import keypad
import runstepper
import readSavedImage

print("ready")
 

# Initialize
kp = keypad()

while True:
    # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    time.sleep(0.5)
    print("Looking for face")
    allowed = readSavedImage.readMain()

    if allowed == 1:
        print("Face recognized")
        runstepper.turnmotor(-1)
        print("locking in 5s")
        time.sleep(5)
        runstepper.turnmotor(1)
        print("locked")
    else:
        seq = []
        for i in range(4):
            digit = None
            while digit == None:
                digit = kp.getKey()
            seq.append(digit)
            time.sleep(0.4)
        print(seq)
        
        if seq == [1, 2, 3, 4]:
            print("Code accepted, opening door")
            runstepper.turnmotor(-1)
            print("locking in 5s")
            time.sleep(5)
            runstepper.turnmotor(1)
            print("locked")
        else:
            print("wrong code :(")
    

    