import serial
import json
from datetime import datetime

# Serial port configuration
SERIAL_PORT = "COM2"
BAUD_RATE = 9600
TIMEOUT = 1

def read_voltage_data_single():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
            print(f"Listening on {SERIAL_PORT}.")
            data = []
            start_time = None
            output_file = ""

            while True:
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        try:
                            line_objs = line.split(': ')
                            volts = line_objs[1]
                            voltage = float(volts)
                            now = datetime.now()

                            if start_time is None:
                                start_time = now
                                # Generate file name with datetime
                                timestamp_str = now.strftime('%Y-%m-%d_%H-%M-%S')
                                output_file = f"voltage_readings_{timestamp_str}.json"
                                print(f"First reading at {now.strftime('%Y-%m-%d %H:%M:%S')}")
                                print(f"Saving to: {output_file}")

                            elapsed = (now - start_time).total_seconds()

                            data_point = {
                                "time_elapsed": round(elapsed, 2),
                                "voltage": voltage,
                                "timestamp": now.strftime('%H:%M:%S')
                            }

                            data.append(data_point)
                            print(f"Read: {data_point}")

                        except ValueError:
                            print(f"Ignored invalid data: {line}")

                except serial.SerialException as e:
                    print(f"Serial error during read: {e}")
                    break

    except serial.SerialException as e:
        print(f"Failed to open serial port: {e}")
        return

    # Save data when disconnected
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {output_file}")
    else:
        print("No valid data to save.")


def read_voltage_data_multiple():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
            print(f"Listening on {SERIAL_PORT}.")
            data = []
            start_time = None
            output_file = ""

            while True:
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        try:
                            # format of text as I am not sure how this reads multiple print lines
                            # B1: x, B2: x
                            line_objs = line.split(', ')
                            # line_objs = ['B1: x', 'B2: x']
                            
                            vdiffs = []
                            for i in line_objs:
                                vdiff = i[-1]
                                vdiffs.append(float(vdiff))
                            now = datetime.now()

                            if start_time is None:
                                start_time = now
                                # Generate file name with datetime
                                timestamp_str = now.strftime('%Y-%m-%d_%H-%M-%S')
                                output_file = f"voltage_readings_{timestamp_str}.json"
                                print(f"First reading at {now.strftime('%Y-%m-%d %H:%M:%S')}")
                                print(f"Saving to: {output_file}")

                            elapsed = (now - start_time).total_seconds()

                            data_point = {
                                "time_elapsed": round(elapsed, 2),
                                "vdiff1": vdiffs[0],
                                "vdiff2": vdiffs[1],
                                "timestamp": now.strftime('%H:%M:%S')
                            }

                            data.append(data_point)
                            print(f"Read: {data_point}")

                        except ValueError:
                            print(f"Ignored invalid data: {line}")

                except serial.SerialException as e:
                    print(f"Serial error during read: {e}")
                    break

    except serial.SerialException as e:
        print(f"Failed to open serial port: {e}")
        return

    # Save data when disconnected
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {output_file}")
    else:
        print("No valid data to save.")

if __name__ == "__main__":
    read_voltage_data_single()
