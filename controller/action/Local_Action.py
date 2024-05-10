# -*- coding:utf-8 -*-
import subprocess

from controller.action_config import setting
from controller.common.logger.info_logger_handle import Logger


class Local_Action:
    @staticmethod
    def whoami() -> str:
        """
        Get current user name.
        :return: [str] current user name
        """

        whoami = subprocess.check_output(["whoami"]).decode("utf-8").strip()
        Logger.info(whoami)

        return whoami

    @staticmethod
    def version(version: str = setting.VERSION) -> str:
        """
        Get Bond Controller Version.

        :param version: [str] Bond Controller Version (default: action_version).
        :return: [str] Bond Controller Version
        """
        Logger.info(f"Bond Controller Version: {version}")

        return version
