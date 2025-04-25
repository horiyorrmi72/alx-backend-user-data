#!/usr/bin/env python3
"""
This module handles session authentication with expiration.
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import timedelta, datetime


class SessionDBAuth(SessionExpAuth):
    """
    Session authentication with database storage for sessions.
    """

    def create_session(self, user_id=None):
        """
        Create and store a session in the database.
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieve the user ID from the database using the session ID.
        """
        if session_id is None:
            return None
        session = UserSession.get(session_id=session_id)
        if not session:
            return None
        if self.session_duration is None or self.session_duration == 0:
            return session.user_id
        if session.created_at + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None
        return session.user_id

    def destroy_session(self, request=None):
        """
        Destroy the session based on the session ID in the request cookie.
        """
        session_id = self.session_id_from_request(request)
        if session_id:
            session = UserSession.get(session_id=session_id)
            if session:
                session.delete()
