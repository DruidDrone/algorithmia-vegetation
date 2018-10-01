from . import vegetation

def test_vegetation():
    assert vegetation.apply("Jane") == "hello Jane"
