import sys
import os
# datafolder = "/Users/premkumargontrand/AITrainingMar2026/python/modules/"

#status code  0 means success and 1 means failure
if len(sys.argv) > 1:
    print("Directory path provided:", sys.argv[1])
else:
    print("Please provide a directory path as a command-line argument.")
    sys.exit(1)

datafolder = sys.argv[1]

for files in os.listdir(datafolder):
    if files.endswith('.csv'):
        print(files)

