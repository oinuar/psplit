import re
import sys
import os

if len(sys.argv) < 3:
    print("Usage: {} [pattern to search] [number of required matches before split] [file]".format(sys.argv[0]))
    sys.exit(1)

pattern = re.compile(sys.argv[1])
split_every = int(sys.argv[2])
filename = sys.argv[3]

with open(filename, "r") as f:
    lines = []
    matches = 0
    counter = 0

    while True:
        line = f.readline()

        # If there is no line, stop.
        if not line:
            break
    
        # Count matches if they match to pattern.
        if pattern.match(line):
            matches += 1
    
        # Write all lines to file when match threshold is reached.
        if matches >= split_every:
            counter += 1
            split_filename = "{:04d}_{}".format(counter, os.path.basename(filename))

            with open(split_filename, "w") as ff:
                ff.writelines(lines)

            print("Split {} line(s) to file {}".format(len(lines), split_filename))
            
            lines = []
            matches = 0
    
        # Store all lines to buffer.
        lines.append(line)
