from typing import Generic, Type, TypeVar, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_model import OrmBase
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy import update, delete

ModelType = TypeVar("ModelType", bound=OrmBase)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.table = model
        self.db_session = db_session

    async def get_list(self, limit: Optional[int] = None):
        query = await self.db_session.execute(
            select(self.table).limit(limit).order_by(-self.table.id.desc())
        )
        return query.scalars().all()

    async def get_one(self, id):
        id_item = await self.db_session.execute(
            select(self.table).filter(self.table.id == id)
        )
        id_item = id_item.scalar()
        if not id_item:
            raise HTTPException(status_code=404, detail="Page is not found")
        return id_item

    async def create(self, data):
        item = self.table(**data.dict())
        self.db_session.add(item)
        await self.db_session.commit()
        return item

    async def update(self, data, id):
        await self.db_session.execute(
            update(self.table).
            filter(self.table.id == id).
            values(**data)
        )
        await self.db_session.commit()
        return await self.get_one(data.id)

    async def delete(self, id):
        query = await self.db_session.execute(
            delete(self.table).filter(self.table.id == id)
        )
        await self.db_session.commit()
        return query.all()