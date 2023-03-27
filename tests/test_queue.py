"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue, Node
import unittest
from types import NoneType


class QueueTest(unittest.TestCase):

    def test_init(self):
        """
        Тест конструктора класса Queue
        """
        queue = Queue()
        self.assertEqual(queue.head, None)  # проверка начала очереди
        self.assertEqual(queue.tail, None)  # проверка конца очереди

    def test_enqueue(self):
        """
        Тест метода для добавления элемента в очередь
        """
        queue = Queue()
        queue.enqueue('test')
        self.assertEqual(queue.head.data, 'test')  # тестирование добавления данных
        self.assertEqual(queue.tail.data, 'test')

        queue.enqueue('test_1')  # тестирование следующего узла после головы
        self.assertEqual(queue.head.next_node.data, 'test_1')
        self.assertEqual(queue.tail.data, 'test_1')
        self.assertEqual(queue.tail.next_node, None)  # тест в конце ничего не прицепилось дополнительно

    def test_dequeue(self):
        """
        Тест метода для удаления элемента из очереди с начала
        """
        queue = Queue()
        queue.dequeue()
        self.assertIsNone(queue.head)
        queue.enqueue('test')
        self.assertEqual(queue.head.data, 'test')
        queue.dequeue()
        self.assertIsInstance(queue.head, NoneType)
        with self.assertRaises(AttributeError):
            data = queue.head.data

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), "")
        queue.enqueue("test")
        self.assertEqual(str(queue), "test")