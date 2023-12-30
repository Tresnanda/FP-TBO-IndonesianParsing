from module.cnf import *

dict = run_conversion()

with open("module/cnf_test.txt", "w") as write_cnf:
    for i in dict:
        write_cnf.write(f"{i} -> {' | '.join(dict[i])}\n")