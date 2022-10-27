import numpy as np


# Substrate values
substrate = []

# V0 values
v0 = []

# Calculate
slope, intercept = np.polyfit(np.reciprocal(substrate), np.reciprocal(v0), 1)
vmax = 1/intercept
km = slope * vmax

# Print Vmax and Km
print(f"Vmax: {vmax}")
print(f"Km: {km}")
