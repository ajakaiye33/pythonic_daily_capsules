
def population_growth(current, rate, target):
    """
    Receives an intial population, annual rate of growth, and target population
    Use a while loop to calculate how many years it takes to go over the target
    population and return it
    """
    number_of_yrs = 0
    if rate > 0:
        while current <= target:
            current *= (1+rate)
            number_of_yrs += 1
        return number_of_yrs
    return "invalid growth rate"


print(population_growth(5000, 0.1, 10000))
