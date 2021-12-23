import math
from rigid_transform_3D import rigid_transform_3D
import numpy as np


def calcDistances(scanner: dict) -> dict:
    for point1 in scanner:
        for point2 in [point for point in scanner if point != point1]:
            a = point1[0] - point2[0]
            b = point1[1] - point2[1]
            c = point1[2] - point2[2]
            scanner[point1].add(math.sqrt((a * a) + (b * b) + (c * c)))


def normalizeScanners(scanners: list) -> list:
    transformed = [scanners.pop(0)]

    while scanners:
        for scanner in scanners:
            for main in transformed:
                calcDistances(main)
                calcDistances(scanner)
                overlap = {}

                # determine overlapping points
                for point1, distances1 in main.items():
                    for point2, distances2 in scanner.items():
                        if len(distances1.intersection(distances2)) > 1:
                            overlap[point1] = point2

                # if we have 12 overlapping points, find the transformation of the scanner
                if len(overlap) >= 12:
                    # determine rotation and offset
                    originals = np.array([list(point) for point in overlap.keys()]).transpose()
                    duplicate = np.array([list(point) for point in overlap.values()]).transpose()

                    rotation, translation = rigid_transform_3D(duplicate, originals)
                    translation = np.around(translation)
                    rotation = np.around(rotation)

                    # transform the scanner matrix and move it to the list of transformed scanners
                    scanner_matrix = np.array([list(point) for point in scanner.keys()]).transpose()
                    actual = (rotation @ scanner_matrix) + translation
                    actual = actual.transpose()
                    scanner_matrix = [(int(actual[i][0]), int(actual[i][1]), int(actual[i][2])) for i in range(len(actual))]

                    transformed.append({point: set() for point in scanner_matrix})
                    scanners.remove(scanner)
                    break;
    return transformed


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

scanners = []
scanner_index = -1

for line in lines:
    if 'scanner' in line:
        scanners.append({})
        scanner_index += 1
    elif line != '':
        vals = line.split(',')
        scanners[scanner_index][(int(vals[0]), int(vals[1]), int(vals[2]))] = set()

scanners = normalizeScanners(scanners)
points = set()

for scanner in scanners:
    points.update(scanner.keys())

print(len(points))
