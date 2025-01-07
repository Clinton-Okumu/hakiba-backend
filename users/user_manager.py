from .models import User
from app.database import SessionLocal

class UserManager:
    def create_user(self, full_name: str, phone_number: str, pin: str, id_number: str = None, **extra_fields):
        if not full_name:
            raise ValueError("Full name is required")
        if not phone_number:
            raise ValueError("Phone number is required")
        if not pin:
            raise ValueError("PIN is required for customers")

        db = SessionLocal()
        user = User(
            full_name=full_name,
            phone_number=phone_number,
            id_number=id_number,
            **extra_fields
        )
        user.set_pin(pin)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        return user

    def create_superuser(self, full_name: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not password:
            raise ValueError("Superusers must have a password")

        db = SessionLocal()
        user = User(full_name=full_name, **extra_fields)
        user.set_password(password)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        return user
