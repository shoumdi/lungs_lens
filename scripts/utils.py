import os


import os
import subprocess
from functools import wraps

def download_dataset(dataset_path, kaggle_dataset):
    if os.path.exists(dataset_path) and os.listdir(dataset_path):
        print("Dataset already exists. Skipping download.")
    else:
        print("Downloading dataset from Kaggle...")
        os.makedirs(dataset_path, exist_ok=True)

        subprocess.run(
            [
                "kaggle", "datasets", "download",
                "-d", kaggle_dataset,
                "-p", dataset_path,
                "--unzip"
            ],
            check=True
        )    
