# -*- coding:utf-8 -*-
import logging
import unittest
from io import StringIO
from termcolor import colored

from bond_controller_action.controller.action_config import setting


class ColoredFormatter(logging.Formatter):
    def __init__(self, use_colors=True):
        super().__init__()
        self.use_colors = use_colors

    def colored_text(self, text, color, on_color=None, attrs=None):
        if self.use_colors:
            return colored(text, color, on_color, attrs)
        return text

    def format(self, record):
        log_level = record.levelname
        time_color = "white"
        log_message = record.getMessage()
        log_message = self.colored_text(
            log_message, setting.LOG_COLOR.get(log_level, "white")
        )
        formatted = f"[{self.colored_text(str(record.created), time_color)}] {log_level}: {log_message}"
        return formatted


class TestColoredFormatter(unittest.TestCase):
    def setUp(self):
        self.log_stream = StringIO()
        self.handler = logging.StreamHandler(self.log_stream)

        self.logger_name = f"test_logger_{id(self)}"
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.handler.setFormatter(ColoredFormatter(use_colors=True))
        self.logger.addHandler(self.handler)

    def test_debug_log_color(self):
        expected_color = setting.LOG_COLOR.get("DEBUG", "white")
        self.logger.debug("This is a debug log")
        self.handler.flush()
        output = self.log_stream.getvalue()

        self.assertIn(colored("DEBUG", expected_color), output)

        self.log_stream.truncate(0)
        self.log_stream.seek(0)

    def test_info_log_color(self):
        expected_color = setting.LOG_COLOR.get("INFO", "white")
        self.logger.info("This is an info log")
        self.handler.flush()
        output = self.log_stream.getvalue()

        self.assertIn(colored("INFO", expected_color), output)

    def tearDown(self):
        self.log_stream.close()
        self.handler.close()
        logging.getLogger(self.logger_name).handlers = []


if __name__ == "__main__":
    unittest.main()
