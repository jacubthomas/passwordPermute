import hashlib
import os
directory = 'passwords'
hasheswithsalt = []
files = []
# iterate over files inthat directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    # if os.path.isfile(f):
    #     print(f)
    files.append(f)

file = open('team3.txt', 'r')
Lines = file.readlines()
for line in Lines:
    temp_list = line.replace('"', '').strip().split(',')
    user = temp_list[0].strip()
    hash = temp_list[1].strip()
    salt = temp_list[2].strip()
    hasheswithsalt.append((hash, salt, user))

file2 = open('team5.txt', 'r')
Lines2 = file2.readlines()
for line in Lines2:
    temp_list = line.replace('"', '').strip().split(',')
    user = temp_list[0].strip()
    hash = temp_list[1].strip()
    salt = temp_list[2].strip()
    hasheswithsalt.append((hash, salt, user))

# with open('passwords/qwert') as file:
for x in files:
    if x != 'passwords/checked' and x != 'passwords/.DS_Store':
        with open(f'{x}') as f:
            print (f)
            lines = [line.strip() for line in f]
            print (len(lines))
            for line in lines:
                for hs in hasheswithsalt:                
                    frontsalted = hs[1] + line
                    backsalted = line + hs[1]
                    fronthashed = hashlib.md5(frontsalted.rstrip().encode()).hexdigest()
                    backhashed = hashlib.md5(backsalted.rstrip().encode()).hexdigest()

                    if fronthashed == hs[0].strip():
                        print (f'FRONT HIT! password: {line}, hash {hs[0]}')
                    elif backhashed == hs[0].strip():
                        print (f'BACK HIT! password: {line}, hash {hs[0]}')
