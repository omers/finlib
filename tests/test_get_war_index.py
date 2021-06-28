def test_import(import_lib):
    data = import_lib
    assert data


def test_get_stock_dataframe_shape(import_lib):
    data = import_lib
    df = data.get_war_index("2020", "2021")
    assert df.shape == (253, 6)
