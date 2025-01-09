from pydantic import BaseModel

class CustomerCreate(BaseModel):
    phone_number: str
    full_name: str
    user_id: int

class CustomerUpdate(BaseModel):
    phone_number: str | None = None
    full_name: str | None = None

class CustomerResponse(BaseModel):
    id: int
    phone_number: str
    full_name: str
    user_id: int

    class Config:
        from_attributes = True  # Enable ORM mode
