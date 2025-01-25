import unittest
from unittest.mock import MagicMock, Mock
from maliang.core.containers import Canvas, Tk
from maliang.extensions import FontConfig, SidePage, SidePageConfig, PageCanvas
import maliang

class TestPageCanvas(unittest.TestCase):

    def setUp(self):
        self.tk = Tk()

        # 设置测试数据
        self.side_page_config = SidePageConfig(
            width=200,
            height=400,
            side_pages=[SidePage(name="Page 1", cav=MagicMock()),
                        SidePage(name="Page 2", cav=MagicMock())],
            side_button_height=30,
            title=FontConfig(text="Test Title", size=12),
            subtitle=FontConfig(text="Test Subtitle", size=10)
        )

    def test_page_canvas_initialization(self):
        # 实例化PageCanvas对象并确保它正确初始化
        page_canvas = PageCanvas(side_config=self.side_page_config, master=self.tk)

        # 确认正确传入了参数
        self.assertEqual(page_canvas.side_pages, self.side_page_config.side_pages)

        # 验证 `frame_side` 和 `frame_main` 是否被正确初始化并且为预期的类型
        self.assertIsInstance(page_canvas.frame_main, maliang.Canvas)

    def test_setup_side(self):
        # 测试 setup_side 方法
        page_canvas = PageCanvas(side_config=self.side_page_config, master=self.tk)

        # mock frame_side
        mock_frame_side = MagicMock()

        # 调用 setup_side 方法
        page_canvas.setup_side(mock_frame_side, self.side_page_config, default=0)

        # 验证 canvas 和 Text 是否正确调用
        mock_frame_side.place.assert_called_with(width=self.side_page_config.width, height=self.side_page_config.height)
        self.assertEqual(mock_frame_side.place.call_count, 1)

        # 验证创建 Text 元素
        self.assertEqual(len(mock_frame_side.mock_calls), 2)  # 两次 Text 元素调用

    def test_call_canvas(self):
        # 测试 call_canvas 方法
        page_canvas = PageCanvas(side_config=self.side_page_config, master=self.tk)

        # mock frame_main
        mock_frame_main = MagicMock()

        # 假设选择的是第一个页面
        page_canvas.frame_main = mock_frame_main
        page_canvas.call_canvas(0)

        # 验证是否正确调用了SidePage的Canvas
        page_canvas.side_pages[0].cav.assert_called_with(mock_frame_main, auto_zoom=True, free_anchor=True, keep_ratio="min")

    def test_invalid_side_page(self):
        # 测试无效的side_page配置
        invalid_config = SidePageConfig(
            width=200,
            height=400,
            side_pages=[],
            side_button_height=30,
            title=FontConfig(text="Test Title", size=12),
            subtitle=FontConfig(text="Test Subtitle", size=10)
        )

        # 创建 PageCanvas 实例时传入无效的side_page配置
        page_canvas = PageCanvas(side_config=invalid_config, master=self.tk)

        # 确保没有错误，且side_pages是空的
        self.assertEqual(page_canvas.side_pages, [])

if __name__ == '__main__':
    unittest.main()
