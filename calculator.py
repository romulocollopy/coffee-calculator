from decimal import Decimal
GRAMS_PER_SPOON = 4.0
GRAMS_PER_CUP = 5.3


def get_amount_of_coffee_spoons(number_of_cups):
    """
    Returns the total of spoons you have to
    add on the machine.
    >>> get_amount_of_coffee_spoons(10)
    13.25

    Params
    ------
        number_of_cups - integer
            Total of cups you'd like to serve
    Returns
    -------
        float
            Number of spoons
    """
    return round(Decimal(3 * GRAMS_PER_CUP / GRAMS_PER_SPOON)*2)/2
