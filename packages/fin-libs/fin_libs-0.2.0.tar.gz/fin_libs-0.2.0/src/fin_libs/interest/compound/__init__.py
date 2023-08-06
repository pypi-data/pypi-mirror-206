"""
Library package to calculate compound interest

Typical usage example:

    compound_interest = calculate_compound_interest(100, 5, 2)
"""


def calculate_compound_interest(principal, rate, time):
    """
    Calculate compound interest

    Args:
            principal (float): principal amount
            rate (float): interest rate
            time (int): time
    Returns:
            float: compound interest"""
    amount = principal * (pow((1 + rate / 100), time))
    interest = amount - principal
    return interest
