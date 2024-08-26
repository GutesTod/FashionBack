from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import Service


class Service(BaseService[Service]):
    def __init__(self, db_session: Session):
        super(Service, self).__init__(Service, db_session)


def get_service(
    db_session: Session = Depends(get_session),
) -> Service:
    return Service(db_session)