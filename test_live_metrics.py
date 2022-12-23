import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live() as live:
    # live.log_param("trigger", random.random())
    accuracy = 0.82
    for i in range(params["epochs"]):
        # live.log_metric("foo", i + random.random())
        # live.log_metric("bar", i + random.random())
        live.log_metric("accuracy", accuracy)

        accuracy += random.uniform(0.001, 0.02)
        if accuracy > 0.98:
            accuracy = random.uniform(0.98, 0.99)
        
        live.next_step()

        time.sleep(6)

time.sleep(5)

live.end()
