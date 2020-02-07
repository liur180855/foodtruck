from datetime import datetime
import pytz
from food_truck import FoodTruck
import sys


page = 0 if len(sys.argv) == 1 else sys.argv[1]
PST = pytz.timezone('US/Pacific')
datetime_PST = datetime.now(PST)
current_weekday = datetime_PST.strftime('%A')
current_time = datetime_PST.strftime("%H:%M")

print(f"Current time in San Francisco is {current_weekday}, {current_time}")

result = FoodTruck.get_food_trucks(current_weekday, current_time, page)

if page == 0 and not result:
    print('There are no foodtrucks opened right now, please wait a bit.')
elif not result:
    print('There are no foodtrucks in the current page, go back to previous page')
else:
    print('NAME; ADDRESS')
    for foodtruck in result:
        print(f"{foodtruck.name}; {foodtruck.address}")
    print()
    print(f"current page {page}, go to the next page by inputting argument '{page+1}'")
