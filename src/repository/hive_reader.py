#!/bin/env python


import logging
import json
import os
import sys
import copy


class HiveReader(object):
    def __init__(self):
        self._init_reader()

    def _init_reader(self):
        self._logger = logging.getLoggerClass()
        self._logger.error("Could not initialize hive")

    def read_status(self):
        self._logger.error("Called read_status method")
        return "Connected unsuccessfully"
