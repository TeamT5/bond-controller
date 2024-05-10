import sys


class CHECK_SYSTEM:
    class SYSTEM:
        AIX = "aix"
        LINUX = "linux"
        WINDOWS = "win32"
        WINDOWS_CYGWIN = "cygwin"
        MAC = "darwin"

    class SYSTEM_NAME:
        WINDOWS = "Windows"
        LINUX = "Linux"
        MAC = "Mac"
        WINDOWS_CYGWIN = "Cygwin"
        AIX = "AIX"

    SYSTEM_CHART = {
        SYSTEM.AIX: "AIX",
        SYSTEM.LINUX: "Linux",
        SYSTEM.WINDOWS: "Windows",
        SYSTEM.WINDOWS_CYGWIN: "Cygwin",
        SYSTEM.MAC: "Mac",
    }

    OS_VERSION = sys.platform
    OS_NAME = SYSTEM_CHART[OS_VERSION]
