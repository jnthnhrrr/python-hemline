from textwrap import fill


def wrap(text: str, width: int) -> str:
    paragraph_delimiter = "\n\n"
    paragraphs = text.split(paragraph_delimiter)
    return paragraph_delimiter.join(
        fill(paragraph.strip(), width)
        for paragraph in paragraphs
    )
