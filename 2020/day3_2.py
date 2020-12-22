def splitword(word): 
    return [char for char in word]  

def navigate(c, l):
    route = open("day3.in").read().splitlines()

    column=0
    line=0
    trees=0
    for path in route:
        new_path = splitword(path)

        if line % l == 0:
            if new_path[column] == '#': 
                trees = trees +1
                new_path[column] = 'X'

            if column +c > len(new_path) -1:
                column = column +c -len(new_path)
            else:
                column = column +c

        line = line +1

    return trees

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

print(navigate(1, 1)*navigate(3, 1)*navigate(5, 1)*navigate(7, 1)*navigate(1, 2))
