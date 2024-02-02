import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file")

args = parser.parse_args()
file_good = True
try:
    np_file = np.load(args.file)
except:
    file_good = False
    print(f"File error: {args.file}")

if file_good:
    with open("file_output", "w+") as out:
        for line in np_file:
            out.write(str(line))

