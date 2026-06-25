def calculate_budget(
    budget,
    travel_cost,
    hotel_cost,
    duration
):

    food_cost = duration * 500

    total_cost = (
        travel_cost +
        hotel_cost +
        food_cost
    )

    remaining_budget = (
        budget -
        total_cost
    )

    return {
        "food_cost": food_cost,
        "total_cost": total_cost,
        "remaining_budget": remaining_budget
    }
