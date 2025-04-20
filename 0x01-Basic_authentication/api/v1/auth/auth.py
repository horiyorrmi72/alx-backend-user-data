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
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False
        return True

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
