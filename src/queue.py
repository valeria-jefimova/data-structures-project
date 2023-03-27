class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if not self.head:  # отрабатывает тогда, если не существует первого элемента
            self.head = node  # создаем первый элемент
            self.tail = node  # так как это первый элемент, он равен и началу и концу цепи
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            dequeue_node = self.head
            self.head = self.head.next_node
        return dequeue_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        if self.head is None:
            return ''
        head = self.head
        while head:
            result.append(head.data)
            head = head.next_node
        return '\n'.join(result)
