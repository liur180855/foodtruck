from socrata_client import SocrataClient


class FoodTruck:
    def __init__(self, name: str, address: str, start24: str, end24: str, weekday: str):
        self.name = name
        self.address = address
        self.start24 = start24
        self.end24 = end24
        self.weekday = weekday

    @staticmethod
    def get_food_trucks(current_weekday: str, current_time: str, page: int) -> list:
        Socrataclient = SocrataClient()
        food_trucks = Socrataclient.get_food_truck_in_alphabetical_order(weekday_opened=current_weekday,
                                                                         time_opened=current_time,
                                                                         page=page)
        result = []
        for food_truck in food_trucks:
            result.append(
                FoodTruck(food_truck['applicant'], food_truck['location'], food_truck['start24'],
                          food_truck['end24'], food_truck['dayofweekstr']))
        return result
