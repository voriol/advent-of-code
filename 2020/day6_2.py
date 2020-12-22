def splitword(word): 
    return [char for char in word]  

input_groups = open("day6.in").read().splitlines()

groups = []
p = []
for line in input_groups:
    if line != "":
        for kk in line.split(" "):
            p.append(kk)
    else:
        groups.append(p)
        p = []
groups.append(p)

general_count=0
for g in groups:
    join_g_lst = splitword(''.join(g))
    g_len = len(g)

    delete_duplicates_lst = list(dict.fromkeys(join_g_lst))

    for i in delete_duplicates_lst:
        if join_g_lst.count(i) ==g_len: general_count = general_count +1
        
print(general_count)
