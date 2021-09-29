import pytest
from src.finpredict import FinData
import time

@pytest.fixture(scope="module", autouse=True)
def import_lib():
    data = FinData()
    yield data
