from wine_model import make_df

def test_something():
    my_dataframe = make_df()
    assert(len(my_dataframe) == 4)