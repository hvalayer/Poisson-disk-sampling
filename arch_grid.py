# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:57:22 2023

@author: hugov
"""

import numpy as np
from scipy import interpolate


# =============================================================================
# Class Point
# =============================================================================

class Point:

    # Attributes: coordinates x and y, radius r
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    # Check if the point overlaps another (sum of radius >= distance of centers)
    def overlap(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dist = np.sqrt(dx**2 + dy**2)
        return self.r + other.r >= dist

# =============================================================================
# Class Cell
# =============================================================================

class Cell:

    # Attributes: store points within the cell
    def __init__(self):
        self.nb_points = 0
        self.list_points = []

    # Return the list of points
    def get_pts(self):
        return self.list_points

    # Append method: add a new point to the current list of points
    def append(self, point):
        self.list_points.append(point)
        self.nb_points += 1

# =============================================================================
# Class Grid
# =============================================================================

class Grid:
    
    # Attributes: store a matrix of cells (grid of size NxN)
    def __init__(self, N, pi, K=0.05):
        # Number of cells along one axis of the grid
        self.nb_cell = N
        # Nested list: NxN matrix of cell objects
        self.list_cell = [[Cell() for _ in range(self.nb_cell)] for _ in range(self.nb_cell)]
        # Cells virtual width
        self.width = 1./(np.ceil((np.min(pi))/K))
        # Interpolate the given density over a [0,1]x[0,1] domain
        x = np.arange(0, self.nb_cell, 1)
        y = np.arange(0, self.nb_cell, 1)
        self.density = interpolate.interp2d(x, y, pi, kind='linear')
        self.K = K

    # Return the coordinates of a cell within the grid given a point
    def access(self, point):
        x, y = point.x, point.y
        i = int(x/self.width)
        j = int(y/self.width)
        return i,j

    # Return list of points from neighboring cells of the current point
    def get_pts_adj(self, pt):
        i,j = self.access(pt)
        last = self.nb_cell-1
        cellsAdj = []
        ptAdj = []
        cellsAdj.append(self.list_cell[i][j])
        if i != last:
            cellsAdj.append(self.list_cell[i + 1][j])
            if j != 0:
                cellsAdj.append(self.list_cell[i + 1][j - 1])
            if j != last:
                cellsAdj.append(self.list_cell[i + 1][j + 1])
        if i != 0:
            cellsAdj.append(self.list_cell[i - 1][j])
            if j != 0:
                cellsAdj.append(self.list_cell[i - 1][j - 1])
            if j != last:
                cellsAdj.append(self.list_cell[i - 1][j + 1])
        if j != 0:
            cellsAdj.append(self.list_cell[i][j - 1])
        if j != last:
            cellsAdj.append(self.list_cell[i][j + 1])
        for cell in cellsAdj:
            for point in cell.list_points:
                ptAdj.append(point)
        return ptAdj
    
    # Draw a new point and add it to the current grid if it's valid
    def new_point(self):
        # initialize boolean stopping condition to False
        did_break = False
        # draw a random pair of coordinates between 0 and 1 (uniform distribution)
        x,y = np.random.uniform(0,1), np.random.uniform(0,1)
        # create a new point in a cell with radius K/density of the cell
        x_grid = x*self.nb_cell
        y_grid = y*self.nb_cell
        p = Point(x, y, self.K / self.density(x_grid,y_grid))
        # get the list of points from neighboring cells
        ptAdj = self.get_pts_adj(p)
        # loop over adjacent points
        for point in ptAdj:
            # check if the new point overlaps with one of the list
            if p.overlap(point) :
                did_break = True
                break
        # if not, append the point to its corresponding cell
        if not(did_break):
            i,j = self.access(p)
            cell = self.list_cell[i][j]
            cell.append(p)
        return did_break, p
