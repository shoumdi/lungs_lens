import time
import os
import subprocess
from functools import wraps

def time_spent(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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

            return func(*args, **kwargs)
        return wrapper
    return decorator