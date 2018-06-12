import pybind_example


def test__add():
    assert pybind_example.add(1, 2) == 3


def test__add_str():
    assert pybind_example.add_str('1', '2') == 3
