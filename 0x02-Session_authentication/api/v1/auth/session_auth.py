#!/usr/bin/env python3
"""
This module handles session authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """
    Session authentication class.
    """
    user_id_by_session_id = {}

    def generateSessionId(self):
        """
        Generate a new Session ID
        """
        return str(uuid4())

    def create_session(self, user_id: str = None) -> str:
        """
        This creates a session for the user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = self.generateSessionId()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        This will return user id based on session id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar(User):
        """
        Retrieve the User instance based on session cookie in the request
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_by_session_id.get(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logs out.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(request)
        if not user_id:
            return False

        del self.user_id_by_session_id[session_id]
        return True
