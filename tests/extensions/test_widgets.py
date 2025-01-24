import unittest
from unittest.mock import Mock

from maliang.extensions.wedgets import UnderlineButton, HighlightButton, IconButton, IconOnlyButton


class TestWidgetClasses(unittest.TestCase):

    def setUp(self):
        self.mock_canvas = Mock()

    def test_underline_button_initialization(self):
        button = UnderlineButton(
            master=self.mock_canvas,
            position=(10, 20),
            text="Click Me",
            fontsize=12,
            weight="bold",
            underline=True,
            command=lambda: print("Clicked")
        )
        self.assertEqual(button.style.__class__.__name__, "UnderlineButtonStyle")
        self.assertEqual(button.feature.command.__name__, "<lambda>")

    def test_highlight_button_initialization(self):
        button = HighlightButton(
            master=self.mock_canvas,
            position=(30, 40),
            text="Highlight",
            fontsize=14,
            gradient_animation=True
        )
        self.assertEqual(button.style.__class__.__name__, "HighlightButtonStyle")
        self.assertTrue(button.gradient_animation)

    def test_icon_button_initialization_and_get_set_text(self):
        button = IconButton(
            master=self.mock_canvas,
            position=(50, 60),
            size=(100, 40),
            text="Icon Button",
            image=Mock(),
            command=lambda: print("Icon Clicked")
        )
        self.assertEqual(button.get(), "Icon Button")

        button.set("New Text")
        self.assertEqual(button.get(), "New Text")

    def test_icon_only_button_initialization(self):
        mock_image = Mock()
        mock_image.width.return_value = 40
        mock_image.height.return_value = 40

        button = IconOnlyButton(
            master=self.mock_canvas,
            position=(70, 80),
            image=mock_image,
            command=lambda: print("Icon Only Clicked"),
            borderless=False
        )
        self.assertEqual(button.style.__class__.__name__, "IconButtonStyle")

        with self.assertRaises(AttributeError):
            button.get()

        with self.assertRaises(AttributeError):
            button.set(None)


if __name__ == "__main__":
    unittest.main()
