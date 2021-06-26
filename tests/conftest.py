import pytest
from src.finpredict import FinData
import os


@pytest.fixture(scope="session", autouse=True)
def import_lib():
    data = FinData()
    yield data