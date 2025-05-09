import serial
import popUpMsg

# Serial port configuration
SERIAL_PORT = "COM2"
BAUD_RATE = 9600
TIMEOUT = 1

def get_vdiff():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
        print(f"Listening on {SERIAL_PORT}.")
    
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        # Hardcoded values test
        # line = "B1: 1.2, B2: 0.03"

        if line:
            print(f'{line}\n')
            # format of text as I am not sure how this reads multiple print lines
            # B1: x, B2: x
            line_objs = line.split(', ')
            # line_objs = ['B1: x', 'B2: x']
            
            vdiffs = []
            for i in line_objs:
                vdiff = i[-1]
                vdiffs.append(float(vdiff))

            if vdiffs[0] > 1.00:
                root = popUpMsg.Tk()
                root.withdraw()
                popUpMsg.message("STRAIN ALERT", "Try this stretch to relax your muscles", "Images\muscle_stretches\Lumbrical.jpg")
                root.destroy()

            if vdiffs[1] > 1.00:  
                root = popUpMsg.Tk()
                root.withdraw()
                popUpMsg.message("STRAIN ALERT", "Try this stretch to relax your muscles", "Images\muscle_stretches\Thenar1.jpg")
                root.destroy()