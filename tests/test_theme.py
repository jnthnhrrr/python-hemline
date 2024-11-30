from uneedtest import TestCase

from hemline.themes import Theme


class TestThemeValidation(TestCase):
    def test_detects_border_characters_with_invalid_length(self):
        with self.assert_raises(ValueError):
            Theme(
                horizontal="+",
                vertical="+",
                top_left="++",
                top_right="+",
                bottom_left="+",
                bottom_right="+",
            )

    def test_detects_border_characters_with_wrong_type(self):
        with self.assert_raises(TypeError):
            Theme(
                horizontal="+",
                vertical="+",
                top_left=1,
                top_right="+",
                bottom_left="+",
                bottom_right="+",
            )
