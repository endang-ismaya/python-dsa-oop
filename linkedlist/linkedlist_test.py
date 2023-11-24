from linkedlist import LinkedList

my_linked_list = LinkedList(4)
my_linked_list.append(10)

my_linked_list.prepend(90)
my_linked_list.print_list()

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
print(my_linked_list.get(2).value)
