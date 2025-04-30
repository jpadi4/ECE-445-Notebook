import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("mock_imu_press_data.csv")
df2 = pd.read_csv("/Users/rawniesingh/Downloads/mock_imu_press_data_2.csv")

# Create the figure and subplots (2 rows, 1 column)
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# plot az1
axs[0, 0].plot(df["time_ms"], df["az"], label="az (Z-Accel)", color="blue")
axs[0, 0].axhline(9.81, color='gray', linestyle='--', label="Gravity baseline")
axs[0, 0].set_title("Simulated Z-Axis Acceleration (az)\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise")
axs[0, 0].set_xlabel("Time (ms)")
axs[0, 0].set_ylabel("Acceleration (m/s²)")
axs[0, 0].legend()
axs[0, 0].grid(True)

# plot az2
axs[0, 1].plot(df2["time_ms"], df2["az"], label="az (Z-Accel)", color="blue")
axs[0, 1].axhline(9.81, color='gray', linestyle='--', label="Gravity baseline")
axs[0, 1].set_title("Simulated Z-Axis Acceleration (az)\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise")
axs[0, 1].set_xlabel("Time (ms)")
axs[0, 1].set_ylabel("Acceleration (m/s²)")
axs[0, 1].legend()
axs[0, 1].grid(True)

# plot gyroscope data
axs[1, 0].plot(df["time_ms"], df["gx"], label="gx")
axs[1, 0].plot(df["time_ms"], df["gy"], label="gy")
axs[1, 0].plot(df["time_ms"], df["gz"], label="gz")
axs[1, 0].set_title("Simulated Gyroscope Data\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise", fontsize=12)
axs[1, 0].set_xlabel("Time (ms)")
axs[1, 0].set_ylabel("Angular Velocity (°/s or rad/s)")
axs[1, 0].legend()
axs[1, 0].grid(True)

# plot gyroscope data
axs[1, 1].plot(df2["time_ms"], df2["gx"], label="gx")
axs[1, 1].plot(df2["time_ms"], df2["gy"], label="gy")
axs[1, 1].plot(df2["time_ms"], df2["gz"], label="gz")
axs[1, 1].set_title("Simulated Gyroscope Data\nEvent 1: lift wrist up\nEvent 2: rotate wrist clockwise", fontsize=12)
axs[1, 1].set_xlabel("Time (ms)")
axs[1, 1].set_ylabel("Angular Velocity (°/s or rad/s)")
axs[1, 1].legend()
axs[1, 1].grid(True)


plt.tight_layout()
plt.show()

