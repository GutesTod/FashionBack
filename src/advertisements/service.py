from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import Advertisement


class AdvertisementsService(BaseService[Advertisement]):
    def __init__(self, db_session: Session):
        super(AdvertisementsService, self).__init__(Advertisement, db_session)


def get_advertisement_service(
    db_session: Session = Depends(get_session),
) -> AdvertisementsService:
    return AdvertisementsService(db_session)