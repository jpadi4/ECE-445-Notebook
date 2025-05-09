import numpy as np
import pandas as pd

fs = 100  # Hz
duration = 2.0  # seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

ax = 0.02 * np.random.randn(len(t))
ay = 0.02 * np.random.randn(len(t))
az = 9.81 + 0.05 * np.random.randn(len(t))

for press_start in [0.4, 1.2]:
    idx_start = int(press_start * fs)
    idx_end = idx_start + 10
    az[idx_start:idx_end] += np.linspace(0, 5, 10)
    az[idx_end:idx_end+10] += np.linspace(5, 0, 10)

gx = 0.1 * np.random.randn(len(t))
gy = 0.1 * np.random.randn(len(t))
gz = 0.1 * np.random.randn(len(t))

for press_start in [0.4, 1.2]:
    idx_start = int(press_start * fs)
    idx_end = idx_start + 20
    gx[idx_start:idx_end] += np.linspace(0, 2, 20)
    gy[idx_start:idx_end] += np.linspace(0, 1, 20)
    gz[idx_start:idx_end] += np.linspace(0, 0.5, 20)

imu_data = pd.DataFrame({
    "time_ms": (t * 1000).astype(int),
    "ax": ax,
    "ay": ay,
    "az": az,
    "gx": gx,
    "gy": gy,
    "gz": gz
})

imu_data.to_csv("mock_imu_press_data.csv", index=False)
from google.colab import files
files.download("mock_imu_press_data.csv")

