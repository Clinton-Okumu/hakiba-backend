from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    full_name: str
    phone_number: str
    pin: str
    id_number: str

    @field_validator("pin")
    def validate_pin(cls, v):
        if len(v) != 4:
            raise ValueError("PIN must be exactly 4 characters long.")
        return v

class SuperuserCreate(BaseModel):
    full_name: str
    password: str
