number_lst = open("day1.in").read().splitlines()

for i in number_lst:
    first_number = number_lst.pop(0)
    for second_number in number_lst:
        if len(first_number) > 0 and len(second_number):
            result=int(first_number)+int(second_number)
        if result == 2020: print(first_number ,"*", second_number, "=", int(first_number)*int(second_number), "-->", int(first_number)+int(second_number))
