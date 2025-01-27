import typing
from tkinter import Canvas


class FontConfig(typing.NamedTuple):
    text: str
    size: int


class SidePage(typing.NamedTuple):
    name: str

    cav: typing.Type[Canvas]


class SidePageConfig(typing.NamedTuple):
    """
    Side page configuration.
    """
    width: int
    height: int
    side_pages: list[SidePage]
    side_button_height: int
    title: FontConfig
    subtitle: FontConfig