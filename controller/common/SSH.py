# -*- coding:utf-8 -*-
import time
import paramiko


class SSH:
    """
    SSH Client
    """

    def __init__(
        self, dest: str, key: str = None, username: str = None, password: str = None
    ):
        """
        init SSH client

        :param dest: [str] target host address
        :param key: [str] private key file path (default: None)
        :param username: [str] SSH username (default: None)
        :param password: [str] SSH password (default: None)
        """
        self.dest = dest
        self.key = key
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()

    def __enter__(self) -> paramiko.SSHClient:
        """
        Enter SSH context manager.

        :return: [paramiko.SSHClient] SSHClient object
        """
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if self.key:
            self.client.connect(
                self.dest, key_filename=self.key, username=self.username
            )
        else:
            self.client.connect(
                self.dest, username=self.username, password=self.password
            )

        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close SSH connection.
        """
        self.client.close()

    def close(self) -> None:
        """
        Close SSH connection.
        """
        self.__exit__(None, None, None)

    def execute_commands(self, commands: list) -> str:
        """
        Execute commands on remote host.

        :param commands: [list] command list (ex: ["ls", "pwd"])
        :return: [str] command output
        """
        command_string = " && ".join(commands)
        _, stdout, _ = self.client.exec_command(command_string)
        output = stdout.read().decode("utf-8")

        return output


class InteractiveSSH:
    """
    Interactive SSH Client
    """

    def __init__(
        self, dest: str, key: str = None, username: str = None, password: str = None
    ):
        """
        Initialize Interactive SSH client.

        :param dest: [str] target host address
        :param key: [str] private key file path
        :param username: [str] SSH username (default: None)
        :param password: [str] SSH password (default: None)
        """
        self.dest = dest
        self.key = key
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()

    def __enter__(self) -> paramiko.Channel:
        """
        Enter SSH interactive context manager.

        :return: [paramiko.Channel] Channel (interactive shell session) object
        """
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.key:
            self.client.connect(
                self.dest, key_filename=self.key, username=self.username
            )
        else:
            self.client.connect(
                self.dest, username=self.username, password=self.password
            )

        return self.client.invoke_shell()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close SSH connection.
        """
        self.client.close()

    def close(self) -> None:
        """
        Close SSH connection.
        """
        self.__exit__(None, None, None)

    @staticmethod
    def send_command(
        dest: str,
        key: str = None,
        username: str = None,
        password: str = None,
        command: str = "",
    ) -> str:
        """
        Send a command in the interactive SSH session.

        :param dest: [str] target host address
        :param key: [str] private key file path (default: None)
        :param username: [str] SSH username (default: None)
        :param password: [str] SSH password (default: None)
        :param command: [str] The command to be executed
        :return: [str] command output
        """

        with InteractiveSSH(dest, key, username, password) as shell:
            shell.send(command + "\n")

            time.sleep(60)

            output = shell.recv(2048).decode("utf-8")

        return output


class SFTP:
    """
    SFTP client
    """

    def __init__(
        self, dest: str, key: str = None, username: str = None, password: str = None
    ):
        """
        init SFTP client

        :param dest: [str] target host address
        :param key: [str] private key file path (default: None)
        :param username: [str] SSH username (default: None)
        :param password: [str] SSH password (default: None)
        """
        self.dest = dest
        self.key = paramiko.RSAKey.from_private_key_file(key) if key else None
        self.username = username
        self.password = password
        self.transport = None
        self.client = None

    def __enter__(self) -> paramiko.SFTPClient:
        """
        Enter SFTP context manager.

        :return: [paramiko.SFTPClient] SFTPClient object
        """
        self.transport = paramiko.Transport((self.dest, 22))

        if self.key:
            self.transport.connect(username=self.username, pkey=self.key)
        else:
            self.transport.connect(username=self.username, password=self.password)

        self.client = paramiko.SFTPClient.from_transport(self.transport)

        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close SFTP connection.
        """
        if self.client:
            self.client.close()
        if self.transport:
            self.transport.close()

    def close(self) -> None:
        """
        Close SFTP connection.
        """
        self.__exit__(None, None, None)

    def upload_file(self, local_path: str, remote_path: str) -> None:
        """
        Upload file to remote host.

        :param local_path: [str] local file path (ex: ./test.txt)
        :param remote_path: [str] remote file path (ex: /home/sonar/test.txt)
        """
        self.client.put(local_path, remote_path)
