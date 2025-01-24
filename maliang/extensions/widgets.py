"""All extensions `Widget` classes"""

from __future__ import annotations

__all__ = [
    'UnderlineButton',
    'HighlightButton',
    'IconButton',
    'IconOnlyButton',
]

import collections.abc
import typing

from maliang.core import configs, containers, virtual
from maliang.toolbox import enhanced, utility
from maliang.standard import images, shapes, styles, texts

from . import features


class UnderlineButton(virtual.Widget):
    """Underline button, generally used to display web links"""

    def __init__(
            self,
            master: containers.Canvas | virtual.Widget,
            position: tuple[int, int],
            *,
            text: str = "",
            family: str | None = None,
            fontsize: int | None = None,
            weight: typing.Literal['normal', 'bold'] = "normal",
            slant: typing.Literal['roman', 'italic'] = "roman",
            underline: bool = False,
            overstrike: bool = False,
            justify: typing.Literal["left", "center", "right"] = "left",
            command: collections.abc.Callable | None = None,
            image: enhanced.PhotoImage | None = None,
            anchor: typing.Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
            capture_events: bool | None = None,
            gradient_animation: bool = False,
            auto_update: bool | None = None,
            style: type[virtual.Style] | None = None,
    ) -> None:
        """
        * `master`: parent canvas
        * `position`: position of the widget
        * `text`: text of the widget
        * `family`: font family
        * `fontsize`: font size
        * `weight`: weight of the text
        * `slant`: slant of the text
        * `underline`: whether the text is underline
        * `overstrike`: whether the text is overstrike
        * `justify`: justify mode of the text
        * `command`: a function that is triggered when the underline button is pressed
        * `image`: image of the widget
        * `anchor`: anchor of the widget
        * `capture_events`: wether detect another widget under the widget
        * `gradient_animation`: wether enable gradient_animation
        * `auto_update`: whether the theme manager update it automatically
        * `style`: style of the widget
        """
        virtual.Widget.__init__(
            self, master, position, utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, master=master),
            anchor=anchor, capture_events=capture_events,
            gradient_animation=gradient_animation, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.UnderlineButtonStyle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.Underline(self, command=command)


class HighlightButton(virtual.Widget):
    """Highlight button, no outline, which added a highlight effect"""

    def __init__(
            self,
            master: containers.Canvas | virtual.Widget,
            position: tuple[int, int],
            *,
            text: str = "",
            family: str | None = None,
            fontsize: int | None = None,
            weight: typing.Literal['normal', 'bold'] = "normal",
            slant: typing.Literal['roman', 'italic'] = "roman",
            underline: bool = False,
            overstrike: bool = False,
            justify: typing.Literal["left", "center", "right"] = "left",
            command: collections.abc.Callable | None = None,
            image: enhanced.PhotoImage | None = None,
            anchor: typing.Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
            capture_events: bool | None = None,
            gradient_animation: bool | None = None,
            auto_update: bool | None = None,
            style: type[virtual.Style] | None = None,
    ) -> None:
        """
        * `master`: parent canvas
        * `position`: position of the widget
        * `text`: text of the widget
        * `family`: font family
        * `fontsize`: font size
        * `weight`: weight of the text
        * `slant`: slant of the text
        * `underline`: whether the text is underline
        * `overstrike`: whether the text is overstrike
        * `justify`: justify mode of the text
        * `command`: a function that is triggered when the hightlight button is pressed
        * `image`: image of the widget
        * `anchor`: anchor of the widget
        * `capture_events`: wether detect another widget under the widget
        * `gradient_animation`: wether enable gradient_animation
        * `auto_update`: whether the theme manager update it automatically
        * `style`: style of the widget
        """
        virtual.Widget.__init__(
            self, master, position, utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, master=master),
            anchor=anchor, capture_events=capture_events,
            gradient_animation=gradient_animation, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.HighlightButtonStyle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.Highlight(self, command=command)


class IconButton(virtual.Widget):
    """A button with an icon on the left side"""

    def __init__(
            self,
            master: containers.Canvas | virtual.Widget,
            position: tuple[int, int],
            size: tuple[int, int] | None = None,
            *,
            text: str = "",
            family: str | None = None,
            fontsize: int | None = None,
            weight: typing.Literal['normal', 'bold'] = "normal",
            slant: typing.Literal['roman', 'italic'] = "roman",
            underline: bool = False,
            overstrike: bool = False,
            justify: typing.Literal["left", "center", "right"] = "left",
            command: collections.abc.Callable | None = None,
            image: enhanced.PhotoImage | None = None,
            anchor: typing.Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
            capture_events: bool | None = None,
            gradient_animation: bool | None = None,
            auto_update: bool | None = None,
            style: type[virtual.Style] | None = None,
    ) -> None:
        """
        * `master`: parent canvas
        * `position`: position of the widget
        * `size`: size of the widget
        * `text`: text of the widget
        * `family`: font family
        * `fontsize`: font size
        * `weight`: weight of the text
        * `slant`: slant of the text
        * `underline`: whether the text is underline
        * `overstrike`: whether the text is overstrike
        * `justify`: justify mode of the text
        * `command`: a function that is triggered when the button is pressed
        * `image`: image of the widget
        * `anchor`: anchor of the widget
        * `capture_events`: wether detect another widget under the widget
        * `gradient_animation`: wether enable gradient_animation
        * `auto_update`: whether the theme manager update it automatically
        * `style`: style of the widget
        """
        if size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=master)
            size = size[0] + size[1] - 6, size[1]
        virtual.Widget.__init__(
            self, master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.IconButtonStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, ((size[1] - size[0]) / 2, 0), image=image)
        texts.Information(
            self, (size[1] - size[0] / 2, 0), text=text, family=family, fontsize=fontsize,
            weight=weight, slant=slant, underline=underline, overstrike=overstrike,
            justify=justify, anchor="w")
        self.feature = features.ButtonFeature(self, command=command)

    def get(self) -> str:
        """Get the text of the widget"""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget"""
        return self.texts[0].set(text)


class IconOnlyButton(IconButton):
    """A button with nothing but an icon"""

    def __init__(
            self,
            master: containers.Canvas | virtual.Widget,
            position: tuple[int, int],
            size: tuple[int, int] | None = None,
            *,
            command: collections.abc.Callable | None = None,
            image: enhanced.PhotoImage | None = None,
            borderless=True,
            anchor: typing.Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
            capture_events: bool | None = None,
            gradient_animation: bool | None = None,
            auto_update: bool | None = None,
            style: type[virtual.Style] | None = None,
    ) -> None:
        """
        * `master`: parent canvas
        * `position`: position of the widget
        * `size`: size of the widget
        * `command`: a function that is triggered when the button is pressed
        * `image`: image of the widget
        * `anchor`: anchor of the widget
        * `capture_events`: wether detect another widget under the widget
        * `gradient_animation`: wether enable gradient_animation
        * `auto_update`: whether the theme manager update it automatically
        * `style`: style of the widget
        """
        if size is None:
            size = image.width(), image.height()
        virtual.Widget.__init__(
            self, master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.TextStyle(self) if borderless else styles.IconButtonStyle(self)
        if image is not None:
            images.StillImage(self, ((size[1] - size[0]) / 2, 0), image=image)
        self.feature = features.IconOnlyFeature(self, command=command)

    def get(self) -> Exception:
        """This class has nothing to get"""
        raise AttributeError()

    def set(self, thing: None) -> Exception:
        """This class has nothing to set"""
        raise AttributeError()
