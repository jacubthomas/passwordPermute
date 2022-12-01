symbols = ['!','@','#','$','%','^','&','*','(',')','?', '_', '-', '~', '()', '|', '+', '-', '<', '>', ',', '.', '/', '\\']
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
with open('password') as file:
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
                    temp1, temp2, temp3 = list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y] = '4', 'A', '@'
                    temp1, temp2, temp3 = ''.join(temp1), ''.join(temp2), ''.join(temp3)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
            if x[y].lower() == '@':
                    temp1, temp2, temp3, temp4, temp5, temp6= list(x), list(x), list(x), list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y], temp4[y], temp5[y], temp6[y] = '4', 'a', 'A', '8', 'AT', 'at'
                    temp1, temp2, temp3, temp4, temp5, temp6 = ''.join(temp1), ''.join(temp2), ''.join(temp3), ''.join(temp4), ''.join(temp5), ''.join(temp6)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
                    cracked.append(temp4)
                    cracked.append(temp5)
                    cracked.append(temp6)
            if x[y] == '!':
                    temp1, temp2, temp3 = list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y] = 'i', '1', 'I'
                    temp1, temp2, temp3 = ''.join(temp1), ''.join(temp2), ''.join(temp3)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
            if x[y].lower() == 'e':
                    temp = list(x)
                    temp[y] = '3'
                    temp = ''.join(temp)
                    cracked.append(temp)
            if x[y] == '3':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = 'e', 'E'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == 'i':
                    temp1, temp2 = list(x), list(x)
                    temp1[y], temp2[y] = '!', '1'
                    temp1, temp2, = ''.join(temp1), ''.join(temp2)
                    cracked.append(temp1)
                    cracked.append(temp2)
            if x[y].lower() == 's':
                    temp1, temp2, temp3, temp4= list(x), list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y], temp4[y] = '5', 's', 'S', '$'
                    temp1, temp2, temp3, temp4 = ''.join(temp1), ''.join(temp2), ''.join(temp3), ''.join(temp4)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
                    cracked.append(temp4)
            if x[y] == '$':
                    temp1, temp2, temp3 = list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y] = 's', 'S', '5'
                    temp1, temp2, temp3 = ''.join(temp1), ''.join(temp2), ''.join(temp3)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
            if x[y].lower() == 'j':
                    temp1, temp2, temp3, temp4= list(x), list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y], temp4[y] = 'l', 'L', '1', '|'
                    temp1, temp2, temp3, temp4 = ''.join(temp1), ''.join(temp2), ''.join(temp3), ''.join(temp4)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
                    cracked.append(temp4)
            if x[y].lower() == '|':
                    temp1, temp2, temp3, temp4= list(x), list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y], temp4[y] = '1', '!', 'l', 'L'
                    temp1, temp2, temp3, temp4 = ''.join(temp1), ''.join(temp2), ''.join(temp3), ''.join(temp4)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
                    cracked.append(temp4)
            if x[y] == '8':
                    temp1, temp2, temp3 = list(x), list(x), list(x)
                    temp1[y], temp2[y], temp3[y] = '@', 'at', 'AT'
                    temp1, temp2, temp3 = ''.join(temp1), ''.join(temp2), ''.join(temp3)
                    cracked.append(temp1)
                    cracked.append(temp2)
                    cracked.append(temp3)
            else:
                temp1, temp2 = list(x), list(x)
                temp1[y], temp2[y] = temp1[y].upper(), temp1[y].lower()
                temp1, temp2, = ''.join(temp1), ''.join(temp2)
                cracked.append(temp1)
                cracked.append(temp2)

def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing

allCases = []
for c in cracked:
        temp = [x for x in all_casings(c)]
        allCases += temp


for c in allCases:
    print (c)