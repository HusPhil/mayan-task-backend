from uuid import uuid4
from sqlalchemy import Column, DateTime, SmallInteger, String, Text, Uuid

from app.core.database import Base
from app.core.enums import TaskStatus
from app.utils.time_utils import get_utc_now


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Uuid, primary_key=True, default=uuid4, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    status = Column(
        SmallInteger,
        default=TaskStatus.INCOMPLETE,
        nullable=False,
        index=True,
    )
    created_at = Column(DateTime(timezone=True), default=get_utc_now, nullable=False)
