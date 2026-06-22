"""Tests for MyLinkedList data structure."""

from app.core.linked_list import MyLinkedList


def test_linked_list():
    print("Testing MyLinkedList...")
    lst = MyLinkedList()
    assert lst.size() == 0

    lst.addLast("A")
    lst.addLast("B")
    lst.addLast("C")
    assert lst.size() == 3
    assert lst.get(0) == "A"
    assert lst.get(1) == "B"
    assert lst.get(2) == "C"

    # test find
    found = lst.find(lambda x: x == "B")
    assert found == "B"

    # test remove from middle
    removed = lst.remove("B")
    assert removed is True
    assert lst.size() == 2
    assert lst.get(0) == "A"
    assert lst.get(1) == "C"

    # test remove head
    removed = lst.remove("A")
    assert removed is True
    assert lst.size() == 1
    assert lst.get(0) == "C"
    assert lst.head.data == "C"
    assert lst.tail.data == "C"

    # test remove last
    removed = lst.remove("C")
    assert removed is True
    assert lst.size() == 0
    assert lst.head is None
    assert lst.tail is None
    print("MyLinkedList tests passed!")


if __name__ == "__main__":
    test_linked_list()
    print("All linked list tests passed!")
