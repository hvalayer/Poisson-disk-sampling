# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:57:22 2023

@author: hugov
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
from arch_grid import Grid

#%% Load test image + pre-processing

# Open the image and convert to gray scale
img = Image.open("test_img.png").convert("L")

# Resize the image if needed (must be a square picture!)
N = 500
if img.width != img.height:
    print("Image resized to %ix%i" %(N,N))
    img = img.resize((N, N))

# Store the image as a Numpy array
img = np.array(img, dtype=float)

# Flip the image so that the original axes match with Numpy array indexes
img = img[-1::-1,:]

# Display the image
plt.figure(figsize=(9.7,8))
plt.pcolormesh(img, cmap='gray')
plt.title("Image")
plt.colorbar()
plt.axis('equal')
plt.show()

# "Reverse" the image to obtain the density map
density_map = np.max(img) - img

# Apply minimum threshold to avoid zero density areas
density_map = np.clip(density_map, 10, None)

# Display the density map
plt.figure(figsize=(9.7,8))
plt.pcolormesh(density_map, cmap='gray')
plt.title("Density map")
plt.colorbar()
plt.axis('equal')
plt.show()

#%% Perform stippling using Poisson Disks on a grid with a density map

start = time.time()

# Initialize vectors of points coordinates (x,y)
px_saved = []
py_saved = []

# Build a grid of same size as the density map
size = density_map.shape[0]
grid = Grid(size, density_map)

# Define constant
cons_failures = 0
points_found  = 0
max_nb_cfails = 3000
max_nb_points = 200000

# Loop while max nb of points and max nb of consecutives failures is not reached
while points_found < max_nb_points and cons_failures < max_nb_cfails:

    # Draw a new random point accros the grid
    did_break, p = grid.new_point()
    
    # If the point is non-valid (overlapping another), count a failure and skip
    if did_break:
        cons_failures += 1
        
    # Else, the point is valid and is stored. We reset the nb of cons. failures
    else:
        cons_failures = 0
        points_found += 1
        px_saved.append(p.x)
        py_saved.append(p.y)
        
        # Print some info on the computation progression
        interval = int(max_nb_points / 10)
        if points_found % interval == 0:
            intermediate_time = time.time() - start
            formated_time = time.strftime("%H:%M:%S", time.gmtime(intermediate_time))
            progress = 100*points_found/max_nb_points
            print("Computation Time: %s | Completion: %2.2f %%" %(formated_time, progress))

#%% Post-Processing

# Display the ouput "image"
plt.figure(figsize=(8,8))
plt.scatter(px_saved, py_saved, s=0.01, c="k", marker=".")
plt.xlim([0,1])
plt.ylim([0,1])
plt.axis("off")
plt.show()

# Same but along with the original image
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
for ax in axes:
    ax.set_aspect('equal')
axes[0].pcolormesh(img, cmap='gray')
axes[0].axis("off")
axes[1].scatter(px_saved, py_saved, s=0.01, c="k", marker=".")
axes[1].axis("off")
plt.tight_layout()
