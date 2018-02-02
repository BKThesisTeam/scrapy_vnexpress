import csv
import random

with open('output.csv','r') as in_file, open('transcript_shuffle.csv','w') as out_file:
    data = in_file.readlines()
    header, rest = data[0], data[1:]
    random.shuffle(rest)

    fieldnames = ['id', 'description']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)

    # reorder the header first
    writer.writeheader()

    counter = 0
    seen = set() # set for fast O(1) amortized lookup
    for line in rest:
        if line in seen: continue # skip duplicate

        counter += 1
        seen.add(line)
        out_file.write(str(counter) + "," + line )
