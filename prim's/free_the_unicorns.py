import math
import csv
import sys

import numpy as np


# prim's algorithm
def prims(arr, vertices):
    INF = math.inf
    selected = [0 for _ in range(len(arr[0]))]
    no_edge = 0
    selected[0] = True
    output = []
    while no_edge < vertices - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if (not selected[j]) and arr[i][j]:
                        # not in selected and there is an edge
                        if minimum > arr[i][j]:
                            minimum = arr[i][j]
                            x = i
                            y = j
        output.append(str(x + 1) + "-" + str(y + 1) if x < y else str(y + 1) + "-" + str(x + 1))  # reset offset
        selected[y] = True
        no_edge += 1
    return output


# read Excel file into array
def readFile(filename):
    with open(filename, 'r') as readData:
        readCsv = csv.reader(readData)
        data = list(readCsv)
        data = np.array(data, dtype=int)
    return data


# read Excel file into array without library
with open('12.csv', 'r') as f:
    results = []
    for line in f:
        words = line.split(',')
        if words[len(words) - 1].__contains__("\n"):
            words[len(words) - 1] = words[len(words) - 1].replace("\n", "")
        results.append(words)
    print(results)
