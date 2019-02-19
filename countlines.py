import os

for check_dir(path):
    print(f"In {path}...")
    for name in os.listdir(path):
        print(f"Checking {name}")
        if os.path.isfile(os.path.join(path, name):
            print(name)
        if os.path.isdir(name):
            check_dir(os.path.join(path, name))

