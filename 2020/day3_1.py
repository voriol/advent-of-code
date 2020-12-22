def splitword(word): 
    return [char for char in word]  

route = open("day3.in").read().splitlines()

column=0
trees=0
for path in route:
    new_path = splitword(path)

    if new_path[column] == '#': 
        trees = trees +1
        new_path[column] = 'X'
    
    print(new_path, column, len(new_path))

    if column +3 > len(new_path) -1:
        column = column +3 -len(new_path)
    else:
        column = column +3

print(trees)
