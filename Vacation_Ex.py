
# Write a function called answer that takes no arguments and returns the value 42.
def answer():
    return 42
	
# Define a function called hotel_cost with one argument nights as input.
# The hotel costs $140 per night. So, the function hotel_cost should return 140*nights.
def hotel_cost(nights):
    return 140*nights
	
# Define a function called plane_ride_cost that takes a string, city, as input. The function 
# should return a different price depending on the location.
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
		
# Define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car:
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
		
# Below your existing code, define a function called trip_cost that takes two arguments, city and days.
# Have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) 
# functions. It is completely valid to call the hotel_cost(nights) function with the variable days.
def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)

######

# Modify your trip_cost function definition. Add a third argument, spending_money.
# Modify what the trip_cost function does. Add the variable spending_money to the sum that it returns. 
# Print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
        
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	
print trip_cost("Los Angeles", 5, 600)




