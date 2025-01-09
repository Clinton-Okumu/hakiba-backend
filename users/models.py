from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql import func
from app.database import Base
from passlib.context import CryptContext
from sqlalchemy.orm import relationship

#password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    id_number = Column(String, unique=True, index=True, nullable=False)
    pin = Column(String(4), nullable=False)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(String, default=func.now())
    updated_at = Column(String, default=func.now(), onupdate=func.now())

    # Relationship to Customer
    customer = relationship("Customer", back_populates="user", uselist=False)

    def set_pin(self, raw_pin: str):
        if not raw_pin:
            raise ValueError("Pin cannot be empty")
        if len(raw_pin) != 4:
            raise ValueError("Pin must be 4 characters long")
        self.pin = pwd_context.hash(raw_pin)

    def check_pin(self, raw_pin: str) -> bool:
        return pwd_context.verify(raw_pin, self.raw_pin)

    def set_password(self, password: str):
        if not password:
            raise ValueError("Password is required")
        self.password = pwd_context.hash(password)
    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

