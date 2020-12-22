def get_bags(bag, b_list):
    current_bag_lst = []
    for b in b_list:
        if bag in b.split('contain')[1]: 
            current_bag_lst.append(b.split(' bags')[0])
    return current_bag_lst

bags_lst = open("day7.in").read().splitlines()
shiny_lst = get_bags("shiny gold", bags_lst)

len_shiny_lst = 0
while True:
    for bag in shiny_lst:
        shiny_lst = shiny_lst +get_bags(bag, bags_lst)
        shiny_lst = list(dict.fromkeys(shiny_lst))

    if len_shiny_lst == len(shiny_lst): break
    else: len_shiny_lst = len(shiny_lst)

print(len(shiny_lst), shiny_lst)
