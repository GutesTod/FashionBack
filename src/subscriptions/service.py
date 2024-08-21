from fastapi import Depends
from ..base import BaseService, get_session
from sqlalchemy.orm import Session
from .model import User


class UserService(BaseService[User]):
    def __init__(self, db_session: Session):
        super(UserService, self).__init__(User, db_session)


def get_users_service(
    db_session: Session = Depends(get_session),
) -> UserService:
    return UserService(db_session)