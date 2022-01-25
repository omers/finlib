import pytest


def test_import(import_lib):
    data = import_lib
    assert data


# @pytest.mark.skip(reason="no way of currently testing this")
def test_get_stock_dataframe_shape(import_lib):
    STOCK = "AAPL"
    START = 2020
    END = 2022
    data = import_lib
    df = data.get_stock(STOCK, START, END)
    assert df.shape == (505, 19)
