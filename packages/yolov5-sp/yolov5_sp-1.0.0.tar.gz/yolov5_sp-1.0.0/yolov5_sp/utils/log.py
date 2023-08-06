# *_* coding : UTF-8 *_*
# 开发团队  ：  AHS-AI
# 开发人员  ：  shaop
# 开发时间  ：  2023/2/7  下午7:52
# 文件名称  :  log.PY
# 开发工具  :  PyCharm
# -*- coding:utf-8 -*-
import logging

import time

from logging.handlers import TimedRotatingFileHandler

base_formatter = "%(message)s"
INFO_FORMATTER = logging.Formatter(base_formatter)
WARN_FORMATTER = logging.Formatter(base_formatter + "-%(module)s")
ERROR_FORMATTER = logging.Formatter(base_formatter + "-%(filename)s")

# !/usr/bin/python
# coding=utf-8

import logging
import os


class Logger:
    def __init__(self, logName, logFile,
                 formatter="%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"):
        self._logger = logging.getLogger(logName)
        handler = TimedRotatingFileHandler(logFile, when='MIDNIGHT', backupCount=100, encoding="utf-8", delay=False,
                                           utc=False)
        formatter = logging.Formatter(formatter)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

        # Add stream for debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self._logger.addHandler(ch)

        self._logger.setLevel(logging.INFO)

    def log(self, msg):
        if self._logger is not None:
            self._logger.info(msg)


def archive_log(log_file_path):
    """
    only for small log file。Append write if new file already exists
    """
    if os.path.isfile(log_file_path):
        new_log_file_path = log_file_path + "-" + time.strftime("%Y%m%d")
        if os.path.isfile(new_log_file_path):
            with open(new_log_file_path, "ab") as new_file, open(log_file_path, "rb+") as old_file:
                for line in old_file:
                    new_file.write(line)
            try:
                os.remove(log_file_path)
            except (IOError, WindowsError):  # if file handler is in use, the overwrite it
                with open(log_file_path, "w") as old_file:
                    old_file.write("")
        else:
            try:
                os.rename(log_file_path, new_log_file_path)
            except (IOError, WindowsError):
                with open(log_file_path, "w") as old_file:
                    old_file.write("")


def create_file_handler(log_name, level=logging.DEBUG, formatter=INFO_FORMATTER):
    file_handler = logging.FileHandler(log_name)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    return file_handler


def create_TimedRotating_handler(log_name, level=logging.DEBUG, formatter=INFO_FORMATTER):
    timedrotating_handler = TimedRotatingFileHandler(log_name, when='MIDNIGHT', backupCount=100, encoding="utf-8",
                                                     delay=False, utc=False)
    timedrotating_handler.setLevel(level)
    timedrotating_handler.setFormatter(formatter)
    return timedrotating_handler


def create_stream_handler(level=logging.DEBUG, formatter=INFO_FORMATTER):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    return stream_handler


def generate_logger_handler(logger_name, is_stream_handler=True, is_file_handler=True,
                            add_error_log=True, log_level=logging.DEBUG, formatter=INFO_FORMATTER, log_path="."):
    handlers = []

    if is_file_handler:
        if log_path and not os.path.exists(log_path):
            os.makedirs(log_path)
        log_name = logger_name + ".log"
        log_file_path = os.path.join(log_path, log_name)
        archive_log(log_file_path)
        info_file_handler = create_TimedRotating_handler(log_file_path, level=log_level, formatter=formatter)
        handlers.append(info_file_handler)
        if add_error_log:
            error_log_name = logger_name + "-error.log"
            error_log_path = os.path.join(log_path, error_log_name)
            archive_log(error_log_path)
            error_file_handler = create_TimedRotating_handler(error_log_path, level=logging.ERROR,
                                                              formatter=ERROR_FORMATTER)
            handlers.append(error_file_handler)

    if is_stream_handler:
        stream_handler = create_stream_handler(level=log_level)
        handlers.append(stream_handler)

    return handlers


os.makedirs('logs', exist_ok=True)
Logger_process = Logger("app_process", "logs/app-process.log")
Logger_process_error = Logger("app_error", "logs/app-error.log")
