import argparse
import numpy as np
from os import listdir

parser = argparse.ArgumentParser()
parser.add_argument("path")

args = parser.parse_args()
file_good = True
files = listdir(args.path)
print(files)
for file in files:
    try:
        np_file = np.load(f"{args.path}/{file}")
    except:
        file_good = False
        print(f"File error: {args.path}")
    if file_good:
        np_temp = np_file[:,:,0].copy()
        np_file[:,:,0] = np_file[:,:,1].copy()
        np_file[:,:,1] = np_temp.copy()

        np.save(f"{args.path}/{file}", np_file, allow_pickle=False)

    # if file_good:
    #     with open("file_output", "w+") as out:
    #         for line in np_file:
    #             out.write(str(line))
