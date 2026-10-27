
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        
    
    def insertion_sort(self):
        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next

            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head

                while (search.next is not None and
                       search.next.data < current.data):
                    search = search.next

                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head
        

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next

        tail = tail.next

    if current1 is not None:
        tail.next = current1
    else:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next

    return merged_list



# Проверка
linked_list = LinkedList()

for number in [10, 20, 30, 40]:
    linked_list.append(number)

print("Початковий список:")
linked_list.print_list()

linked_list.reverse()

print("Реверсований список:")
linked_list.print_list()


print("\nПеревірка сортування:")

unsorted_list = LinkedList()

for number in [40, 10, 30, 20, 5]:
    unsorted_list.append(number)

print("До сортування:")
unsorted_list.print_list()

unsorted_list.insertion_sort()

print("Після сортування:")
unsorted_list.print_list()


print("\nПеревірка об'єднання списків:")

list1 = LinkedList()
list2 = LinkedList()

for number in [1, 3, 5]:
    list1.append(number)

for number in [2, 4, 6]:
    list2.append(number)

print("Перший список:")
list1.print_list()

print("Другий список:")
list2.print_list()

merged = merge_sorted_lists(list1, list2)

print("Об'єднаний відсортований список:")
merged.print_list()
