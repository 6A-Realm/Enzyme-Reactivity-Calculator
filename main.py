import numpy as np


# Substrate values
substrate = [
    1.0,
    2.0,
    5.0,
    10.0,
    20.0,
]

# V0 values
v0 = [
    0.70,
    1.20,
    2.00,
    2.50,
    2.80,
]

# Calculate
slope, intercept = np.polyfit(np.reciprocal(substrate), np.reciprocal(v0), 1)
vmax = 1/intercept
km = slope * vmax

# Print Vmax and Km
print(f"Vmax: {vmax}")
print(f"Km: {km}")
