# ADD LABELED NOISE POINTS

import pandas as pd
import numpy as np
import math
import os

noise_label = -1
noise_perc = 5
noise_range = [-100, 100]
input = sys.argv[0]
#input = "pendigits_full_with_head.csv"
output = input.replace(".csv", "_noise" + str(noise_perc) + ".csv")

# Find input csv shape
txt = pd.read_csv(input, sep=',', iterator=True, chunksize=10000)
data = pd.concat(txt, ignore_index=True)
[num_rows, num_cols] = data.shape

# Add noise points to random position
noise_count = math.floor(num_rows * noise_perc / 100)
noise = np.random.uniform(low=noise_range[0], high=noise_range[1], size=(noise_count, num_cols))
noise[:, num_cols-1] = noise_label
df = pd.DataFrame(data=noise, columns=data.columns)
data = data.append(df)
data = data.sample(frac=1)

# Write to file
data.to_csv(output, sep=',', index=False)

print("Done!")