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

![gray_img](https://github.com/hvalayer/Poisson-disk-sampling/assets/98541826/5c1de816-04f5-46da-a69b-385ca0e1db04)

Derived density map

![density_map](https://github.com/hvalayer/Poisson-disk-sampling/assets/98541826/598dabc3-2661-4ab4-8e15-8a58ef919821)

Final result with 200 000 points

![result_200k](https://github.com/hvalayer/Poisson-disk-sampling/assets/98541826/7afd2f93-9588-4ac7-a47c-46e33854b490)

Final result with 500 000 points

![result_500k](https://github.com/hvalayer/Poisson-disk-sampling/assets/98541826/68b51035-a3a1-424c-a8b5-8d7e8c35953d)
