"""All standard `Feature` classes"""

from __future__ import annotations

__all__ = [
    "IconOnlyFeature",
    "Underline",
    "Highlight",
]

import tkinter

from maliang.animation import animations, controllers
from maliang.toolbox import utility
from maliang.standard.features import ButtonFeature


class IconOnlyFeature(ButtonFeature):
    """Feature of Icon Only Button"""

    def _motion(self, event: tkinter.Event) -> bool:
        if flag := self.widget.images[0].detect(event.x, event.y):
            cursor = utility.fix_cursor(
                "disabled" if self.widget.state == "disabled" else "hand2")
            self.widget.master.trigger_config.update(cursor=cursor)
            if self.widget.state == "normal":
                self.widget.update("hover")
        else:
            if self.widget.state != "normal":
                self.widget.update("normal")
        return flag

    def _button_release_1(self, event: tkinter.Event) -> bool:
        if flag := self.widget.images[0].detect(event.x, event.y):
            if self.widget.state == "active":
                self.widget.update("hover")
                if self.command is not None:
                    self.command(*self._args)
        return flag


class Underline(ButtonFeature):
    """Feature of underline"""

    def _motion(self, event: tkinter.Event) -> bool:
        if flag := self.widget.texts[0].detect(event.x, event.y):
            cursor = utility.fix_cursor(
                "disabled" if self.widget.state == "disabled" else "hand2")
            self.widget.master.trigger_config.update(cursor=cursor)
            if self.widget.state == "normal":
                self.widget.update("hover")
                self.widget.texts[0].font.config(underline=True)
        else:
            if self.widget.state != "normal":
                self.widget.update("normal")
                self.widget.texts[0].font.config(underline=False)
        return flag

    def _button_1(self, _: tkinter.Event) -> bool:
        if flag := self.widget.state == "hover":
            self.widget.update("active")
        return flag

    def _button_release_1(self, event: tkinter.Event) -> bool:
        if flag := self.widget.texts[0].detect(event.x, event.y):
            if self.widget.state == "active":
                self.widget.update("hover")
                self.widget.texts[0].font.config(underline=True)
                if self.command is not None:
                    self.command(*self._args)
        return flag


class Highlight(ButtonFeature):
    """Feature of highlight"""

    def _motion(self, event: tkinter.Event) -> bool:
        if flag := self.widget.texts[0].detect(event.x, event.y):
            cursor = utility.fix_cursor(
                "disabled" if self.widget.state == "disabled" else "hand2")
            self.widget.master.trigger_config.update(cursor=cursor)
            if self.widget.state == "normal":
                self.widget.update("hover")
                animations.ScaleFontSize(self.widget.texts[0], 28, 150).start()
        else:
            if self.widget.state != "normal":
                self.widget.update("normal")
                animations.ScaleFontSize(self.widget.texts[0], 24, 150).start()
        return flag

    def _button_1(self, _: tkinter.Event) -> bool:
        if flag := self.widget.state == "hover":
            self.widget.update("active")
            animations.ScaleFontSize(self.widget.texts[0], 26, 150).start()
        return flag

    def _button_release_1(self, event: tkinter.Event) -> bool:
        if flag := self.widget.texts[0].detect(event.x, event.y):
            if self.widget.state == "active":
                self.widget.update("hover")
                animations.ScaleFontSize(self.widget.texts[0], 28, 150).start()
                if self.command is not None:
                    self.command(*self._args)
        return flag
