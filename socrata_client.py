from sodapy import Socrata
import configparser


class SocrataClient:
    LOOP_SIZE = 10

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config")
        socrata_domain = config.get('Socrata', 'socrata_domain')
        socrata_token = config.get('Socrata', 'socrata_token')

        self.food_truck_endpoint = config.get('Socrata', 'food_truck')
        self.client = Socrata(socrata_domain, socrata_token)

    def get_food_truck_in_alphabetical_order(self, weekday_opened: str, time_opened: str, page: int = 0) -> list:
        where_clause = f"dayofweekstr = '{weekday_opened}' " \
                       f"and start24 <= '{time_opened}' " \
                       f"and '{time_opened}' <= end24"

        return self.client.get(self.food_truck_endpoint, limit=self.LOOP_SIZE, offset=self.LOOP_SIZE * page,
                               select="applicant, location, start24, end24, dayofweekstr", order="applicant ASC",
                               where=where_clause)
