import csv
from typing import List
import numpy as np

def get_2D_array(filename: str) -> List[List[int]]:
    results = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)

    if len(np.array(results).shape) != 2: # checking if results is 2D array
        print("WARNING: THIS PROGRAM EXPECTS A 2D ARRAY! ANYTHING ELSE MAY PRODUCE UNEXCEPTED RESULTS")

    return results