import hashlib

file = open('team3.txt', 'r')
Lines = file.readlines()

hasheswithsalt = []

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

with open('passwords/ctf2430') as file:
    lines = [line.strip() for line in file]
    print (len(lines))
    for line in lines:
        for hs in hasheswithsalt:                
            frontsalted = hs[1] + line
            backsalted = line + hs[1]
            fronthashed = hashlib.md5(frontsalted.encode('utf-8')).hexdigest()
            backhashed = hashlib.md5(backsalted.encode('utf-8')).hexdigest()

            if fronthashed == hs[0]:
                print (f'FRONT HIT! password: {line}, hash {hs[0]}')
            elif backhashed == hs[0]:
                print (f'BACK HIT! password: {line}, hash {hs[0]}')
