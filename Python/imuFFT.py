# Python script that we wrote to process accelerometer data
# We want to detect human motion (<=5Hz) for 30 seconds using FFT

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from collections import deque
import serial
# import time

# UART signal config
port = 'COM2'
baudRate = 115200 # match IMU baud rate
sampleRate = 100 # 100 Hz

# FFT parameters
sampleRate = 100      # Hz (100 samples/sec)
sizeFFT = 128         # Samples per FFT (1.28s of data)
freqTarget = 5        # Hz (human motion)
timeThreshold = 30    # seconds (total monitoring time) (this can change to a more realistic time, like 20 mins or 1200 sec)
freqRes = sampleRate / sizeFFT  # 0.78 Hz

# helper function to analyze data with an FFT to detect repetitive motion
def detectMotion(dataBuf, sampleRate, freqTarget, sizeFFT, multiplier=5):
        # Compute FFT
    fft_result = np.abs(fft(dataBuf))[:sizeFFT//2]
    freqs = np.linspace(0, sampleRate/2, sizeFFT//2)
    
    # Check target frequency bin
    freqRes = sampleRate / sizeFFT
    target_bin = int(freqTarget / freqRes)
    noise_floor = np.mean(fft_result[:10])  # Low-frequency noise baseline
    threshold = multiplier * noise_floor
    
    if fft_result[target_bin > threshold]:
        return True
    else:
        return False

# function to continuously read data from a serial port
def main():
    # initializing serial port
    ser = serial.Serial(port, baudRate, timeout=1)

    # initisilizing data bufs to track for 30s 
    dataBuf = deque(maxlen=sizeFFT)
    chunks = deque(maxlen=int(timeThreshold * sampleRate / sizeFFT))
    try:
        print(f"Reading from {port}... (Ctrl+C to stop)")
        while True:
            # Read serial data (adjust parsing for your IMU's format)
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    # get accel data from serial port
                    # calculate acceleroation magnitude and add it to databuf
                    x, y, z = map(float, line.split(','))
                    accel_magnitude = np.sqrt(x**2 + y**2 + z**2)  # Combine axes
                    dataBuf.append(accel_magnitude)
                    
                    # Process when buffer is full
                    if len(dataBuf) == sizeFFT:
                        # call the FFT function
                        motion = detectMotion(dataBuf, sampleRate, freqTarget, sizeFFT)

                        chunks.append(1 if motion else 0)
                        if sum(chunks) == len(chunks):
                            print("WARNING! TAKE A BREAK!")
                            # ***NOTE: call warning pop-up here?

                        
                except ValueError:
                    print("error parsing data!!")

    except KeyboardInterrupt:
        ser.close()
        print("Serial connection closed.")

if __name__ == "__main__":
    main()


# ***NOTE: the followign code is to statically simulate data, but we want to mimic a more
# real-world environment (reading data from a port)
# def get_accelerometer_data():
#     t = np.linspace(0, timeThreshold, int(sampleRate * timeThreshold))

#     # ***NOTE: this is not REAL data,
#     # this is simluation 5Hz motion + noise
#     motion_signal = 0.5 * np.sin(2 * np.pi * freqTarget * t)
#     noise = 0.1 * np.random.randn(len(t))
#     return motion_signal + noise  # Replace with actual 3-axis data

# init imu data
# data = get_accelerometer_data()
# num_chunks = int(len(data) / sizeFFT)
# detected_motion = np.zeros(num_chunks)

# # processing data in chunks
# for i in range(num_chunks):
#     chunk = data[i*sizeFFT : (i+1)*sizeFFT]
    
#     # Apply FFT
#     fft_result = np.abs(fft(chunk))[:sizeFFT//2]  # Take magnitude + discard mirror
#     freqs = np.linspace(0, sampleRate/2, sizeFFT//2)
    
#     # checking for for 5Hz peak
#     # (within ±0.78Hz resolution)
#     target_bin = int(freqTarget / freqRes)

#     # distinguishing between motion + noise
#     threshold = 5 * np.mean(fft_result[:10])
#     if fft_result[target_bin] > threshold:
#         detected_motion[i] = 1

# # verifying if 30s of continuous motion has passed
# motion_timeThreshold = np.sum(detected_motion) * (sizeFFT / sampleRate)
# print(f"5Hz motion detected for {motion_timeThreshold:.1f}s")

# # Plot (for debugging)
# plt.figure()
# plt.plot(freqs, fft_result, label='FFT')
# plt.axvline(freqTarget, color='r', linestyle='--', label='5Hz')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()