import pytest

from hash_table.hash_table import HashTable


# --------------------------
# Fixtures
# --------------------------

@pytest.fixture
def empty_table():
    """Return an empty hash table."""
    return HashTable()


@pytest.fixture
def small_table():
    """Return a small table to trigger resize quickly."""
    table = HashTable()
    table.slots = 2  # small slots to force resize
    table.threshold = 0.5
    return table


@pytest.fixture
def collision_table():
    """Return a table designed to produce collisions."""
    table = HashTable()
    table.slots = 2  # small slots for intentional collisions
    return table


@pytest.fixture
def table_with_items():
    """Return a hash table pre-filled with some entries."""
    table = HashTable()
    table.insert("a", 1)
    table.insert("b", 2)
    table.insert("c", 3)
    return table


# --------------------------
# Test insertion and search
# --------------------------

insert_search_cases = [
    ("a", 1),
    ("b", 2),
    ("c", 3),
    ("d", 4),
]

insert_search_ids = [
    "insert_a",
    "insert_b",
    "insert_c",
    "insert_d",
]


@pytest.mark.parametrize(
    "key, value",
    insert_search_cases,
    ids=insert_search_ids
)
def test_insert_and_search(empty_table, key, value):
    # Insert key-value pair
    empty_table.insert(key, value)
    # Search should return the correct value
    assert empty_table.search(key) == value


# --------------------------
# Test deletion
# --------------------------

delete_cases = [
    ("a", True),
    ("b", True),
    ("x", None),  # key not present
]

delete_ids = [
    "delete_a",
    "delete_b",
    "delete_missing",
]


@pytest.mark.parametrize(
    "key, expected",
    delete_cases,
    ids=delete_ids
)
def test_delete(table_with_items, key, expected):
    # Delete the key and check the return value
    assert table_with_items.delete(key) is expected
    # If key existed, it should no longer be found
    if expected:
        assert table_with_items.search(key) is None


# --------------------------
# Test resize functionality
# --------------------------

def _extracted_from_test_resize_sequential_8(table, arg1, arg2):
    # Insert first element
    table.insert(arg1, arg2)
    assert table.get_size() == arg2
    assert table.search(arg1) == arg2


def test_resize_sequential():
    """Test sequential insertions trigger resize and maintain correct size."""
    table = HashTable()
    table.slots = 2
    table.threshold = 0.5
    _extracted_from_test_resize_sequential_8(table, "key1", 1)
    _extracted_from_test_resize_sequential_8(table, "key2", 2)
    _extracted_from_test_resize_sequential_8(table, "key3", 3)

    # Ensure all elements are still retrievable after resize
    assert table.search("key1") == 1
    assert table.search("key2") == 2
    assert table.search("key3") == 3
    assert table.get_size() == 3


# --------------------------
# Test collision handling
# --------------------------

collision_cases = [
    (("a", 1), 1),
    (("c", 2), 2),  # likely collides with "a" when slots=2
]

collision_ids = [
    "insert_a",
    "insert_c_collision",
]


@pytest.mark.parametrize(
    "key_value, expected_value",
    collision_cases,
    ids=collision_ids
)
def test_collisions(collision_table, key_value, expected_value):
    key, value = key_value
    collision_table.insert(key, value)
    # Ensure search returns correct value even if collision occurs
    assert collision_table.search(key) == expected_value
