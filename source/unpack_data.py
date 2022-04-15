import tarfile 

if __name__ == "__main__":
    for type in ["train", "val", "test"]:
        with tarfile.open(name=f'source/Dataset/{type}.tar.gz', mode='r') as tar:
            tar.extractall("source/Dataset")