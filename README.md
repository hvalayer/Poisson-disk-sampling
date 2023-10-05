# Poisson disk sampling for image processing

3rd year project in Applied Mathematics at INSA Toulouse, France

*Authors:*
- Gabriel Depaillat & Hugo Valayer, INSA Toulouse, France

*Project advisor:*
- Alban Gossard, Institut de Mathématiques de Toulouse, France

## About the project
The aim of this project is to create a stippled (or dotted) version of an original image, using the Poisson disk sampling based on a density map over a grid.

## How to use the project
The distribution of files is as follows:
 * <ins>arch_grid.py:</ins> contains the implementation of the grid structure used to perform the sampling
 * <ins>main.py:</ins> main file for applying the sampling to a given image, along with some displays

## Example
Original grayscale image
[!image](https://github.com/hvalayer/Poisson-disk-sampling/blob/master/images/gray_img.png)
Derived density map
[!density map](https://github.com/hvalayer/Poisson-disk-sampling/blob/master/images/density_map.png)
Final result with 200 000 points
[!result_200k](https://github.com/hvalayer/Poisson-disk-sampling/blob/master/images/result_200k.png)
Final result with 500 000 points
[!result_500k](https://github.com/hvalayer/Poisson-disk-sampling/blob/master/images/result_500k.png)