from uneedtest import TestCase

from hemline.alignment import center, left, right


class TestCenter(TestCase):
    def test_centers_text(self):
        target_length = 8
        text = "123456"
        result = center(text, target_length)
        expected = " 123456 "
        assert len(expected) == target_length
        self.assert_equal(result, expected)

    def test_adds_left_padding_first(self):
        target_length = 7
        text = "123456"
        result = center(text, target_length)
        expected = " 123456"
        assert len(expected) == target_length
        self.assert_equal(result, expected)

    def test_ignores_invisible_ansi_characters(self):
        invisible = "\033[0;31m"
        text = invisible + "123456"
        target_length = 8
        result = center(text, target_length)
        expected = " " + text + " "
        self.assert_equal(result, expected)


class TestLeft(TestCase):
    def test_adds_padding_on_the_right(self):
        target_length = 8
        text = "123456"
        result = left(text, target_length)
        expected = "123456  "
        assert len(expected) == target_length
        self.assert_equal(result, expected)


class TestRight(TestCase):
    def test_adds_padding_on_the_left(self):
        target_length = 8
        text = "123456"
        result = right(text, target_length)
        expected = "  123456"
        assert len(expected) == target_length
        self.assert_equal(result, expected)
