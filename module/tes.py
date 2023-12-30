text = open('cfg.txt', 'r')
kok = text.read().splitlines()
oaw = {}

for i in range(len(kok)):
    lhs = kok[i].split(' -> ')[0]
    rhs = set(kok[i].split(' -> ')[1].split(' | '))
    oaw.update({lhs: list(rhs)})
key = list(oaw.keys())

# for i in key:
#     for j in key:
#         if i in oaw[j]:
#             oaw[j].remove(i)
#             oaw[j].extend(oaw[i])

for keys in oaw:
    print(f'{keys}: , {oaw[keys]}')

print()
print()

# for j in oaw['K']:
#       if len(j.split(' ')) <= 2:  
#         continue
#       else:
#         print('a: ', oaw['K'][oaw['K'].index(j)])
#         oaw['K'][oaw['K'].index(j)] = 'JAWA'

# for j in oaw['K']: 
#     print('b: ', oaw['K'][oaw['K'].index(j)])

print(oaw)
        
