import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live() as live:
    # live.log_param("trigger", random.random())
    accuracy = 0.85
    for i in range(params["epochs"]):
        # live.log_metric("foo", i + random.random())
        # live.log_metric("bar", i + random.random())
        accuracy += 0.009 + random.uniform(0.0001, 0.001)
        live.log_metric("accuracy", accuracy)
        live.next_step()

        time.sleep(6)

time.sleep(5)

live.end()
