# -*- coding:utf-8 -*-
import uuid

from controller.common.SSH import SSH, SFTP
from controller.common.logger.info_logger_handle import Logger


class Server_Action:
    @staticmethod
    def only_update_binary_on_remote_server(
        dest: str, filepath: str, target: str, key: str
    ) -> dict:
        """
        Only update binary to remote server.

        :param dest: [str] target host address.
        :param filepath: [str] local binary file path.
        :param target: [str] target path on remote server.
        :param key: [str] private key file path.
        :return: [dict] result
        """
        result = {}

        with SSH(dest, key) as ssh, SFTP(dest, key) as sftp:
            unique_id = uuid.uuid4()
            target_remote_file = f"/tmp/remote{unique_id}"

            sftp.put(filepath, target_remote_file)
            Logger.info(f"Put {filepath} to {target_remote_file}")

            _, out_, err_ = ssh.exec_command(f"mv {target_remote_file} {target}")
            Logger.info(f"Move {target_remote_file} to {target}")

            result = {"out": out_.read(), "err": err_.read()}

        return result

    @staticmethod
    def execute_command(dest: str, key: str, command: str) -> dict:
        """
        Execute the provided command on remote server.

        :param dest: [str] target host address.
        :param key: [str] private key file path.
        :param command: [str] the command string to execute.
        :return: [str] result with stdout and stderr
        """
        result = {}

        with SSH(dest, key) as ssh:
            _, out_, err_ = ssh.exec_command(command)
            Logger.info(f"Executed command: {command}")
            result = {"out": out_.read(), "err": err_.read()}

        return result

    @staticmethod
    def delete_target_file(dest: str, target: str, key: str) -> dict:
        """
        delete binary on remote server.

        :param dest: [str] target host address.
        :param target: [str] target file path on remote server.
        :param key: [str] private key file path.
        :return: [dict] result
        """
        result = {}

        with SSH(dest, key) as ssh:
            _, out_, err_ = ssh.exec_command(f"rm {target}")
            Logger.info(f"rm {target}")

            result = {"out": out_.read(), "err": err_.read()}

        return result
