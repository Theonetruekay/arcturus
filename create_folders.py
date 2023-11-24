import os

# Define the folder structure
folders = [
    "Arcturus",
    "Arcturus/libraries",
    "Arcturus/data_loading_preprocessing",
    "Arcturus/train_test_split",
    "Arcturus/model_architecture",
    "Arcturus/model_training",
    "Arcturus/model_evaluation",
    "Arcturus/additional_techniques"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create some initial files
with open("Arcturus/libraries/requirements.txt", "w") as file:
    file.write("pandas\nnumpy\ntensorflow\nscikit-learn\n")

with open("Arcturus/data_loading_preprocessing/data_loader.py", "w") as file:
    file.write("# Data loading and preprocessing scripts\n")

# ... similar for other folders

print("Folder structure created successfully.")
