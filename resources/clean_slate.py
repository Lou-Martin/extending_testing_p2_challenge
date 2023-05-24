import os
import shutil

def clean_slate():
    # Directory paths
    clean_slate_dir = "./clean_slate/"
    testing_grounds_dir = "./testing_grounds/"

    # Remove the testing_grounds directory if it exists
    if os.path.exists(testing_grounds_dir):
        shutil.rmtree(testing_grounds_dir)

    # Copy clean_slate to testing_grounds
    shutil.copytree(clean_slate_dir, testing_grounds_dir)

if __name__ == "__main__":
    clean_slate()
