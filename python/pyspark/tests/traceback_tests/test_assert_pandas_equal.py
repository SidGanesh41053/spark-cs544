import pandas as pd
from pyspark.testing.pandasutils import PandasOnSparkTestUtils

class TestTracebackPandasEqual(PandasOnSparkTestUtils):

    def test_simple_mismatch(self):
        left = pd.DataFrame({"a": [1, 2, 3]})
        right = pd.DataFrame({"a": [1, 999, 3]})

        # This should fail and produce a traceback
        self.assertPandasEqual(left, right)
