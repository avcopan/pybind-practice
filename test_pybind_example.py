import pybind_example


def test__add():
    assert pybind_example.add(1, 2) == 3
