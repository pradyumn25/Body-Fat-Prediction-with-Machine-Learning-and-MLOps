import os

dirs = [  # creating the directories for various files
    os.path.join("data", "raw"),  # file for the raw data
    # file for the data where we are keeping all the data after processing it
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

# we are using the os.path.join() so on the basis of your opertaing system it will join the path

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # it is just to make a gitkeep file so while we are pushing the directories it has something to as git does not allow us to push the empty repo.
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]


for file_ in files:
    os.makedirs(file_, exist_ok=True)
    # it is just to make a gitkeep file so while we are pushing the directories it has something to as git does not allow us to push the empty repo.
    with open(os.path.join(file_, ".gitkeep"), "w") as f:
        pass
