"""Module contains LinkedList and Node classes."""

class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A class to represent a linked list."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """Inserts a new node after the given prev_node."""
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """Deletes a node with the given key."""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """Searches for an element in the linked list."""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        """Prints the linked list."""
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def reverse(self):
        """Reverses the linked list."""
        prev = None
        cur = self.head
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def sort(self):
        """Sorts the linked list using insertion sort algorithm."""
        sorted_head = None
        cur = self.head

        while cur is not None:
            next_node = cur.next
            if sorted_head is None or sorted_head.data >= cur.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                sorted_cur = sorted_head
                while sorted_cur.next is not None and sorted_cur.next.data < cur.data:
                    sorted_cur = sorted_cur.next
                cur.next = sorted_cur.next
                sorted_cur.next = cur
            cur = next_node

        self.head = sorted_head

    def merge_sorted(self, other):
        """Merges two sorted linked lists."""
        dummy = Node()
        cur_tail = dummy

        cur_a = self.head
        cur_b = other.head

        while cur_a is not None and cur_b is not None:
            if cur_a.data <= cur_b.data:
                cur_tail.next = cur_a
                cur_a = cur_a.next
            else:
                cur_tail.next = cur_b
                cur_b = cur_b.next
            cur_tail = cur_tail.next

        if cur_a is not None:
            cur_tail.next = cur_a
        if cur_b is not None:
            cur_tail.next = cur_b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list
