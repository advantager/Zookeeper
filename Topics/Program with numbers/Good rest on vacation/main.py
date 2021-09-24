# put your python code here
duration = abs(int(input()))
food_day_cost = abs(int(input()))
flight_way_cost = abs(int(input()))
hotel_night_cost = abs(int(input()))
print(duration * food_day_cost
      + (2 * flight_way_cost)
      + ((duration - 1) * hotel_night_cost))
