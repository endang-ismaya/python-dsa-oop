class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        """Create a new Node"""
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print all the list"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        """Get Node Value by index"""
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def append(self, value):
        """
        Create New Node
        Add Node to End
        """
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        """Remove Node at the End"""
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        """Remove the first of the Node"""
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def prepend(self, value):
        """
        Create New Node
        Add Node to the Beginning
        """
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def insert(self, index, value):
        """
        Create New Node
        Insert Node
        """
