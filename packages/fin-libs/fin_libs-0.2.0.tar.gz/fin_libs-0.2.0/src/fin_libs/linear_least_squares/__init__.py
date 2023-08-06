"""
Library package to compute linear least squares regression

Typical usage example:

    x, y, y_pred = do_linear_least_squares_regression("data.csv")
    plot_linear_least_squares_regression(x, y, y_pred, "red")
"""
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def do_linear_least_squares_regression(csv_file_path):
    """
    Does linear least squares regression

    Args:
            csv_file_path (string): file path where data is located
    Returns:
           int: x coefficient
           int: y coefficient
           int: y predictor coefficient
    """
    df = pandas.read_csv(csv_file_path)
    x = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values.reshape(-1, 1)
    lr_helper = LinearRegression()
    lr_helper.fit(x, y)
    y_pred = lr_helper.predict(x)
    return x, y, y_pred


def plot_linear_least_squares_regression(x, y, y_pred, color='yellow'):
    """
    Plots chart of linear least squares regression

    Args:
           x (int): x coefficient
           y (int): y coefficient
           y_pred (int): y predictor coefficient
           color (string, optional): color
    Returns:
           None
    """
    plt.scatter(x, y)
    plt.plot(x, y_pred, color=color)
    plt.show()
