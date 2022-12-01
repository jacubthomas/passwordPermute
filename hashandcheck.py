import hashlib
import os


# assign directory
directory = 'passwords'
files = []
# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    files.append(f)

# get all hashes for teams 1
all_hashes = []
with open('team1.txt') as file:
    lines = [line.strip() for line in file]
    all_hashes += lines
usernames = []
with open('usernames') as file2:
    user = [line.strip() for line in file2]
    usernames += user

'''
TEAM 2 IS COMMENTED OUT, BECAUSE TEAM 1 ACTUALLY SALTS, BUT THIS WAS NOT OBVIOUS.
TO USE TEAM 2, USE NON-SALTED HASH SECTION OF CODE.
'''
# get all hashes for teams 2
# with open('team2.txt') as file:
#     lines = [line.strip() for line in file]
#     all_hashes += lines

# for x in all_hashes:
#     print (x)

''' 
CHANGED THIS SLIGHTLY LATE IN THE GAME.
IT USED TO, AND STILL CAN WITH A SMALL TWEAK, GENERATE STRAIGHT MD5 HASHES FROM THE PASSWORDS IN
EACH FILE. I FOUND OUT THAT TEAM 1 WAS IN FACT SALTING WITH RESPECTIVE USERNAMES, SO THIS ALSO
SALTS PRIOR TO HASHING. IF YOU WANT NO SALT HASHES, COMMENT THIS OUT AND UNCOMMENT BELOW
'''
for x in files:
    if x != 'passwords/checked' and x != 'passwords/.DS_Store' and x != 'passwords/checkedbyhash':
        with open(f'{x}') as f:
            print(f)
            passwords = [line for line in f]
            print (len(all_hashes))
            print (len(passwords))
            for p in passwords:
                p = p.strip()
                for u in usernames:
                    u = u.strip()
                    str = p+u
                    hashed = hashlib.md5(str.encode('ascii')).hexdigest()
                    if hashed in all_hashes:
                        print (f"HIT! password: {p}, hash = {hashed}")

'''NON-SALTED HASHES'''
# for x in files:
#     if x != 'passwords/checked' and x != 'passwords/.DS_Store' and x != 'passwords/checkedbyhash':
#         with open(f'{x}') as f:
#             passwords = [line for line in f]
#             print (len(all_hashes))
#             print (len(passwords))
#             for p in passwords:
#                 p = p.strip()
#                 hashed = hashlib.md5(p.encode('ascii')).hexdigest()
#                 if hashed in all_hashes:
#                     print (f"HIT! password: {p}, hash = {hashed}")