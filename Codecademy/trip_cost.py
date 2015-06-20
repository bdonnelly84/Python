def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days < 3:
        return 40 * days
    elif days >= 3 and days < 7:
        return (40 * days) - 20
    elif days >= 7:
        return (40 * days) - 50

def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money
