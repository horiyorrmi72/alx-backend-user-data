#!/usr/bin/env python3
"""
This module handles session authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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
