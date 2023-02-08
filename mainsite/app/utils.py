import csv
from typing import List

def get_2D_array(filename: str) -> List[List[int]]:
    results = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    return results