# Styling the Frame

## Predefined Themes

The characters defining the edges and corners of the frame make a theme.
[`hemline.themes`][hemline.themes] provides four predefined themes, with self-explanatory names:

+ [`single`][hemline.themes.single]  (The default theme)
+ [`double`][hemline.themes.double]
+ [`dotted`][hemline.themes.dotted]
+ [`none`][hemline.themes.none]

```python3
from hemline.themes import double

frame = Frame(theme=double)
text = "This is some text"
frame.format(text)
```

## Custom Theme

You can define a custom theme by instancing a [`Theme`][hemline.themes.Theme].
If you want to create a theme based on a single border character, you can use
the [`factory`][hemline.themes.factory] for your convenience.

## Colorized Frames

If you want the frame in a certain color, you can pass an instance of
[`colors.Color`][hemline.colors.Color] to the frame's constructor.

If you need more flexibility, you can also pass a colorization function into the
constructor of [`Frame`][hemline.Frame]. This function must accept a string and the
color parameter you pass in the `color` argument of the `Frame`'s constructor,
and return the colorized version of the string.

## Wrapping Text Inside The Frame

Text inside the frame is wrapped by keeping paragraphs intact (a paragraph being
defined as an occurrence of two line breaks in a row), but condensing line
breaks.

If you want to apply a different way of wrapping the text, you can define a
custom wrapping function and inject it into the constructor of `Frame` by
passing it through the `wrap` parameter. The wrapping function must have the
function signature `Callable[[str, int], str]`, with the first parameter being
the input string, and the second parameter being the target width.

Under the hood, `hemline` uses the
[`tamal`](https://github.com/jnthnhrrr/python-tamal) library for wrapping. It
allows for a lot of customization. If you want to change specifics in the
wrapping method, you might find what you need there. Here is one example:

```python
from tamal import wrap

def custom_wrapping(text: str, width: int) -> str:
    return wrap(text, width, paragraph="\n", soft_hyphen="+++")

frame_with_custom_wrapping = Frame(wrap=custom_wrapping)
```

The example above will treat linebreaks as paragraph boundaries, i.e. it will
treat them as hard linebreaks.
