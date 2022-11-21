symbols = ['!','@','#','$','%','^','&','*','(',')','?', '_', '-']
digits = ['1','2','3','4','5','6','7','8','9','0']
cracked = []


'''
generates a small subset of permutations by changing examining each password char by char
if it is a symbol, it generates permutations of the password with all symbols at that index.
if it is a digit, 0-9, ....
if it is letter, it tries cap and lowercase
for certain chars such as a, it tries 4 and @; for @, it tries a,4.

run this using
`python3 crackedsymbolreplacer.py > [outputfile]`
'''

# enter a single file
with open('achieved') as file:
    lines = [line.strip() for line in file]
    for x in lines:
        for y in range(0, len(x)):
            if x[y] in symbols:
                for z in symbols:
                    temp = list(x)
                    temp[y] = z
                    temp = ''.join(temp)
                    cracked.append(temp)
            if x[y] in digits:
                for z in digits:
                    temp = list(x)
                    temp[y] = z
                    temp = ''.join(temp)
                    cracked.append(temp)
            if x[y].lower() == 'a':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = '4', '@'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == '@':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = '4', 'a'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == '!':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = 'i', '1'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == 'e':
                    temp = list(x)
                    temp[y] = '3'
                    temp = ''.join(temp)
                    cracked.append(temp)
            if x[y].lower() == 'i':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = '!', '1'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == 's':
                    temp = list(x)
                    temp[y] = '$'
                    temp = ''.join(temp)
                    cracked.append(temp)
            else:
                temp1, temp2 = list(x), list(x)
                temp1[y], temp2[y] = temp1[y].upper(), temp1[y].lower()
                temp1, temp2, = ''.join(temp1), ''.join(temp2)
                cracked.append(temp1)
                cracked.append(temp2)

for c in cracked:
    print (c)