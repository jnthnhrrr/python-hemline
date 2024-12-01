from dataclasses import dataclass, field
from typing import Any, Callable

from .alignment import Alignment, get_alignment_method
from .defaults import (
    DEFAULT_COLORIZE,
    DEFAULT_FRAME_ALIGNMENT,
    DEFAULT_HORIZONTAL_PADDING,
    DEFAULT_OUTER_WIDTH,
    DEFAULT_TEXT_ALIGNMENT,
    DEFAULT_TEXT_WRAP,
    DEFAULT_THEME,
    DEFAULT_VERTICAL_PADDING,
)
from .themes import Theme
from .utils import get_terminal_width


@dataclass
class Frame:
    color: Any | None = None
    text_alignment: Alignment = DEFAULT_TEXT_ALIGNMENT
    alignment: Alignment = DEFAULT_FRAME_ALIGNMENT
    theme: Theme = field(default_factory=lambda: DEFAULT_THEME)
    horizontal_padding: int = DEFAULT_HORIZONTAL_PADDING
    vertical_padding: int = DEFAULT_VERTICAL_PADDING
    outer_width: int = DEFAULT_OUTER_WIDTH
    container_width: int | None = None

    colorize: Callable[[str, Any], str] = DEFAULT_COLORIZE
    wrap: Callable[[str, int], str] = DEFAULT_TEXT_WRAP

    @property
    def effective_container_width(self) -> int:
        terminal_width = get_terminal_width()
        if self.container_width is None:
            return terminal_width

        return min(self.container_width, terminal_width)

    @property
    def effective_outer_width(self) -> int:
        return min(self.outer_width, self.effective_container_width)

    @property
    def inner_width(self) -> int:
        return self.effective_outer_width - 2

    @property
    def text_width(self) -> int:
        return self.inner_width - 2*self.horizontal_padding

    @property
    def vertical_border(self) -> str:
        character = self.theme.vertical
        if self.color:
            character = self.colorize(character, self.color)
        return character

    def format(self, text: str) -> str:
        text = self.wrap(text, self.text_width)
        raw_lines = text.split("\n")
        raw_lines = (
            [""] * self.vertical_padding + raw_lines + [""] * self.vertical_padding
        )
        top_line = self._border_line(
            left=self.theme.top_left,
            right=self.theme.top_right,
        )
        bottom_line = self._border_line(
            left=self.theme.bottom_left,
            right=self.theme.bottom_right,
        )
        framed_lines = [self._framed_line(text=line) for line in raw_lines]
        return "\n".join([top_line] + framed_lines + [bottom_line])

    def _pad_line(self, line : str) -> str:
        return " " * self.horizontal_padding + line + " " * self.horizontal_padding

    def _apply_vertical_border(self, line: str) -> str:
        return self.vertical_border + line + self.vertical_border

    def _align_text(self, line: str) -> str:
        return get_alignment_method(self.text_alignment)(line, self.inner_width)

    def _align_framed_line(self, line: str) -> str:
        return get_alignment_method(self.alignment)(line, self.effective_container_width)

    def _border_line(
        self,
        left: str,
        right: str,
    ) -> str:
        line = left + self.inner_width * self.theme.horizontal + right
        line = self._align_framed_line(line)
        if self.color:
            return self.__class__.colorize(line, self.color)
        return line

    def _framed_line(self, text: str) -> str:
        text = self._pad_line(text)
        text = self._align_text(text)
        text = self._apply_vertical_border(text)
        text = self._align_framed_line(text)
        return text
