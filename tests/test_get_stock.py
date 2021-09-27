STOCK = "FB"
START = 2020
END = 2021


def test_import(import_lib):
    data = import_lib
    assert data


def test_get_stock_dataframe_shape(import_lib):
    data = import_lib
    df = data.get_stock(STOCK, START, END)
    assert df.shape == (253, 16)
