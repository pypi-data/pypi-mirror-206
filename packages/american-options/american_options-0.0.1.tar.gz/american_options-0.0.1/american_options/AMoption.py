from scipy.stats import norm
import numpy as np


class Option:
    """
    Obtain value for options using various pricing methods.

    :param strike: Strike price of an option.
    :type strike: int
    :param spot: Current price of the underlying.
    :type spot: float
    :param volatility: Volatility of the underlying asset.
    :type volatility: float
    :param maturity: Time to maturity for the option.
    :type maturity: float
    """

    def __init__(self, strike, spot, volatility, maturity):
        self.strike = strike
        self.spot = spot
        self.volatility = volatility
        self.maturity = maturity

    def d1(self, r):
        """
        Get value of d1, used in european option pricing.

        :param r: Interest rate.
        :type r: float

        :return: Value of d1.
        :rtype: float
        """
        return (np.log(self.spot / self.strike) + (r + (self.volatility**2)/2) * self.maturity) \
            / (self.volatility * np.sqrt(self.maturity))

    def d2(self, r):
        """
        Get value of d2, used in european option pricing.

        :param r: Interest rate.
        :type r: float

        :return: Value of d1.
        :rtype: float
        """
        return self.d1(r) - self.volatility * np.sqrt(self.maturity)

    def european_call(self, r):
        """
        Get a price of European Call option using Black-Scholes formula.

        :param r: Interest rate.
        :type r: float

        :return: Price of European Call option.
        :rtype: float
        """
        return norm.cdf(self.d1(r)) * self.spot - norm.cdf(self.d2(r)) * self.strike * np.exp(- r * self.maturity)


if __name__ == '__main__':
    test = Option(100, 100, 0.25, 1)
    print(test.european_call(0.05))
