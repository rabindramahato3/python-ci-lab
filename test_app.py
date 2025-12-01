def add_numbers(a, b):
    return a + b

def test_add_numbers():
    """Simple test case."""
    assert add_numbers(1, 2) == 4
    assert add_numbers(5, -5) == 0
