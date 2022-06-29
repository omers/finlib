dates = {'Date': ["1998-07-20", "2007-10-11", "2008-09-16", "2020-02-24"]}

def test_import(import_lib):
    data = import_lib
    assert data


def test_get_pi_cycles_shape(import_lib):
    data = import_lib
    df = data.get_pi_cycles(dates)
    assert df.shape == (4, 7)
