from services.chat_service.models.message import MessageStatus
from sqlalchemy import Integer, String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
from services.chat_service.db.database import db
from datetime import datetime

class MessageTable(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    message_body: Mapped[String] = mapped_column(String(255))
    sender_id: Mapped[int] = mapped_column(Integer)
    chat_id: Mapped[int] = mapped_column(Integer)
    message_status: Mapped[MessageStatus]= mapped_column(Enum(MessageStatus))
    send_time: Mapped[datetime]= mapped_column(DateTime)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

#Base.metadata.create_all(engine)
