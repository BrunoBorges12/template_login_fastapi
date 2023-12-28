from models.user import User
from sqlmodel import Session
from models.user import User, UserCreate, UserRead  # noqa: F811
from sqlmodel import select
from typing import Optional
from core.security import get_password_hash, verific_password_hash


class UserService:
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        query_user = select(User).where(User.email == email)
        results = db.exec(query_user).first()
        return results

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        create_user_db = User(
            email=user_data.email,
            name=user_data.name,
            password=get_password_hash(user_data.password),
        )
        db.add(create_user_db)
        db.commit()
        db.refresh(create_user_db)

        return create_user_db

    def user_authentication(self, db: Session, email: str, password: str) -> User:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verific_password_hash(password=password, hash_password=user.password):
            return None

        return user


user = UserService()
