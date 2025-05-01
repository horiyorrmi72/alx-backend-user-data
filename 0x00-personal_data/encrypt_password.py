#!/usr/bin/env python3
"""
This module encrypt user password
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """This hash user password and return salted"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
