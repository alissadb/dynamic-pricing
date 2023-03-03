"""Models."""
import pandas as pd
from loguru import logger
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

from modeling.data import train_test_split


def train_model(data: pd.DataFrame) -> DummyRegressor:
    """Train a dummy model with the provided data.

    Args:
        data (pd.DataFrame): Data to use for training the model.

    Returns:
        DummyRegressor: DummyRegressor model using the median
    """
    logger.info("Train model...")
    X_train, X_test, y_train, y_test = train_test_split(data)

    linear_dummy_median = DummyRegressor(strategy="median")
    linear_dummy_median.fit(X_train, y_train)

    return linear_dummy_median
