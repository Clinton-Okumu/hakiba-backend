from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from app.database import get_db

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.
    """
    try:
        return services.CustomerService.create_customer(
            db,
            phone_number=customer.phone_number,
            full_name=customer.full_name,
            user_id=customer.user_id,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{customer_id}", response_model=schemas.CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a customer by ID.
    """
    customer = services.CustomerService.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=schemas.CustomerResponse)
def update_customer(
    customer_id: int,
    customer: schemas.CustomerUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a customer's details.
    """
    updated_customer = services.CustomerService.update_customer(
        db,
        customer_id=customer_id,
        phone_number=customer.phone_number,
        full_name=customer.full_name,
    )
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a customer by ID.
    """
    if not services.CustomerService.delete_customer(db, customer_id):
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}
