from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import Notification


class NotificationsService(BaseService[Notification]):
    def __init__(self, db_session: Session):
        super(Notification, self).__init__(Notification, db_session)


def get_advertisement_service(
    db_session: Session = Depends(get_session),
) -> NotificationsService:
    return NotificationsService(db_session)