"""
Library package to calculate simple interest

Typical usage example:

    simple_interest = calculate_simple_interest(100, 5, 2)
"""


def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest

    Args:
            principal (float): principal amount
            rate (float): interest rate
            time (int): time
    Returns:
            float: simple interest"""
    interest = (principal * rate * time) / 100
    return interest
