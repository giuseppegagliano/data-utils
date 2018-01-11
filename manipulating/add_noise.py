import numpy as np
import math
from shutil import copyfile
import csv
import os

input = sys.argv[0]
output = sys.argv[0].replace(".csv","_noise5.csv")
num_cols = 0
num_lines = -1
with open(input, 'r') as f:
    for line in f:
        if num_lines == -1:
            num_cols = len(line.split(sep=','))
        num_lines += 1
if os.path.isfile(output): os.remove(output)
copyfile(input, output)
with open(output, 'a') as f:
    writer = csv.writer(f, delimiter=",")
    for i in range(1, math.floor(num_lines*.05)):
        row = np.random.randint(0,9,size=(num_cols))
        writer.writerow(row)
print("Done.")