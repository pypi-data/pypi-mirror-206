"""
Library module to compute earnings per share

Typical usage example:

        aapl_eps = calculate_eps("AAPL")
"""
import yfinance as yf


def calculate_eps(ticker):
    """
    Calculate Earnings per Share

    Args:
            ticker (str): the ticker for which we should calculate the EPS
    Returns:
            float: the EPS"""
    tick = yf.Ticker(ticker)
    return tick.info['forwardEps']
