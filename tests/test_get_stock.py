import pytest


def test_import(import_lib):
    data = import_lib
    assert data


#@pytest.mark.skip(reason="Yahoo finance broke the API")
def test_get_stock_dataframe_shape(import_lib):
    STOCK = "AAPL"
    START = 2020
    END = 2022
    data = import_lib
    df = data.get_stock(STOCK)
    assert df.shape == (len(df. index), 21)
