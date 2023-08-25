#!/usr/bin/env python3
"""Module Regex-ing - handling user data"""
from typing import List
import logging
from os import environ
import re
import mysql.connector

PII_FIELDS = ('name', 'password', 'phone', 'ssn', 'email')


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str
        ) -> str:
    """returns the log message obfuscated"""

    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator, message)
    return message
