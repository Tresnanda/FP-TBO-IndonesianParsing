from module.cyk import *
from tabulate import tabulate

text = open('module/accept.txt', 'r')
kalimat_accept = text.read().splitlines()

total_accept = 0
total_reject = 0

kalimat_valid = []
kalimat_nonvalid = []

for kalimat in kalimat_accept:
    table = parse(kalimat)
    if table is not None:
        if 'K' in table[0][0]:
            kalimat_valid.append(kalimat)
            #print(f'{kalimat} diterima')
            total_accept = total_accept + 1
        else:
            n = len(kalimat.split())
            kalimat_nonvalid.append(kalimat)
            #print(f'{kalimat} ditolak dengan table filling: ')
            # print(tabulate(table, headers=[f"{idx}" for idx in range(n)], tablefmt="fancy_grid"))
            # print()
            total_reject = total_reject + 1

print("Kalimat diterima: ")
for kalimat in kalimat_valid:
    print(f'{kalimat} Diterima')
print("------------------------------------------------------------------------------")
print("Kalimat ditolak: ")
for kalimat in kalimat_nonvalid:
    print(f'{kalimat} Ditolak')
print("Accept: ", total_accept)
print("Reject: ", total_reject)