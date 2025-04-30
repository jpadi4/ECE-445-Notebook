import matplotlib.pyplot as plt

df = pd.read_csv("mock_imu_press_data.csv")

#plot az
plt.plot(df["time_ms"], df["az"], label="az (Z-Accel)", color="blue")
plt.axhline(9.81, color='gray', linestyle='--', label="Gravity baseline")
plt.title("Simulated Z-Axis Acceleration (az)\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise")
plt.xlabel("Time (ms)")
plt.ylabel("Acceleration (m/s²)")
plt.legend()
plt.grid(True)
plt.show()

# Plot all three gyro axes
plt.figure(figsize=(12, 4))
plt.plot(df["time_ms"], df["gx"], label="gx")
plt.plot(df["time_ms"], df["gy"], label="gy")
plt.plot(df["time_ms"], df["gz"], label="gz")
plt.title("Simulated Gyroscope Data\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise")
plt.xlabel("Time (ms)")
plt.ylabel("Angular Velocity (°/s or rad/s)")
plt.legend()
plt.grid(True)
plt.show()
