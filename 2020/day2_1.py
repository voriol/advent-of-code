def splitword(word): 
    return [char for char in word]  

passwd_lst = open("day2.in").read().splitlines()

correct_passwd=0

for p in passwd_lst:
    min_char = int(p.split(":")[0].split("-")[0])
    max_char = int(p.split(":")[0].split("-")[1].split()[0])
    leter = p.split(":")[0].split("-")[1].split()[1]
    passwd = p.split(":")[1]

    passwd_lst = splitword(passwd)
    passwd_lst.pop(0)

    num_of_leters = 0
    passwd_lst_copy = passwd_lst.copy()
    for i in passwd_lst_copy:
        charr = passwd_lst.pop(0)
        if charr == leter: num_of_leters = num_of_leters +1

    if num_of_leters >= min_char and num_of_leters <= max_char: 
        correct_passwd = correct_passwd +1
        print(p, num_of_leters)

print(correct_passwd)