"""
Library package to compute the weighted average

Typical usage example:

    weighted_avg = compute_weighted_average("data.csv", "values", "weights")
"""
import numpy
import pandas


def compute_weighted_average(csv_file_path, distr_col, weights_col):
    """
    Compute weighted average

    Args:
            csv_file_path (str): file path string
            distr_col (str): column name for distribution
            weights_col (str): column name for weights
    Returns:
            int: weighted average"""
    df = pandas.read_csv(csv_file_path)
    distribution = df[distr_col]
    weights = df[weights_col]
    return _compute_weighted_average(distribution, weights)


def _compute_weighted_average(distribution, weights):
    """
    Helper function to calculate weighted average

    Args:
            distribution (list): list of values
            weights (list): weights for each value
    Returns:
            int: weighted average"""
    return numpy.average(distribution, weights=weights)
