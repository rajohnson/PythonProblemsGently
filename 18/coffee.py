def get_cost_of_coffee(number_coffees: int, price: float) -> float:
    """
    Calculate cost of bill at coffee shop with a buy 8 get 1 free deal.
    """
    free_coffees = number_coffees // 9
    cost = (number_coffees - free_coffees) * price
    return cost
