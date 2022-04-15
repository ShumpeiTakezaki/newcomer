#!/bin/bash
docker exec -itd newcomer tensorboard --logdir=. --host=0.0.0.0 --port=${@-6006}
