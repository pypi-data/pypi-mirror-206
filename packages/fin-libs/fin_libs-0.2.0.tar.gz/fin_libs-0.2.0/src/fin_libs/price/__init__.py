"""
Module to calculate stock price ratios

Typical usage example:

    apple_pe = calculate_price_to_earning("AAPL")
    apple_pbv = calculate_price_to_book_value("AAPL")
"""
import yfinance as yf


def calculate_price_to_earning(ticker):
    """
    Calculate Price to Earnings Ratio (P/E)

    Args:
            ticker (str): the ticker for which we should calculate the ratio
    Returns:
            float: the ratio"""
    tick = yf.Ticker(ticker)
    return tick.info['forwardPE']


def calculate_price_to_book_value(ticker):
    """
    Calculate Price to Book Value Ratio (P/BV)

    Args:
            ticker (str): the ticker for which we should calculate the ratio
    Returns:
            float: the ratio"""
    tick = yf.Ticker(ticker)
    return tick.info['bookValue']
