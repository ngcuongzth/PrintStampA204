import time
import os
from qfluentwidgets import InfoBar, InfoBarPosition
from PyQt5.QtCore import Qt
import re
from dotenv import load_dotenv
import os


load_dotenv()
path_logs = "./data/logs/"
path_config = "./configs/config.ini"
path_configApp = "./configs/configApp.ini"
CHECK_DATA_URL = os.getenv("CHECK_DATA_URL")
INSERT_DATA_URL = os.getenv("INSERT_DATA_URL")

# auto create folder logs if it doesn't exist

if not os.path.exists(path_logs):
    os.makedirs(path_logs)


def createLog(msg, type, logType):
    """Insert log to file"""
    try:
        data = str(msg.encode("utf-8"))
        if type == "DT":
            pathLog = path_logs + "LogData_" + time.strftime("%Y%m%d") + ".log"
        elif type == "IMG":
            pathLog = path_logs + "LogImage_" + time.strftime("%Y%m%d") + ".log"
        else:
            pathLog = path_logs + "LogDB_" + time.strftime("%Y%m%d") + ".log"
        with open(pathLog, "a") as file:
            if logType == "info":
                file.write(time.strftime("%H:%M:%S") + " - INFO - " + data + "\n")
            if logType == "E":
                file.write(time.strftime("%H:%M:%S") + " - ERROR - " + data + "\n")
            if logType == "war":
                file.write(time.strftime("%H:%M:%S") + " - WARNING - " + data + "\n")
    except Exception as e:
        print(
            "-->>>" + time.strftime("%Y%m%d_%H_%M_%S") + ": ERROR LogEvent: ",
            e,
            "--Data: ",
            data,
        )


def createInfoBar(ref, title, msg, type):
    if type == "0":
        InfoBar.error(
            title,
            msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,
            parent=ref,
        )
    elif type == "1":
        InfoBar.success(
            title,
            msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,
            parent=ref,
        )

    elif type == "2":
        InfoBar.warning(
            title,
            msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,
            parent=ref,
        )
    elif type == "3":
        InfoBar.info(
            title,
            msg,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,
            parent=ref,
        )


def is_can_cvt_float(value):
    if not isinstance(value, str):
        value = str(value)
    pattern = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"
    if re.match(pattern, value):
        return True
    else:
        return False


def is_can_cvt_int(value):
    pattern = r"^\d+$"
    if re.match(pattern, value):
        return True
    else:
        return False


def validate_DATE_CODE(date_string: str, type: str):
    if type == "YYMMDD" or type == "yymmdd":
        pattern = r"^\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$"
        return bool(re.match(pattern, date_string))
    elif type == "YYYYMMDD" or type == "yyyymmdd":
        pattern = r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$"
        return bool(re.match(pattern, date_string))


stepcodes = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

print(len(stepcodes))
