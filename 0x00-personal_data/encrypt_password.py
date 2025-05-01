#!/usr/bin/env python3
"""
This module encrypt user password
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """This hash user password and return salted"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function compare the provided plain password
    with the password stored in DB and returns true if match
    and false otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
