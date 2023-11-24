def binary_search(item, my_list):
    found = False

    first = 0
    last = len(my_list) - 1

    while first <= last and found is False:
        midpoint = (first + last) // 2
        print(midpoint)

        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1

    return found


test1 = [6, 5, 8, 2, 3, 45, 87, 24, 70]
test1 = sorted(test1)
print(binary_search(87, test1))  # True
print(binary_search(88, test1))  # False
