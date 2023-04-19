# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FPunXW78FCTFGIxPyMsIbOoJYE25DXIs
"""

import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import math
import numpy as np

# Load data
data = "2023-04-16 08_48_02stile.csv"
expected_columns = 11

lines = []

# Open the CSV file and read each line
with open(data) as f:
    for i, line in enumerate(f):
        # Skip the first row (header)
        if i == 0:
            continue
        # Split the line into fields
        fields = line.strip().split(',')
        # Check if the line has the expected number of fields
        if len(fields) == expected_columns:
            # Append the line to the list of valid lines
            lines.append(fields)
        elif len(fields) > expected_columns:
            # If there are too many fields, take the first n fields and skip the rest
            lines.append(fields[:expected_columns])
        else:
            # If there are too few fields, skip the line
            continue

data = pd.DataFrame(lines, columns=['time', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'mag_x', 'mag_y', 'mag_z', 'pressure'])
# data = data.loc[data.apply(lambda row: len(row.str.split(','))) == expected_columns]
data.columns = ['time', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'mag_x', 'mag_y', 'mag_z', 'pressure']

# Convert data types
for column in data.columns[1:]:
    data[column] = pd.to_numeric(data[column])

# Calculate the net acceleration
data['acc_net'] = [math.sqrt(acc_z**2 + acc_x**2 + acc_y**2) for acc_x, acc_y, acc_z in zip(data['accel_x'], data['accel_y'], data['accel_z'])]

print(data['accel_x'].values)

# Calculate the average values
acc_x_avg = data['accel_x'].mean()
acc_y_avg = data['accel_y'].mean()
acc_z_avg = data['accel_z'].mean()
gyro_x_avg = data['gyro_x'].mean()
gyro_y_avg = data['gyro_y'].mean()
gyro_z_avg = data['gyro_z'].mean()

# Print the results
print(f"Average Accelerometer X: {acc_x_avg}")
print(f"Average Accelerometer Y: {acc_y_avg}")
print(f"Average Accelerometer Z: {acc_z_avg}")
print(f"Average Gyroscope X: {gyro_x_avg}")
print(f"Average Gyroscope Y: {gyro_y_avg}")
print(f"Average Gyroscope Z: {gyro_z_avg}")

# Set up 3D plot
fig = plt.figure()
ax = plt.axes(projection = '3d')

print(len(data))

# Plot accelerometer data
ax.plot3D(data['accel_x'].values, data['accel_y'].values, data['accel_z'].values, label='Accelerometer')

# Plot magnetometer data
ax.quiver(0, 0, 0, data['mag_x'].mean(), data['mag_y'].mean(), data['mag_z'].mean(), length=1, normalize=True, color='r', label='Magnetometer')
plt.show()

# Plot gyroscope data
ax = plt.axes(projection = '3d')
ax.plot3D(data['gyro_x'].values, data['gyro_y'].values, data['gyro_z'].values, label='Gyroscope')

# Set axis labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()