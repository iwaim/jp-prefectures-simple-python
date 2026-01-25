import pytest

from src.jp_prefectures_simple import code2name, name2code


def test_code2name():
    with pytest.raises(KeyError):
        code2name("0")


def test_code2name_typeerror():
    with pytest.raises(TypeError):
        code2name()

    with pytest.raises(TypeError):
        code2name(3.14)

    with pytest.raises(TypeError):
        code2name({1: "北海道"})

    with pytest.raises(TypeError):
        code2name(None)


def test_name2code():
    with pytest.raises(KeyError):
        name2code("名古屋県")


def test_name2code_typeerror():
    with pytest.raises(TypeError):
        name2code()

    with pytest.raises(TypeError):
        name2code(123)

    with pytest.raises(TypeError):
        name2code(3.14)

    with pytest.raises(TypeError):
        name2code({1: "北海道"})

    with pytest.raises(TypeError):
        name2code(None)

    with pytest.raises(TypeError):
        name2code(True)


if __name__ == "__main__":
    test_name2code()
    test_code2name()
