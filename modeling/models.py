"""Model."""
import functools
from typing import Final

import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin

PRODUCTS: Final = {
    "apples-red": (3, 1),  # mean and standard deviation
    "apples-green": (2.5, 0.5),
    "bananas": (2, 0.5),
    "bananas-organic": (2.5, 0.5),
    "broccoli": (4, 1),
    "rice": (2, 1),
    "wine": (6.5, 3),
    "cheese": (4, 2),
    "beef": (10, 2),
    "avocado": (1.5, 0.25),
}


def vectorized(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        vectorized_func = np.vectorize(func)
        return vectorized_func(*args, **kwargs)

    return wrapper


class SimpleRegression(BaseEstimator, RegressorMixin):
    def __init__(self):
        ...

    def fit(self, X, y):
        """Fit the function."""
        return self

    @vectorized
    def get_price(self, product: str) -> float:
        """Get the price based on the product.

        Args:
            product (str): Product (for example apples-red, apples-green)

        Returns:
            float: Price in euro's
        """
        mean, standard_deviation = PRODUCTS[product]
        return np.random.normal(mean, standard_deviation)

    def predict(self, X) -> np.array(float):
        """Predict the product price based only on the products"""
        return self.get_price(X)
