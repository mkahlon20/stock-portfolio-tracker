import unittest
import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.linked_deque import LinkedDeque

class TestLinkedDeque(unittest.TestCase):
    def setUp(self):
        self.deque = LinkedDeque()

    def test_empty_deque(self):
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.get_front(), None)
        self.assertEqual(self.deque.get_back(), None)

    def test_add_to_front(self):
        self.deque.add_to_front(1)
        self.assertEqual(self.deque.get_front(), 1)
        self.assertEqual(self.deque.get_back(), 1)
        self.deque.add_to_front(2)
        self.assertEqual(self.deque.get_front(), 2)
        self.assertEqual(self.deque.get_back(), 1)

    def test_add_to_back(self):
        self.deque.add_to_back(1)
        self.assertEqual(self.deque.get_front(), 1)
        self.assertEqual(self.deque.get_back(), 1)
        self.deque.add_to_back(2)
        self.assertEqual(self.deque.get_front(), 1)
        self.assertEqual(self.deque.get_back(), 2)

    def test_remove_front(self):
        self.deque.add_to_back(1)
        self.deque.add_to_back(2)
        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.get_front(), 2)
        self.assertEqual(self.deque.remove_front(), 2)
        self.assertTrue(self.deque.is_empty())

    def test_remove_back(self):
        self.deque.add_to_back(1)
        self.deque.add_to_back(2)
        self.assertEqual(self.deque.remove_back(), 2)
        self.assertEqual(self.deque.get_back(), 1)
        self.assertEqual(self.deque.remove_back(), 1)
        self.assertTrue(self.deque.is_empty())

    def test_clear(self):
        self.deque.add_to_back(1)
        self.deque.add_to_back(2)
        self.deque.clear()
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.get_front(), None)
        self.assertEqual(self.deque.get_back(), None)

    def test_display(self):
        self.deque.add_to_back(1)
        self.deque.add_to_back(2)
        self.deque.add_to_back(3)
        self.assertEqual(self.deque.display(), "1 -> 2 -> 3")

if __name__ == '__main__':
    unittest.main()