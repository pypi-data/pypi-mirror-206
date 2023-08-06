"""
Library module to compute dividend information

Typical usage example:

        aapl_dr = calculate_dividend_rate("AAPL")
"""
import yfinance as yf


def calculate_dividend_rate(ticker):
    """
    Calculate dividend rate

    Args:
            ticker (str): name of the ticker
    Returns:
            float: dividend rate
    """
    tick = yf.Ticker(ticker)
    return tick.info['dividendRate']


def calculate_dividend_yield(ticker):
    """
    Calculate dividend yield

    Args:
            ticker (str): name of the ticker
    Returns:
            float: dividend yield
    """
    tick = yf.Ticker(ticker)
    return tick.info['dividendYield']
