from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import User


class CategoryService(BaseService[User]):
    def __init__(self, db_session: Session):
        super(CategoryService, self).__init__(User, db_session)


def get_category_service(
    db_session: Session = Depends(get_session),
) -> CategoryService:
    return CategoryService(db_session)