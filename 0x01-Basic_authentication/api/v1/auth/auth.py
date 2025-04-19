#!/usr/bin/env python3
""" Authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for all authentication systems"""
    def require_auth(self, path: str, excluded_paths:  List[str]) -> bool:
        """ Checks if the path requires authentication
        Args:
            path (str): the path to check
            excluded_paths (list[str]): list of excluded paths
        Returns:
            bool: True if the path requires authentication, False otherwise
            But for now it will onl return False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header from the request
        Args:
            request: the request object
        Returns:
            str: the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None"""
        return None
