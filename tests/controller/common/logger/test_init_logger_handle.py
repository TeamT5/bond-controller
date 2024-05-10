# -*- coding:utf-8 -*-
import os
import time
import shutil
import logging
import unittest
import logging.handlers


def safe_remove_directory(directory_path, retries=5, delay=1):
    for _ in range(retries):
        try:
            if os.path.exists(directory_path):
                shutil.rmtree(directory_path)
            return
        except Exception as e:
            time.sleep(delay)
    raise Exception(
        f"Unable to remove directory {directory_path} after {retries} attempts."
    )


class Logger:
    info_logger = logging.getLogger("info_logger")
    logs_path = "your_logs_directory_path"

    _handler_setup = False

    @staticmethod
    def debug(message):
        if not Logger._handler_setup:
            Logger._setup_logger()
        Logger.info_logger.debug(message)

    @staticmethod
    def _setup_logger():
        Logger.info_logger.setLevel(logging.DEBUG)
        Logger._handler_setup = True

    @staticmethod
    def _setup_log_directory():
        if not os.path.exists(Logger.logs_path):
            os.makedirs(Logger.logs_path)

    @staticmethod
    def supported_colors():
        for color in ["red", "blue", "green"]:
            Logger.info_logger.info(f"Supported Color: {color}")


class TestLogger(unittest.TestCase):
    def setUp(self):
        Logger._handler_setup = False
        self.log_capture_string = logging.handlers.BufferingHandler(9999)
        log_format = logging.Formatter(
            "%(asctime)s %(name)s [%(levelname)s] %(message)s"
        )
        self.log_capture_string.setFormatter(log_format)
        Logger.info_logger.addHandler(self.log_capture_string)

    def tearDown(self):
        for handler in Logger.info_logger.handlers[:]:
            handler.close()
        Logger.info_logger.handlers = []
        safe_remove_directory(Logger.logs_path)

    def test_debug_log(self):
        Logger.debug("This is a debug log")
        self.assertTrue(len(self.log_capture_string.buffer) > 0, "No logs captured.")
        log_record = self.log_capture_string.buffer[0]
        self.assertEqual(log_record.levelname, "DEBUG")
        self.assertIn("This is a debug log", log_record.msg)

    def test_log_directory_creation(self):
        safe_remove_directory(Logger.logs_path)
        self.assertFalse(os.path.exists(Logger.logs_path))
        Logger._setup_log_directory()
        self.assertTrue(os.path.exists(Logger.logs_path))

    def test_supported_colors(self):
        Logger.supported_colors()
        logs = [record.msg for record in self.log_capture_string.buffer]
        expected_colors = ["red", "blue", "green"]
        for color in expected_colors:
            self.assertIn(f"Supported Color: {color}", logs)


if __name__ == "__main__":
    unittest.main()
