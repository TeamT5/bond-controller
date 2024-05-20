# -*- coding:utf-8 -*-
import os
import base64

from controller.action_config import setting
from controller.common.zip.zip import ZipTool
from controller.common.about_folder import Folder
from controller.action.common.response import ResponseMethod
from controller.common.logger.info_logger_handle import Logger


class Endpoint_Action:
    """
    Endpoint_Action 類別，用於管理與 agent 端點的各種互動。
    """

    @staticmethod
    def bond_info(dest: str, port: int = setting.AGENT_PORT) -> str:
        """
        Get agent info.

        :param dest: [str] target host address.
        :param port: [str] target host port (default: 8086).
        :return: [str] text
        """
        Logger.info(f"Get agent info from {dest}:{port}")
        url = f"http://{dest}:{port}/bond_info/"

        return ResponseMethod.get_text(url)

    @staticmethod
    def send_folder_to_agent(
        dest: str,
        folder_path: str,
        target: str,
        port: int = setting.AGENT_PORT,
        exclude_files: tuple = (),
        exclude_dirs: tuple = (),
    ) -> str:
        """
        Send folder to agent.

        :param dest: [str] target host address.
        :param filepath: [str] filepath to send.
        :param target: [str] target filepath.
        :param port: [int] target host port (default: 8086).
        :param exclude_files: [tuple] files to exclude.
        :param exclude_dirs: [tuple] directories to exclude.
        :return: [str] text
        """
        Logger.info(f"Sending folder to agent at {dest}:{port}")

        zip_folder_base64_data = ZipTool.zip_dir(
            folder_path, exclude_files, exclude_dirs
        )

        data = {"target": target, "folder_content": zip_folder_base64_data}
        url = f"http://{dest}:{port}/upload_folder/"

        return ResponseMethod.post_text(url, json=data)

    @staticmethod
    def send_file_to_agent(
        dest: str, filepath: str, target: str, port: int = setting.AGENT_PORT
    ) -> str:
        """
        Send file to agent.

        :param dest: [str] target host address.
        :param filepath: [str] filepath to send.
        :param target: [str] target filepath.
        :param port: [int] target host port (default: 8086).
        :return: [str] text
        """

        Logger.debug(filepath)

        Logger.info(f"Sending file to agent at {dest}:{port}")
        with open(filepath, "rb") as f:
            file_content = base64.b64encode(f.read()).decode("utf-8")

        data = {"target": target, "file_content": file_content}
        url = f"http://{dest}:{port}/upload_file/"

        return ResponseMethod.post_text(url, json=data)

    @staticmethod
    def execute_file(
        dest: str,
        target: str,
        timeout: int = setting.EXECUTE_TIMEOUT,
        port: int = setting.AGENT_PORT,
        extra_args: tuple = (),
    ) -> str:
        """
        Execute file at endpoint.

        :param dest: [str] target host address.
        :param target: [str] target filepath.
        :param timeout: [int] timeout (default: 0).
        :param port: [int] target host port (default: 8086).
        :param extra_args: [str] extra args.
        :return: [tuple] text
        """
        Logger.info(
            f"Executing file at {dest}:{port} on {target} with timeout {timeout}"
        )
        url = f"http://{dest}:{port}/execute_file/"
        data = {"to_be_executed": target, "timeout": timeout, "extra_args": extra_args}

        return ResponseMethod.post_text(url, json=data)

    @staticmethod
    def execute_python_folder(
        dest: str,
        target: str,
        timeout: int = setting.EXECUTE_TIMEOUT,
        port: int = setting.AGENT_PORT,
        extra_args: tuple = (),
    ) -> str:
        """
        Execute python folder at endpoint.

        :param dest: [str] target host address.
        :param target: [str] target folderpath.
        :param timeout: [int] timeout (default: 0).
        :param port: [int] target host port (default: 8086).
        :param extra_args: [str] extra args.
        :return: [tuple] text
        """
        Logger.info(
            f"Executing python folder at {dest}:{port} on {target} with timeout {timeout}"
        )
        url = f"http://{dest}:{port}/execute_python_folder/"
        data = {"to_be_executed": target, "timeout": timeout, "extra_args": extra_args}

        return ResponseMethod.post_text(url, json=data)

    @staticmethod
    def send_python_folder_to_execute(
        dest: str,
        folder_path: str,
        target: str,
        port: int = setting.AGENT_PORT,
        exclude_files: tuple = (),
        exclude_dirs: tuple = (),
        timeout: int = setting.EXECUTE_TIMEOUT,
        extra_args: list = [],
    ) -> dict:
        """
        Send python folder to endpoint to execute.

        :param dest: [str] target host address.
        :param folder_path: [str] folder path.
        :param target: [str] target folder.
        :param port: [int] target host port (default: 8086).
        :param exclude_files: [tuple] files to exclude.
        :param exclude_dirs: [tuple] directories to exclude.
        :param timeout: [int] timeout (default: 0).
        :param extra_args: [list] extra args.
        :return: [dict] result
        """

        result = {}

        result["send_folder_to_agent"] = Endpoint_Action.send_folder_to_agent(
            dest, folder_path, target, port, exclude_files, exclude_dirs
        )
        result["execute_file"] = Endpoint_Action.execute_python_folder(
            dest, target, timeout, port, extra_args
        )

        return result

    @staticmethod
    def send_file_to_execute(
        dest: str,
        filepath: str,
        target: str,
        timeout: int = setting.EXECUTE_TIMEOUT,
        port: int = setting.AGENT_PORT,
        extra_args: list = [],
    ) -> dict:
        """
        Send file to endpoint to execute.

        :param dest: [str] target host address.
        :param filepath: [str] filepath to send.
        :param target: [str] target filepath.
        :param timeout: [int] timeout (default: 0).
        :param port: [int] target host port (default: 8086).
        :param extra_args: [list] extra args.
        :return: [dict] result
        """

        result = {}

        result["send_file_to_agent"] = Endpoint_Action.send_file_to_agent(
            dest, filepath, target, port
        )
        result["execute_file"] = Endpoint_Action.execute_file(
            dest, target, timeout, port, extra_args
        )

        return result

    @staticmethod
    def get_physical_file(
        dest: str, target: str, host_name: str, port: int = setting.AGENT_PORT
    ) -> None:
        """
        Get physical file.

        :param dest: [str] target host address.
        :param target: [str] target file.
        :param host_name: [str] target host name.
        :param port: [int] target host port (default: 8086).
        """

        Folder.check_and_make_folder(setting.DOWNLOAD_PATH)

        Logger.info(f"Get physical file at {dest}:{port} on `{target}`")
        url = rf"http://{dest}:{port}/get_physical_file?target={target}"

        content = ResponseMethod.get_json(url)

        decoded_content = base64.b64decode(content["file_base64"])
        file_name = host_name + "_" + content["filename"]
        file_path = os.path.join(setting.DOWNLOAD_PATH, file_name)

        with open(file_path, "wb") as file:
            file.write(decoded_content)

        Logger.info(f"Get physical file at {dest}:{port} on `{target}` success")

    @staticmethod
    def get_physical_folder_zip(
        dest: str, target: str, port: int = setting.AGENT_PORT
    ) -> None:
        """
        Get physical folder as ZIP.

        :param dest: [str] target host address.
        :param target: [str] target folder.
        :param port: [int] target host port (default: 8086).
        """
        Folder.check_and_make_folder(setting.DOWNLOAD_PATH)

        Logger.info(f"Getting physical folder as ZIP from {dest}:{port} for `{target}`")
        url = rf"http://{dest}:{port}/get_physical_folder_zip?target={target}"

        response = ResponseMethod.get_response(url)

        content_disposition = response.headers.get("Content-Disposition")
        if content_disposition and "filename=" in content_disposition:
            zip_filename = content_disposition.split("filename=")[-1].strip('"')
        else:
            zip_filename = "default_bond_get.zip"

        counter = 1
        base_filename, file_extension = os.path.splitext(zip_filename)
        while os.path.exists(zip_filename):
            zip_filename = f"{base_filename} ({counter}){file_extension}"
            counter += 1

        file_path = os.path.join(setting.DOWNLOAD_PATH, zip_filename)

        with open(file_path, "wb") as f:
            f.write(response.content)

        Logger.info(
            f"Successfully saved physical folder from {dest}:{port} as `{zip_filename}`"
        )
