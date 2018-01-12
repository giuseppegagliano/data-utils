import pandas as pd
import numpy as np
import math
import os

input = sys.argv[0]
train_perc = .7
output_test = input.replace(".csv", "_test.csv")
output_train = input.replace(".csv", "_train.csv")

# Load & split data 
txt = pd.read_csv(input, sep=',', iterator=True, chunksize=10000)
data = pd.concat(txt, ignore_index=True)
train_size = math.floor(data.shape[0] * train_perc)
test, train = data[:train_size], data[train_size:]

# Write to file
test.to_csv(output_test, sep=',', index=False)
train.to_csv(output_train, sep=',', index=False)

print("Done!")