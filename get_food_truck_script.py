from datetime import datetime
import pytz
from food_truck import FoodTruck
import sys


page = 0 if len(sys.argv) == 1 else int(sys.argv[1])
def get_food_trucks_in_san_francisco_open_now(page):
    PST = pytz.timezone('US/Pacific')
    datetime_PST = datetime.now(PST)
    current_weekday = datetime_PST.strftime('%A')
    current_time = datetime_PST.strftime("%H:%M")

    print(f"Current time in San Francisco is {current_weekday}, {current_time}")

    food_trucks = FoodTruck.get_food_trucks(current_weekday, current_time, page)
    return food_trucks

food_trucks = get_food_trucks_in_san_francisco_open_now(page)
if page == 0 and not food_trucks:
    print('There are no food_trucks opened right now, please wait a bit.')
elif not food_trucks:
    print('There are no food_trucks in the current page, go back to previous page')
else:
    print('NAME; ADDRESS')
    for food_truck in food_trucks:
        print(f"{food_truck.name}; {food_truck.address}")
    print()
    print(f"current page {page}, go to the next page by inputting argument {page+1}")
