from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.future import select

from ..base import BaseService, get_session
from .model import Salon



class SalonService(BaseService[Salon]):
    def __init__(self, db_session: Session):
        super(SalonService, self).__init__(Salon, db_session)
    async def get_one(self, id):
        id_item = await self.db_session.execute(
            select(self.table).filter(self.table.user_id == id)
        )
        id_item = id_item.scalar()
        if not id_item:
            raise HTTPException(status_code=404, detail="Page is not found")
        return id_item


def get_salon_service(
    db_session: Session = Depends(get_session),
) -> SalonService:
    return SalonService(db_session)