def test_print():
    print("Hello")


class TestPrint:
    def test_1(self):
        print("1")

    def test_2(self):
        print("2")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"
