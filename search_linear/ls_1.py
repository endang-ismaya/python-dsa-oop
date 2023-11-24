def linear_search(item, my_list):
    i = 0
    found = False

    while i < len(my_list) and found is False:
        if my_list[i] == item:
            found = True

        else:
            i = i + 1

    return found


test1 = [6, 5, 8, 2, 3, 45, 87, 24, 70]
print(linear_search(87, test1))  # True
print(linear_search(88, test1))  # False
