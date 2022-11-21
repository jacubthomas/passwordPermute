import random
from itertools import permutations

cracked_passes = [
'DanielKang123!',
'CTF2!2022',
'HelloWorld1234!',
'P@sswordA123',
'TOMtom123!',
'TOMtom123!',
'QQQ111!!',
'3n(cH4nT5)',
'3JsY4f5X',
'!NETwrk111',
'h3Js8n',
'Hello123H*',
'IaCh13vednoTh1ngtodAy!~',
'passwordLOL699!',
'sH4q%GOAT34',
'Surf_life200!X',
'TomorrowNeverComes@007',
'PAssword-123',
'Ctf2Team2!2',
'AFkjk314picirc()',
'Qd3?5^3',
'VenkiTest@007',
'TTouchdown2020!',
'IwannaWin.19984',
'@Jwwl76O57^b',
'aBC@123456',
'CTF2430!',
'K@rtav1N0Jers3y',
'DimpleAvani@1998',
'RunningToBellevue12345$',
'JAb39B5fgtfWA*zROZak',
'54iO$(csH7',
'JiangyI1500!',
'qekBap$gybbi9$hyjdugAV45',
'Peterstark'
]

cracked_passes.sort(key=len)
for i in cracked_passes[19:20]:
    _permutations_ = [''.join(p) for p in permutations(i)]
    print (i)
    for x in _permutations_:
        print (x)