#!/usr/bin/env python3
""" Authentication related module"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Hash a password using bcrypt and return the hashed password"""
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_password.decode('utf-8')


def _generate_uuid() -> str:
    """this generate and return a string representation
    of a new uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the provided email and password"""
        if not email or not password:
            raise ValueError("Email and password are required")
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password=password)
            return self._db.add_user(email=email,
                                     hashed_password=hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """validates user credentials"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password.encode('utf-8'))
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """check for user with the provided email
        and generate new session id for user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user_new_session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=user_new_session_id)
                return user_new_session_id
        except NoResultFound:
            return

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Get a user based on a given session_id.
        Args:
        session_id (str): The session ID to search for.
        Returns:
        User | None: The User object if found, otherwise None.
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                return None
        return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a user's session by setting session_id to None"""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset password token for the user"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User DNE")

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token
