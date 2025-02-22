"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Stack, Node


def test_push():
    stack = Stack()
    stack.push('test_data1')
    node = stack.top
    assert isinstance(stack.top, Node)
    assert stack.top.data == 'test_data1'
    assert stack.top.next_node is None
    stack.push('test_data2')
    assert isinstance(stack.top.next_node, Node)
    assert stack.top.data == 'test_data2'
    assert stack.top.next_node is node


def test_pop():
    stack = Stack()
    stack.push('test_data1')
    stack.push('test_data2')
    assert stack.pop() == 'test_data2'
    assert stack.pop() == 'test_data1'
    assert stack.pop() is None
    with pytest.raises(AttributeError):
        stack.top.next_node


def test__str__(self):
        stack = Stack()
        self.assertEqual(stack.top, None)



