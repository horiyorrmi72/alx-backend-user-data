#!/usr/bin/env python3
"""Module Regex-ing - handling user data"""
from typing import List
import logging
import os
import re
import mysql.connector
from mysql.connector.connection import MySQLConnection

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


def get_logger() -> logging.Logger:
    """returns get logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_Handler = logging.StreamHandler()
    stream_Handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_Handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format method """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super(RedactingFormatter,
                                  self).format(record), self.SEPARATOR)


def get_db() -> MySQLConnection:
    """
    function to connect securely to a MySQL database
    using environment variables.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
