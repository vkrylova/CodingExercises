class Node:
    def __init__(self, data):
        self.data = data  # Data field
        self.next_element = None  # Pointer to the next node


class SinglyLinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head_node = None  # Pointer to first node in the list

    def get_head(self):
        """Return the head of the linked list."""
        return self.head_node

    def insert_at_head(self, data):
        """
        Insert a node at the head of the linked list.

        Args:
            data: The value to be inserted.

        Returns:
            Node: The new head of the linked list.
        """
        temp_node = Node(data)  # Create a new node containing your specified value
        temp_node.next_element = self.head_node  # Point the new node to the current head
        self.head_node = temp_node  # # Make the head point to the new node
        return self.head_node  # Return the new head

    def to_list(self):
        """
        Convert the linked list into a standard Python list

        Returns:
            list: A list containing all node values in order.
        """
        node = self.head_node
        result = []
        while node:
            result.append(node.data)
            node = node.next_element
        return result

    @staticmethod
    def search(head, value):
        """
        Search for a node containing the specified value.

        Args:
            head (Node): The head node of the list.
            value: The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        if head is not None:
            while head.next_element is not None:
                if head.data == value:
                    return True
                head = head.next_element
        return False

    @staticmethod
    def insert_at_tail(head, value):
        """
        Insert a new node at the end of the list.

        Args:
            head (Node): The head node of the list.
            value: The value to insert.

        Returns:
            Node: The head node of the updated list.
        """
        temp_node = Node(value)
        if head is None:
            head = temp_node
            return head

        current_node = head
        while current_node.next_element is not None:
            current_node = current_node.next_element
        current_node.next_element = temp_node
        return head

    def delete_at_head(self):
        """
        Delete the first node of the list.

        Returns:
            bool: True if the deletion was successful, False if the list was empty.
        """
        if self.get_head() is None:
            return False
        self.head_node = self.head_node.next_element
        return True

    def delete_value(self, value):
        """
        Delete the first node containing the specified value.

        Args:
            value: The value to delete.

        Returns:
            bool: True if the node was found and deleted, False otherwise.
        """
        print("head:", self.get_head().data)
        if self.get_head() is None:
            return False

        if self.get_head().data == value:
            print("Deleting head")
            self.delete_at_head()
            return True

        current_node = self.get_head()
        while current_node.next_element is not None:
            if current_node.next_element.data == value:
                current_node.next_element = current_node.next_element.next_element
                return True
            current_node = current_node.next_element
        return False

    def length(self):
        """
        Count the number of nodes in the list.

        Returns:
            int: The number of nodes.
        """
        head = self.get_head()
        count = 0
        while head is not None:
            count += 1
            head = head.next_element
        return count

    def reverse(self):
        """
        Reverse the order of nodes in the list.

        Returns:
            Node: The new head node of the reversed list.
        """
        previous = None  # Maintain track of the previous node
        current = self.get_head()  # The current node
        next_node = None  # The next node in the list

        while current:
            next_node = current.next_element
            current.next_element = previous
            previous = current
            current = next_node

        self.head_node = previous
        return self.head_node

    def remove_duplicates(self):
        """
        Remove duplicate values from the list.

        Returns:
            Node: The head node after duplicates are removed.
        """
        head = self.get_head()
        if head is None or head.next_element is None:
            return None
        seen = set()
        current = head
        previous = None
        while current:
            if current.data not in seen:
                seen.add(current.data)
                previous = current
            else:
                previous.next_element = current.next_element
            current = current.next_element
        return self.head_node

    def is_empty(self):
        """
        Check if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head_node is None
