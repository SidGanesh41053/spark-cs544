import time
from pyspark.testing.utils import eventually

def test_eventually_timeout():
    def f():
        time.sleep(0.1)
        return False

    # Should fail, produce traceback
    eventually(lambda: f(), timeout=0.2, interval=0.05)
