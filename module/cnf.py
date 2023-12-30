dic = {}
start_symbol = 'K'

text = open('module/cfg_text.txt', 'r')
cfg = text.read().splitlines()

# baca rule cfg
for i in range(len(cfg)):
    lhs = cfg[i].split(' -> ')[0]
    rhs = set(cfg[i].split(' -> ')[1].split(' | '))
    dic.update({lhs: list(rhs)})


var_ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
new_rs = []
new_ls = []


# jika lhs terdapat pada rhs, maka hapus lhs, tambahkan rhs dari lhs yang telah di hapus ke rhs (misal S -> A B, dan B -> C D maka setelah kode ini akan menjadi S -> A C D)
def ekstensi():
  key = list(dic.keys())  
  for i in key:  
    for j in key:
      if i in dic[j]:  
        dic[j].remove(i)  
        dic[j].extend(dic[i]) 


# cari non terminal yang berjumlah dua, lalu diubah menjadi max 2
def ubah_cnf():
  #print(f'K: {dic[start_symbol]}')
  while rule_max_length() > 2:
    keys = list(dic.keys())
    for lhs in keys:
        for j in dic[lhs]:  
            if len(j.split(' ')) <= 2: ### jika sudah dalam bentuk cnf 
                continue #abaikan
            else:
                remove_non_terminal(lhs, j) 
    #print(f'K: {dic[start_symbol]}')


# fungsi buat ubah non terminal di atas dua jadi maks dua
def remove_non_terminal(pin, check_non_term):
  lst_check_val = check_non_term.split(' ')  
  temp = ''
  index = get_subs_index(new_rs, check_non_term)
  if index == -1: #-1 artinya ini lhs baru
    add_val = ' '.join(lst_check_val[0:2]) 
    new_ls.append(var_ls[len(new_ls)]) 
    new_rs.append(add_val) 
    temp = check_non_term.replace(add_val, new_ls[len(new_ls) - 1]) 
    dic.update({new_ls[len(new_ls) - 1]: [add_val]}) 
  else: # artinya sudah pernah dibuat lhs dengan non terminalnya sama dengan yang dicek sekarang
    temp = check_non_term.replace(new_rs[index], new_ls[index]) 
  dic[pin][dic[pin].index(check_non_term)] = temp


# mencari panjang tertinggii di lhs
def rule_max_length():
  maks = 0  
  for j in dic:
      for i in dic[j]: 
        if len(i.split(' ')) > maks:  
          maks = len(i.split(' ')) 
      return maks


def get_subs_index(new_rs, check_non_term):
  for i in new_rs:
    if i in check_non_term:
      return new_rs.index(i)
  return -1


def run_conversion():

  ekstensi()
  ubah_cnf()

  return dic

dict = run_conversion()

# with open("module/cnf_new_test.txt", "w") as write_cnf:
#     for i in dict:
#         write_cnf.write(f"{i} -> {' | '.join(dict[i])}\n")