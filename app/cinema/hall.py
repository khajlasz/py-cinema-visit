from app.people.cinema_stuff import Cleaner
from app.people.customer import Customer


class CinemaHall():
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f"Movie {movie_name} started in hall {self.hall_number}")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie {movie_name} finished in hall {self.hall_number}")
        cleaning_staff.clean_hall(self.hall_number)
