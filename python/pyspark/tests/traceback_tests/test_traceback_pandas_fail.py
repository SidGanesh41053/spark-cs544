import pandas as pd
from pyspark.testing.pandasutils import PandasOnSparkTestUtils

def test_pandas_equal_traceback():
    utils = PandasOnSparkTestUtils()

    left = pd.DataFrame({"a": [1, 2, 3]})
    right = pd.DataFrame({"a": [1, 999, 3]})

    # DO NOT CATCH THE ERROR
    utils.assertPandasEqual(left, right)
