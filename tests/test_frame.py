from uneedtest import TestCase
from unittest.mock import patch

from hemline import Frame
from hemline.colors import Color
from hemline.themes import double, factory


@patch("hemline.frame.get_terminal_width", return_value=100)
class TestFormatting(TestCase):
    def test_creates_frame(self, _):
        container_width = 40
        frame = Frame(container_width=container_width)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "┌──────────────────────────────────────┐",
            "│                                      │",
            "│    Hello, World                      │",
            "│                                      │",
            "└──────────────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_theme(self, _):
        container_width = 40
        frame = Frame(container_width=container_width, theme=double)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "╔══════════════════════════════════════╗",
            "║                                      ║",
            "║    Hello, World                      ║",
            "║                                      ║",
            "╚══════════════════════════════════════╝",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def applies_custom_theme(self, _):
        theme = factory("+")
        container_width = 40
        frame = Frame(container_width=container_width, theme=theme)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "++++++++++++++++++++++++++++++++++++++++",
            "+                                      +",
            "+    Hello, World                      +",
            "+                                      +",
            "++++++++++++++++++++++++++++++++++++++++",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_horizontal_padding(self, _):
        container_width = 40
        frame = Frame(container_width=container_width, horizontal_padding=1)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "┌──────────────────────────────────────┐",
            "│                                      │",
            "│ Hello, World                         │",
            "│                                      │",
            "└──────────────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_vertical_padding(self, _):
        container_width = 40
        frame = Frame(container_width=container_width, vertical_padding=3)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "┌──────────────────────────────────────┐",
            "│                                      │",
            "│                                      │",
            "│                                      │",
            "│    Hello, World                      │",
            "│                                      │",
            "│                                      │",
            "│                                      │",
            "└──────────────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_outer_width(self, _):
        container_width = 40
        frame = Frame(container_width=container_width, outer_width=28)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "      ┌──────────────────────────┐      ",
            "      │                          │      ",
            "      │    Hello, World          │      ",
            "      │                          │      ",
            "      └──────────────────────────┘      ",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_outer_width_and_text_alignment(self, _):
        container_width = 40
        frame = Frame(
            container_width=container_width,
            outer_width=38,
            text_alignment="center",
        )
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            " ┌────────────────────────────────────┐ ",
            " │                                    │ ",
            " │            Hello, World            │ ",
            " │                                    │ ",
            " └────────────────────────────────────┘ ",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_frame_alignment(self, _):
        container_width = 40
        frame = Frame(
            container_width=container_width,
            alignment="left",
            outer_width=38,
        )
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "┌────────────────────────────────────┐  ",
            "│                                    │  ",
            "│    Hello, World                    │  ",
            "│                                    │  ",
            "└────────────────────────────────────┘  ",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_applies_color(self, _):
        container_width = 40
        frame = Frame(container_width=container_width, color=Color.DARK_GREEN)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "\x1b[0;32m┌──────────────────────────────────────┐\x1b[0m",
            "\x1b[0;32m│\x1b[0m                                      \x1b[0;32m│\x1b[0m",
            "\x1b[0;32m│\x1b[0m    Hello, World                      \x1b[0;32m│\x1b[0m",
            "\x1b[0;32m│\x1b[0m                                      \x1b[0;32m│\x1b[0m",
            "\x1b[0;32m└──────────────────────────────────────┘\x1b[0m",
        ]
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_wraps_text(self, _):
        container_width = 30
        text = "Hello, darkness, my old friend"
        frame = Frame(container_width=container_width)
        result = frame.format(text)
        expected_lines = [
            "┌────────────────────────────┐",
            "│                            │",
            "│    Hello, darkness, my     │",
            "│    old friend              │",
            "│                            │",
            "└────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_respects_paragraphs_when_wrapping_text(self, _):
        container_width = 30
        text_lines = [
            "Hello, darkness, my old friend",
            "",
            "I've come to talk with you again",
        ]
        text = "\n".join(text_lines)

        frame = Frame(container_width=container_width)
        result = frame.format(text)
        expected_lines = [
            "┌────────────────────────────┐",
            "│                            │",
            "│    Hello, darkness, my     │",
            "│    old friend              │",
            "│                            │",
            "│    I've come to talk       │",
            "│    with you again          │",
            "│                            │",
            "└────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == container_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)

    def test_remains_in_terminal_width(self, terminal_width_mock):
        terminal_width = 40
        terminal_width_mock.return_value = terminal_width
        frame = Frame(container_width=100)
        text = "Hello, World"
        result = frame.format(text)
        expected_lines = [
            "┌──────────────────────────────────────┐",
            "│                                      │",
            "│    Hello, World                      │",
            "│                                      │",
            "└──────────────────────────────────────┘",
        ]
        assert len(expected_lines[0]) == terminal_width
        expected = "\n".join(expected_lines)
        self.assert_equal(result, expected)
