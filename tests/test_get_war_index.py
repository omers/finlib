import pytest
def test_import(import_lib):
    data = import_lib
    assert data

@pytest.mark.skip(reason="Yahoo finance broke the API")
def test_get_stock_dataframe_shape(import_lib):
    data = import_lib
    df = data.get_war_index("01-01-2022", "01-02-2022")
    assert df.shape == (253, 6)
