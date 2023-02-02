import pytest
def test_import(import_lib):
    data = import_lib
    assert data

#@pytest.mark.skip(reason="Yahoo finance broke the API")
def test_get_stock_dataframe_shape(import_lib):
    data = import_lib
    df = data.get_war_index()
    assert df.shape == (len(df.index), 8)
