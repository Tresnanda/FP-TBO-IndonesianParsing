from tabulate import tabulate
from module.cnf import *

rule = {}
text = open('module/cnf_test.txt', 'r')
cnf = text.read().splitlines()

for i in range(len(cnf)):
    lhs = cnf[i].split(' -> ')[0]
    rhs = set(cnf[i].split(' -> ')[1].split(' | '))
    rule.update({lhs: list(rhs)})

text = open('module/accept.txt', 'r')
kalimat_accept = text.read().splitlines()

total_accept = 0
total_reject = 0

kalimat_valid = []
kalimat_nonvalid = []

def parse2(string):
    n = len(string.split())
    table = [[set([]) for j in range(n)] for i in range(n)]
    table2 = [[set([]) for j in range(n)] for i in range(n)]

    string2 = string.split()
    for j in range(0, n):
        for lhs, rule in dict.items():
            for rhs in rule:
                if len(rhs.split()) == 1 and rhs.lower() == string2[j].lower():
                    table[j][j].add(lhs)

    for j in range(0, n):
        for i in range (j, -1, -1):
            for k in range(i, j):
                result = f"({i}, {k}): {table[i][k]} * ({k+1}, {j}): {table[k+1][j]}"
                for lhs, rule in dict.items():
                    for rhs in rule:
                        if len(rhs.split()) == 2 and rhs.split()[0] in table[i][k] and rhs.split()[1] in table[k+1][j]:
                            table[i][j].add(lhs)
    for i in range(0, n):
        table2[0][i] = table[i][i]

    for i in range(1, n):
        k = i
        for j in range(0, n-i):
            table2[i][j] = table[j][k]
            k = k+1
    table2 = table2[::-1]
    return table2

for kalimat in kalimat_accept:
    table = parse2(kalimat)
    if table is not None:
        if 'K' in table[0][0]: # kalo diaccept
            kalimat_valid.append(kalimat)
            #print(f'{kalimat} diterima')
            total_accept = total_accept + 1
        else: # kalo ditolak
            # n = len(kalimat.split())
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