import csv
from typing import List

def get_2D_array(filename: str) -> List[List[int]]:
    results = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)  # change contents to floats
        for row in reader:  # each row is a list
            results.append(row)
    return results