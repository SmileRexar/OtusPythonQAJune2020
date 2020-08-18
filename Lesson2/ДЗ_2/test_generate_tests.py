from collections import namedtuple

import pytest
import pandas as pd
import numpy as np



def pytest_generate_tests(metafunc):
    if "fixture_pd" in metafunc.fixturenames:
        products = {
            'Product': ['Tablet', 'iPhone', 'Laptop', 'Monitor', 'Monitor', 'Monitor', 'Monitor', 'Monitor', 'Monitor'],
            'Price': [250, 800, 1200, 300, 3, 4, 5, 65, 4]
            }
        df = pd.DataFrame(products, columns=['Product', 'Price'])
        metafunc.parametrize("fixture_pd",  df.itertuples() )




def test_foobar(fixture_pd):
    print(type(fixture_pd))
    print(fixture_pd.Price)




