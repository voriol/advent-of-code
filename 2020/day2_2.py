def splitword(word): 
    return [char for char in word]  

passwd_lst = open("day2.in").read().splitlines()

correct_passwd=0

for p in passwd_lst:
    min_char = int(p.split(":")[0].split("-")[0])
    max_char = int(p.split(":")[0].split("-")[1].split()[0])
    leter = p.split(":")[0].split("-")[1].split()[1]
    passwd = p.split(":")[1]

    num_passwd_lst = splitword(passwd)

    if (num_passwd_lst[min_char] == leter and num_passwd_lst[max_char] != leter) or (num_passwd_lst[min_char] != leter and num_passwd_lst[max_char] == leter):
        correct_passwd = correct_passwd +1
        print(p, num_passwd_lst)

print(correct_passwd)