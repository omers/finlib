def test_import(import_lib):
    data = import_lib
    assert data


def test_get_solar_cycle_shape(import_lib):
    data = import_lib
    df = data.get_solar_cycle()
    assert df.shape == (len(df), 7)
