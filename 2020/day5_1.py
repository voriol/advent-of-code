def splitword(word): 
    return [char for char in word]  

ticket_lst = open("day5.in").read().splitlines()

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
    if seat_id > max_seat_id: max_seat_id = seat_id

    print(ticket, "row: ", min_row, ":", max_row, " - column: ", min_column, ":", max_column, " -- seat_id: ", seat_id)

print("max seat ID: ", max_seat_id)
