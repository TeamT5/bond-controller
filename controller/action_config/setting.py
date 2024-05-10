from controller.action_config.__version__ import __version__

DEBUG = False
VERSION = __version__

# *------ Agent Config ------*
AGENT_PORT = 8086
EXECUTE_TIMEOUT = 0  # 單位為秒

# *------ Download Config ------*
DOWNLOAD_PATH = "./Downloads"


# *----- All Logger Setting -----*
LOG_COLOR = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "red",
}

# *----- Server INFO Log Setting -----*
INFO_LOG_NAME = "Bond Controller"
INFO_LOG_SIZE = 1000  # 單位為 KB
INFO_LOG_LEVEL = "INFO"
INFO_LOG_PATH = "Logs"
INFO_LOG_FILE_NAME = "Bond_Controller_INFO_LOG.log"
INFO_LOG_BACKUP_COUNT = 5
INFO_LOG_MODE = "a"
INFO_LOG_ENCODING = "utf-8"
