#!/bin/python3

import sys


def mainDiagonal(grid):
    diagonals = []
    ref = 19
    for i in range(0, len(grid[0])):
        tam = i + 1
        diagonal = []
        for j in range(0, tam):
            diagonal.append(grid[j][ref - (tam - 1) + j])
        diagonals.append(diagonal)
    for i in range(0, len(grid[0]) - 1):
        tam = i + 1
        diagonal = []
        for j in range(0, tam):
            diagonal.append(grid[ref - (tam - 1) + j][j])
        diagonals.append(diagonal)
    return diagonals


def secondaryDiagonal(grid):
    diagonals = []
    for i in range(0, len(grid[0])):
        tam = i + 1
        diagonal = []
        for j in range(0, tam):
            diagonal.append(grid[j][tam-1-j])
        diagonals.append(diagonal)
    ref = 19
    for i in range(0, len(grid[0]) - 1):
        tam = i + 1
        diagonal = []
        for j in range(0, tam):
            diagonal.append(grid[ref-(tam-1-j)][ref - j])
        diagonals.append(diagonal)
    return diagonals


def allDiagonals(grid):
    ArrayAllDiagonals = mainDiagonal(grid)
    ArraySecondaryDiagonals = secondaryDiagonal(grid)
    ArrayAllDiagonals.extend(ArraySecondaryDiagonals)
    return ArrayAllDiagonals


def allColumns(grid):
    arrayAllColumns = []
    numberOfColumns = len(grid[0])
    for columns in range(0, numberOfColumns):
        arrayColumns = []
        for lines in range(0, len(grid)):
            arrayColumns.append(grid[lines][columns])
        arrayAllColumns.append(arrayColumns)
    return arrayAllColumns


def generateSearchSpace(grid):
    searchSpace = grid.copy()
    columns = allColumns(grid)
    main_diagonal = mainDiagonal(grid)
    secondary_diagonal = secondaryDiagonal(grid)
    searchSpace.extend(columns)
    searchSpace.extend(main_diagonal)
    searchSpace.extend(secondary_diagonal)
    return searchSpace


def biggestProductSeries(number, k):
    numberString = number
    counterProduct = 0
    iCounter = 0
    pivot = iCounter
    product = 1
    maxProduct = 0
    for i in numberString:
        if (i == 0):
            counterProduct = 0
            product = 1
            iCounter = iCounter + 1
            continue
        if (counterProduct == 0):
            pivot = iCounter
        if (counterProduct < k):
            product = product * i
            counterProduct = counterProduct + 1
            if (counterProduct == k):
                if (product > maxProduct):
                    maxProduct = product
        else:
            product = product // numberString[pivot]
            product = product * i
            pivot = pivot + 1
            if (product > maxProduct):
                maxProduct = product
        iCounter = iCounter + 1
    return maxProduct


def LargestProductGrid(searchSpace):
    product = 0
    for space in searchSpace:
        if (len(space) >= 4):
            value = biggestProductSeries(space, 4)
            if (value > product):
                product = value
    return product


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

searchSpace = generateSearchSpace(grid)
result = LargestProductGrid(searchSpace)
print(result)
