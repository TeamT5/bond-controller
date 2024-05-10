import os

from controller.common.logger.info_logger_handle import Logger


class Folder:
    @staticmethod
    def check_and_make_folder(folder_path: str) -> None:
        """
        Check folder exists or not, if not, create it.

        :param folder_path: [str] folder path
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            Logger.info(f"Folder {folder_path} created.")
