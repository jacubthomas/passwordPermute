import hashlib

import os
# assign directory
directory = 'passwords'
files = []
# iterate over files inthat directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    # if os.path.isfile(f):
    #     print(f)
    files.append(f)

# get all hashes for teams 1 + 3 for comparison
all_hashes = []
with open('team1.txt') as file:
    lines = [line.strip() for line in file]
    all_hashes += lines
# with open('team2hashes.txt') as file:
#     lines = [line.strip() for line in file]
#     all_hashes += lines

# for x in files:
#     if x != 'passwords/checked' and x != 'passwords/.DS_Store':
#         with open(f'{x}') as f:
with open('passwords/ctf2430') as f:
    passwords = [line for line in f]
    print (len(all_hashes))
    print (len(passwords))
    for p in passwords:
        hashed = hashlib.md5(p.encode('utf-8')).hexdigest()
        if hashed in all_hashes:
            print (f"HIT! password: {p}, hash = {hashed}")
            break
