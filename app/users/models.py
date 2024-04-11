
from app.app.db import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass