
'''
multiple ways to run this file. comment one out and run.

1) using a preset phrase + preset num
2) using a preset phrase + permutations of sequential digits

in each approach, it generates all permutations of capitalization of the phrase
and adds in all combos of symbols and prints to output
'''

symbols = ['!','@','#','$','%','^','&','*','(',')','?', '_', '-']
digits = ['1','2','3','4','5','6','7','8','9','0']
letters = ['A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


''' approach 1 '''
phrase = 'CTF2'
num = '430'
allCases = [x for x in all_casings(phrase)]
midphrase = []
for x in allCases:
    for z in symbols:
        midphrase.append (x+z+num)
        midphrase.append (x+num+z)
        midphrase.append (x+num[:1]+z)
        midphrase.append (x+num[:2]+z)
        midphrase.append (x+num[1:]+z)
        midphrase.append (num+x+z)
        midphrase.append (num+z+x)
        midphrase.append (z+x+num)
        midphrase.append (z+num+x)
        midphrase.append (x+num+z+z)
        midphrase.append (x+num[:2]+z+z)
        midphrase.append (x+num[:len(num)-1]+z+z)
        midphrase.append (x+num+z+z)


for x in midphrase:
    print (x)

''' end approach 1 '''

''' approach 2 '''

# phrase = 'ctf2'

# def all_casings(input_string):
#     if not input_string:
#         yield ""
#     else:
#         first = input_string[:1]
#         if first.lower() == first.upper():
#             for sub_casing in all_casings(input_string[1:]):
#                 yield first + sub_casing
#         else:
#             for sub_casing in all_casings(input_string[1:]):
#                 yield first.lower() + sub_casing
#                 yield first.upper() + sub_casing

# allCases = [x for x in all_casings(phrase)]

# digit_groups = []
# for i in range(0, len(digits)):
#     temp = digits[:i]
#     digit_groups.append(''.join(temp))
# for i in range(0, len(digits)):
#     temp = digits[i:]
#     digit_groups.append(''.join(temp))

# midphrase = []
# for x in allCases:
#     for y in digit_groups:
#         for z in symbols:
#             midphrase.append (x+z+y)
#             midphrase.append (x+y+z)
#             midphrase.append (y+x+z)
#             midphrase.append (y+z+x)
#             midphrase.append (z+x+y)
#             midphrase.append (z+y+x)
#             midphrase.append (x+y+z+z)
#             midphrase.append (x+y+z+z)

# for x in midphrase:
#     print (x)

''' end approach 2 '''