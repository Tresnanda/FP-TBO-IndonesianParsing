from module.cnf import *
from tabulate import tabulate

# rule = run_conversion()

rule = {}
text = open('module/cnf_test.txt', 'r')
cnf = text.read().splitlines()

for i in range(len(cnf)):
    lhs = cnf[i].split(' -> ')[0]
    rhs = set(cnf[i].split(' -> ')[1].split(' | '))
    rule.update({lhs: list(rhs)})
    
def parse(string):
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
            print('i: ', i) # Penitng
            print("j: ", j) # Penting 
            print('hasil algoritma: ') # Penting
            for k in range(i, j):
                print("k: ", k) # Penting
                result = f"({i}, {k}): {table[i][k]} * ({k+1}, {j}): {table[k+1][j]}"
                print(f'{result}: ', end=" ") # Penting
                for lhs, rule in dict.items():
                    for rhs in rule:
                        if len(rhs.split()) == 2 and rhs.split()[0] in table[i][k] and rhs.split()[1] in table[k+1][j]:
                            table[i][j].add(lhs)
                            print(f"-> ({i}, {j}): '{rhs.split()[0]}', '{rhs.split()[1]}', non-terminal berada di: {lhs} ") # Penting
                            #print(f"{result} -> ({i}, {j}): non-terminal berada di: {lhs} ")
                print() # Penting
                print() # Penting
            print(tabulate(table, headers=[f"{idx}" for idx in range(n)], tablefmt="fancy_grid")) # Penting
            print('==-----------------------------------------------------------------') # Penting
            print() # Penting
            print() # Penting

    for i in range(0, n):
        table2[0][i] = table[i][i]

    for i in range(1, n):
        k = i
        for j in range(0, n-i):
            table2[i][j] = table[j][k]
            k = k+1
    table2 = table2[::-1]
    # print("table2: ")
    # print(tabulate(table2, headers=[f"{idx}" for idx in range(n)], tablefmt="fancy_grid"))
    
    #print(table[0][n-1])
    # if 'K' in table[0][n-1]:
    #     return table2
    # else:
    #     return None
    return table2