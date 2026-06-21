"""Tests for MyLinkedList edge cases: traverse, remove predicates, out-of-bounds get."""

from app.core.linked_list import MyLinkedList


def test_traverse_collects_all_items():
    print("Testing MyLinkedList.traverse - collects all items in order...")
    lst = MyLinkedList()
    lst.addLast("X")
    lst.addLast("Y")
    lst.addLast("Z")
    result = []
    lst.traverse(lambda item: result.append(item))
    assert result == ["X", "Y", "Z"]
    print("traverse collects all items - passed!")


def test_traverse_empty_list():
    print("Testing MyLinkedList.traverse - empty list calls action zero times...")
    lst = MyLinkedList()
    result = []
    lst.traverse(lambda item: result.append(item))
    assert result == []
    print("traverse empty list - passed!")


def test_remove_item_not_found_returns_false():
    print("Testing MyLinkedList.remove - item not found returns False...")
    lst = MyLinkedList()
    lst.addLast("A")
    lst.addLast("B")
    assert lst.remove("Z") is False
    assert lst.size() == 2
    print("remove not found returns False - passed!")


def test_remove_from_empty_list_returns_false():
    print("Testing MyLinkedList.remove - empty list returns False...")
    lst = MyLinkedList()
    assert lst.remove("A") is False
    print("remove from empty list - passed!")


def test_remove_with_predicate():
    print("Testing MyLinkedList.remove - callable predicate removes correct item...")
    lst = MyLinkedList()
    lst.addLast(10)
    lst.addLast(20)
    lst.addLast(30)
    removed = lst.remove(lambda x: x == 20)
    assert removed is True
    assert lst.size() == 2
    assert lst.get(0) == 10
    assert lst.get(1) == 30
    print("remove with predicate - passed!")


def test_get_out_of_bounds_returns_none():
    print("Testing MyLinkedList.get - out of bounds returns None...")
    lst = MyLinkedList()
    lst.addLast("A")
    assert lst.get(1) is None
    assert lst.get(5) is None
    print("get out of bounds returns None - passed!")


def test_get_negative_index_returns_none():
    print("Testing MyLinkedList.get - negative index returns None...")
    lst = MyLinkedList()
    lst.addLast("A")
    assert lst.get(-1) is None
    print("get negative index returns None - passed!")


def test_get_on_empty_list_returns_none():
    print("Testing MyLinkedList.get - empty list returns None...")
    lst = MyLinkedList()
    assert lst.get(0) is None
    print("get on empty list returns None - passed!")


def test_find_not_found_returns_none():
    print("Testing MyLinkedList.find - no match returns None...")
    lst = MyLinkedList()
    lst.addLast("A")
    lst.addLast("B")
    result = lst.find(lambda x: x == "Z")
    assert result is None
    print("find not found returns None - passed!")


def test_find_on_empty_list_returns_none():
    print("Testing MyLinkedList.find - empty list returns None...")
    lst = MyLinkedList()
    assert lst.find(lambda x: x == "A") is None
    print("find on empty list returns None - passed!")


if __name__ == "__main__":
    test_traverse_collects_all_items()
    test_traverse_empty_list()
    test_remove_item_not_found_returns_false()
    test_remove_from_empty_list_returns_false()
    test_remove_with_predicate()
    test_get_out_of_bounds_returns_none()
    test_get_negative_index_returns_none()
    test_get_on_empty_list_returns_none()
    test_find_not_found_returns_none()
    test_find_on_empty_list_returns_none()
    print("All MyLinkedList edge case tests passed!")
