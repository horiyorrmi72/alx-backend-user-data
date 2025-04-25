from models.base import Base
from datetime import datetime


class UserSession(Base):
    """Model to store session information in the database (or file)."""

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
        self.created_at = datetime.now
        super().__init__(*args, **kwargs)
