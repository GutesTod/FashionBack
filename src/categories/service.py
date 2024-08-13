from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import Category


class CategoryService(BaseService[Category]):
    def __init__(self, db_session: Session):
        super(CategoryService, self).__init__(Category, db_session)


def get_category_service(
    db_session: Session = Depends(get_session),
) -> CategoryService:
    return CategoryService(db_session)