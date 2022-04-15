#!/bin/bash
docker run \
    -d \
    --init \
    --rm \
    -p 15000:5000 \
    -p 16006:6006 \
    -p 18501-18511:8501-8511 \
    -p 18888:8888 \
    -it \
    --gpus=all \
    --ipc=host \
    --name=newcomer \
    --env-file=.env \
    --volume=$PWD:/workspace \
    newcomer:latest \
    ${@-fish}
