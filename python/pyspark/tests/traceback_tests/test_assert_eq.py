import pandas as pd
from pyspark.testing.pandasutils import PandasOnSparkTestUtils

class TestTracebackAssertEq(PandasOnSparkTestUtils):

    def test_assert_eq_list_mismatch(self):
        self.assert_eq([1, 2, 3], [1, 999, 3])
