from app.people.customer import Customer


class CinemaBar():
    def __init__(self) -> None:
        pass

    def sell_product(self, customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}")
