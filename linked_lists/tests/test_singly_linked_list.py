import unittest

from linked_lists.singly_linked_list import Node
from linked_lists.singly_linked_list import SinglyLinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Create a linked list before each test: 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4"""
        self.list = SinglyLinkedList()

        # Create the head node
        self.list.head_node = Node(1)
        current = self.list.head_node

        # Append the remaining nodes
        for val in [1, 2, 2, 3, 3, 4]:
            new_node = Node(val)
            current.next_element = new_node
            current = new_node

    def test_initial_structure(self):
        """Verify that the list was created correctly"""
        self.assertEqual(self.list.to_list(), [1, 1, 2, 2, 3, 3, 4])

    def test_remove_duplicates(self):
        """Check that duplicate values are removed properly"""
        self.list.remove_duplicates()
        self.assertEqual(self.list.to_list(), [1, 2, 3, 4])

    def test_length(self):
        """Check that the length of the list is correct"""
        self.assertEqual(self.list.length(), 7)

    def test_reverse(self):
        """Check that the list is reversed correctly"""
        self.list.reverse()
        self.assertEqual(self.list.to_list(), [4, 3, 3, 2, 2, 1, 1])

    def test_search(self):
        """Check if the search function correctly finds or misses values"""
        head = self.list.get_head()
        self.assertTrue(SinglyLinkedList.search(head, 3))
        self.assertFalse(SinglyLinkedList.search(head, 10))

    def test_delete_value(self):
        """Check that deleting a specific value works"""
        self.assertTrue(self.list.delete_value(4))  # Should delete 4
        self.assertFalse(SinglyLinkedList.search(self.list.get_head(), 4))

    def test_delete_at_head(self):
        """Check that deleting the head node works"""
        self.assertTrue(self.list.delete_at_head())
        # After deleting first node (1), the next '1' becomes the new head
        self.assertEqual(self.list.get_head().data, 1)

    def test_insert_at_head(self):
        """Check that inserting a new head works"""
        self.list.insert_at_head(0)
        self.assertEqual(self.list.get_head().data, 0)
        self.assertEqual(self.list.get_head().next_element.data, 1)

    def test_insert_at_tail(self):
        """Check that inserting a value at the tail works"""
        head = self.list.get_head()
        SinglyLinkedList.insert_at_tail(head, 5)
        self.assertEqual(self.list.to_list()[-1], 5)


if __name__ == "__main__":
    # Run all test cases when this file is executed directly
    unittest.main(verbosity=2)
