def test_import(import_lib):
    data = import_lib
    assert data


def test_get_currencies_dataframe_shape(import_lib):
    data = import_lib
    df = data.get_currencies("01-01-2022", "01-02-2023")
    assert df.shape == (261, 9)
