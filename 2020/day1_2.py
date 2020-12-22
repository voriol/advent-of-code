number_lst = open("day1.in").read().splitlines()

for i in number_lst:
    first_number = number_lst.pop(0)
    new_number_lst = number_lst.copy()
    for j in new_number_lst:
        second_number = new_number_lst.pop(0)
        for thirth_number in new_number_lst:
            if len(first_number) > 0 and len(second_number) and len(thirth_number) > 0:
                result=int(first_number)+int(second_number)+int(thirth_number)
            if result == 2020: print(int(first_number)+int(second_number)+int(thirth_number), "--", int(first_number)*int(second_number)*int(thirth_number))
