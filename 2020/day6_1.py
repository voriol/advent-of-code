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

group_counts = 0
for group in groups:
    split_group_lst = splitword(''.join(group))
    delete_duplicates_lst = list(dict.fromkeys(split_group_lst))

    group_counts = group_counts +len(delete_duplicates_lst)

print(group_counts)
