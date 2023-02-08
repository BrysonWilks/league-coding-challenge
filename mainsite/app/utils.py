import csv
from typing import List
import numpy as np

def get_2D_array(filename: str) -> List[List[int]]:
    results = []
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                results.append(row)
        if np.shape != 2:
            print("WARNING! THIS PROGRAM EXPECTS A 2D ARRAY. RESULTS MAY VARY WITH OTHER INPUT")
    except IOError as e:
        print("UNABLE TO PARSE FILE")
        print(e)
    return results