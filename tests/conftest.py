import pytest
from src.finpredict import FinData
import time
import warnings


@pytest.fixture(scope="module", autouse=True)
def import_lib():
    data = FinData()
    yield data
