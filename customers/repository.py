from sqlalchemy.orm import Session
from .models import Customer

class CustomerRepository:
    @staticmethod
    def create_customer(db: Session, phone_number: str, full_name: str, user_id: int):
        """
        Create a new customer.
        """
        customer = Customer(
            phone_number=phone_number,
            full_name=full_name,
            user_id=user_id,
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def get_customer(db: Session, customer_id: int):
        """
        Retrieve a customer by ID.
        """
        return db.query(Customer).filter(Customer.id == customer_id).first()

    @staticmethod
    def update_customer(db: Session, customer_id: int, phone_number: str = None, full_name: str = None):
        """
        Update a customer's details.
        """
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer:
            return None

        if phone_number:
            customer.phone_number = phone_number
        if full_name:
            customer.full_name = full_name

        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        """
        Delete a customer by ID.
        """
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer:
            return False

        db.delete(customer)
        db.commit()
        return True
