from customers.repository import CustomerRepository

class CustomerService:
    @staticmethod
    def create_customer(db, phone_number: str, full_name: str, user_id: int):
        """
        Create a new customer.
        """
        return CustomerRepository.create_customer(db, phone_number, full_name, user_id)

    @staticmethod
    def get_customer(db, customer_id: int):
        """
        Retrieve a customer by ID.
        """
        return CustomerRepository.get_customer(db, customer_id)

    @staticmethod
    def update_customer(db, customer_id: int, phone_number: str = None, full_name: str = None):
        """
        Update a customer's details.
        """
        return CustomerRepository.update_customer(db, customer_id, phone_number, full_name)

    @staticmethod
    def delete_customer(db, customer_id: int):
        """
        Delete a customer by ID.
        """
        return CustomerRepository.delete_customer(db, customer_id)
