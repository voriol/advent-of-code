def splitword(word): 
    return [char for char in word]  

ticket_lst = open("day5.in").read().splitlines()

seat_id_list=[]
max_seat_id = 0
for ticket in ticket_lst:
    min_column = 0
    max_column = 7
    min_row = 0
    max_row = 127
    s_ticket = splitword(ticket)
    for s in s_ticket:
        if s == "F": max_row = (max_row + min_row) // 2
        elif s == "B": min_row = (max_row + min_row) // 2 + (max_row + min_row) % 2
        elif s == "L": max_column = (max_column + min_column) // 2
        elif s == "R": min_column = (max_column + min_column) // 2 + (max_column + min_column) % 2

    seat_id = max_row * 8 + max_column
    seat_id_list.append(seat_id)

    if seat_id > max_seat_id: max_seat_id = seat_id

seat_id_sorted = sorted(seat_id_list)

for i in range(len(seat_id_sorted)):
    if i == len(seat_id_sorted) -1: break
    if seat_id_sorted[i] +1 != seat_id_sorted[i +1]: 
        print(seat_id_sorted[i], seat_id_sorted[i+1])
        print("el teu seient es: ", seat_id_sorted[i] +1)

#print("max seat list: ", seat_id_sorted)
