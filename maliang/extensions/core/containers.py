"""All containers.

There are two containers at the window level: `Tk` and `Toplevel`. `Tk` is
generally used for the main window, while `Toplevel` is a pop-up window.

There is another container at the canvas level: `Canvas`. `Canvas` is the main
container carrier.
"""

from __future__ import annotations

__all__ = [
    'PageCanvas',
]

import typing

from maliang.core.containers import Canvas, Tk, Toplevel
from .config import *

import maliang


class PageCanvas(Canvas):
    def __init__(
            self,
            side_config: SidePageConfig,
            master: Tk | Toplevel | Canvas | None = None,
            *,
            expand: typing.Literal["", "x", "y", "xy"] = "xy",
            auto_zoom: bool = False,
            default: int = 0,
            keep_ratio: typing.Literal["min", "max"] | None = None,
            free_anchor: bool = False,
            auto_update: bool | None = None,
            zoom_all_items: bool = False,
            **kwargs,
    ) -> None:
        """
        * `master`: parent widget
        * `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
        * `auto_zoom`: whether or not to scale its items automatically
        * `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
        value, `max` follows the maximum value
        * `free_anchor`: whether the anchor point is free-floating
        * `auto_update`: whether the theme manager update it automatically
        * `zoom_all_items`: (Experimental) whether or not to scale its all items
        * `kwargs`: compatible with other parameters of class `tkinter.Canvas`
        """
        super().__init__(
            master,
            expand=expand,
            auto_zoom=auto_zoom,
            keep_ratio=keep_ratio,
            free_anchor=free_anchor,
            auto_update=auto_update,
            zoom_all_items=zoom_all_items,
            **kwargs
        )
        frame_side = maliang.Canvas(self, width=side_config.width, expand="x")
        frame_side.pack(fill="y", side="left")
        self.frame_main = frame_main = maliang.Canvas(self, auto_zoom=True)
        frame_main.pack(fill="both", expand=True)

        self.side_pages = side_config.side_pages

        self.setup_side(frame_side, side_config, default)

    def setup_side(self, frame_side: maliang.Canvas, side_config: SidePageConfig, default: int) -> None:
        canvas = maliang.Canvas(
            frame_side, expand="y", highlightthickness=0)
        canvas.place(width=side_config.width, height=side_config.height)
        maliang.Text(canvas, (side_config.width // 2, side_config.side_button_height),
                             text=side_config.title.text,
                             fontsize=side_config.title.size, anchor="center")
        maliang.Text(
            canvas,
            (side_config.width // 2, int(side_config.side_button_height * 1.8)),
            text=side_config.subtitle.text,
            fontsize=side_config.subtitle.size, anchor="center")

        sizes = ((side_config.width - 50, 50),) * len(side_config.side_pages)
        text = []

        for page in side_config.side_pages:
            text.append(page.name)

        maliang.SegmentedButton(canvas, (20, 140), sizes,
                                default=default, text=tuple(text), command=self.call_canvas, layout="vertical")

    def call_canvas(self, index: int) -> None:
        """"""
        self.side_pages[index].cav(self.frame_main, auto_zoom=True, free_anchor=True, keep_ratio="min")
