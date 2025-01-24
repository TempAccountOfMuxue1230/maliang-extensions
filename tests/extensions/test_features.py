import unittest
from unittest.mock import Mock, MagicMock
import tkinter

# 假设这些类可以通过以下方式导入
from maliang.extensions.features import IconOnlyFeature, Underline, Highlight


class TestFeatureClasses(unittest.TestCase):

    def setUp(self):
        self.mock_widget = Mock()
        self.mock_widget.state = "normal"
        self.mock_widget.master = Mock()
        self.mock_widget.master.trigger_config = Mock()
        self.mock_widget.images = [Mock()]
        self.mock_widget.images[0].detect = Mock(return_value=True)
        self.mock_widget.texts = [Mock()]
        self.mock_widget.texts[0].detect = Mock(return_value=True)
        self.mock_widget.texts[0].font = Mock()

    def test_icon_only_feature_motion(self):
        feature = IconOnlyFeature(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        self.assertTrue(feature._motion(event))
        self.mock_widget.master.trigger_config.update.assert_called_with(cursor="hand2")
        self.mock_widget.update.assert_called_with("hover")

    def test_icon_only_feature_button_release(self):
        feature = IconOnlyFeature(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        self.assertTrue(feature._button_release_1(event))
        feature.command.assert_called_once()

    def test_underline_motion(self):
        feature = Underline(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        self.assertTrue(feature._motion(event))
        self.mock_widget.master.trigger_config.update.assert_called_with(cursor="hand2")
        self.mock_widget.update.assert_called_with("hover")
        self.mock_widget.texts[0].font.config.assert_called_with(underline=True)

    def test_underline_button_release(self):
        feature = Underline(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        self.assertTrue(feature._button_release_1(event))
        feature.command.assert_called_once()

    def test_highlight_motion(self):
        feature = Highlight(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        animations_mock = Mock()
        with unittest.mock.patch("your_module.animations", animations_mock):
            self.assertTrue(feature._motion(event))
            self.mock_widget.master.trigger_config.update.assert_called_with(cursor="hand2")
            self.mock_widget.update.assert_called_with("hover")
            animations_mock.ScaleFontSize.assert_called_with(self.mock_widget.texts[0], 28, 150)

    def test_highlight_button_release(self):
        feature = Highlight(self.mock_widget, command=Mock())
        event = Mock(x=10, y=20)

        animations_mock = Mock()
        with unittest.mock.patch("your_module.animations", animations_mock):
            self.assertTrue(feature._button_release_1(event))
            feature.command.assert_called_once()
            animations_mock.ScaleFontSize.assert_called_with(self.mock_widget.texts[0], 28, 150)


if __name__ == "__main__":
    unittest.main()
