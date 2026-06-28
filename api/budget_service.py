def calculate_budget(budget, travel_cost, hotel_cost, duration):

    if (travel_cost + hotel_cost) > budget:
        travel_cost = int(budget * 0.30)
        hotel_cost = int(budget * 0.50)

    food_cost = int(budget * 0.20)

    total_cost = (
        travel_cost +
        hotel_cost +
        food_cost
    )

    remaining_budget = budget - total_cost

    return {
        "travel_cost": travel_cost,
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "total_cost": total_cost,
        "remaining_budget": remaining_budget
    }