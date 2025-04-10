from flask_sqlalchemy import SQLAlchemy
from app.customer.dao import CustomerDAO
from app.models.models import Customer
from app.customer.dto import CustomerDTO


class CustomerService:
    def __init__(self, db: SQLAlchemy):
        self.dao = CustomerDAO(db)

    def create(self, customer_dto: CustomerDTO, id: int) -> tuple[dict | None, int]:
        new_customer = Customer(id=id, budget=customer_dto.budget)
        registered_customer = self.dao.create(new_customer)
        return registered_customer.to_dict(), 201

    def get_all(self) -> tuple[list, int]:
        return [customer.to_dict() for customer in self.dao.get_all(Customer)], 200

    def get_customer_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        customer = self.dao.get(Customer, id)
        if not customer:
            return None, 404
        return customer.to_dict(), 200

    def delete_customer_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(Customer, id)
        return "User deleted successfully", 204

    def update_customer_by_id(self, id: int, customer_dto: CustomerDTO) -> tuple[dict, int]:
        updated_customer = self.dao.update(
            model=Customer,
            new_object=Customer(budget=customer_dto.budget),
            object_id=id
        )
        return updated_customer.to_dict(), 200
