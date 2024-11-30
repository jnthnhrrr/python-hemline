This is yet another python library for creating frames around your terminal
output.

It creates a frame around text, wrapping the text to fit into the frame.

The implementation follows clean code principles such as single responsibility
principle, and dependency injection.


# Install

    pip install hemline


# Use

```python3
from hemline import Frame

frame = Frame()
text = "This is some text"
framed = frame.format(text)
```

## Formatting the Frame

You can pass the following parameters to the constructor
of`hemline.Frame`:

    + `outer_width` (the width of the frame including `horizontal_padding`),
    + `container_width` (defaults to the width of the terminal),
    + `text_alignment` (either `"center"` or `"left"`),
    + `frame_alignment` inside the container (either `"center"` or `"left"`),
    + `horizontal_padding`,
    + `vertical_padding`
    + `color`


## Styling the Frame

### Predefined Themes

The characters defining the edges and corners of the frame make a theme. There
are four predefined themes, with self-explanatory names:

    + `hemline.themes.single`  (The default theme)
    + `hemline.themes.double`
    + `hemline.themes.dotted`
    + `hemline.themes.none`

```python3
from hemline.themes import double

frame = Frame(theme=double)
text = "This is some text"
frame.format(text)
```

### Custom Theme

You can define a custom theme by instancing `hemline.themes.Theme`. If
you want to create a theme based on a single border character, you can use the
`hemline.themes.factory` for your convenience.

### Colorized Frames

If you want the frame in a certain color, you can pass an instance of
`hemline.colors.Color` to the frame's constructor.

If you need more flexibility, you can subclass `hemline.Frame`, implement
a custom colorization function and inject it as class variable `colorize`. This
function must accept a string and a color parameter, and return the colorized
string.
