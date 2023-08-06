"""
Library module to compute net income

Typical usage example:

        net_income = calculate_net_income("earnings.csv", "transactions")
"""
import pandas


def calculate_net_income(csv_file_path, col_name):
    """
    Calculate net income

    Args:
        csv_file_path(str): expect csv_file_path to have column with
                        positive and negative values for money in & out
        col_name(str): name of the column


    Returns:
        float: the net income
    """
    df = pandas.read_csv(csv_file_path)
    amounts = df[col_name]
    return sum(amounts)
